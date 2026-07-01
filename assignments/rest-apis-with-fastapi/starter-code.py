"""Starter code for Building REST APIs with FastAPI assignment.

Run locally:
    uvicorn starter-code:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class TaskCreate(BaseModel):
    """Incoming payload for creating a task."""

    title: str
    completed: bool = False


tasks = []
next_id = 1


@app.get("/")
def root():
    return {"message": "Task API is running"}


@app.get("/tasks")
def list_tasks():
    return {"tasks": tasks}


@app.post("/tasks")
def create_task(payload: TaskCreate):
    global next_id
    task = {
        "id": next_id,
        "title": payload.title,
        "completed": payload.completed,
    }
    tasks.append(task)
    next_id += 1
    return {"task": task}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted = tasks.pop(index)
            return {"deleted": deleted}

    raise HTTPException(status_code=404, detail="Task not found")
