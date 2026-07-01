# 📘 Assignment: FastAPI + SQLite To-Do API

## 🎯 Objective

Build a REST API that stores data in SQLite using FastAPI. You will connect API endpoints to a database, run SQL queries for CRUD operations, and return clear JSON responses.

## 📝 Tasks

### 🛠️ Build a Persistent To-Do API

#### Description
Create a FastAPI application for managing to-do items. Instead of storing tasks in memory, use a SQLite database so data persists between runs.

#### Requirements
Completed program should:

- Create or connect to a SQLite database file (for example: `tasks.db`).
- Create a `tasks` table with fields such as `id`, `title`, and `completed`.
- Add a `GET /tasks` endpoint that returns all tasks from the database.
- Add a `POST /tasks` endpoint that inserts a new task into the database.
- Add a `DELETE /tasks/{task_id}` endpoint that deletes a task by ID.

### 🛠️ Add Validation and Robust Error Handling

#### Description
Improve API reliability by validating input and handling common error scenarios with clear HTTP responses.

#### Requirements
Completed program should:

- Define a Pydantic model for incoming task data.
- Validate that task titles are not empty.
- Return a `404` response when trying to delete a non-existent task.
- Return consistent JSON responses with meaningful keys.
- Include at least one commented example request/response for testing.
