"""Starter code for FastAPI + SQLite To-Do API assignment.

Run locally:
    uvicorn starter-code:app --reload
"""

import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()
DB_PATH = Path(__file__).with_name("tasks.db")


class TaskCreate(BaseModel):
    """Incoming payload for creating a task."""

    title: str = Field(min_length=1)
    completed: bool = False


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/")
def root() -> dict:
    return {"message": "FastAPI + SQLite To-Do API is running"}


@app.get("/tasks")
def list_tasks() -> dict:
    with get_connection() as conn:
        rows = conn.execute("SELECT id, title, completed FROM tasks ORDER BY id").fetchall()

    tasks = [
        {"id": row["id"], "title": row["title"], "completed": bool(row["completed"])}
        for row in rows
    ]
    return {"tasks": tasks}


@app.post("/tasks")
def create_task(payload: TaskCreate) -> dict:
    title = payload.title.strip()
    if not title:
        raise HTTPException(status_code=422, detail="Title cannot be empty")

    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, completed) VALUES (?, ?)",
            (title, int(payload.completed)),
        )
        task_id = cursor.lastrowid

    return {
        "task": {
            "id": task_id,
            "title": title,
            "completed": payload.completed,
        }
    }


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict:
    with get_connection() as conn:
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    # Example response: {"message": "Task 3 deleted"}
    return {"message": f"Task {task_id} deleted"}
