# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using FastAPI by creating endpoints, validating request data with Pydantic models, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Build a FastAPI application for a simple task manager. Start by defining routes that let users check API status and perform basic CRUD-style operations for tasks.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Add a `GET /` endpoint that returns a welcome or status message.
- Add a `GET /tasks` endpoint that returns a list of tasks.
- Add a `POST /tasks` endpoint that creates a new task and returns the created item.
- Add a `DELETE /tasks/{task_id}` endpoint that removes a task by ID and returns a confirmation message.

### 🛠️ Add Data Validation and Error Handling

#### Description
Improve the API by validating input data and handling common errors so responses are clear and reliable.

#### Requirements
Completed program should:

- Define a Pydantic model for task input (for example: `title`, `completed`).
- Reject invalid payloads automatically through FastAPI validation.
- Return a `404` error when a task ID does not exist.
- Ensure each endpoint returns JSON responses with clear keys and values.
- Include at least one example request and response in comments or docstrings.
