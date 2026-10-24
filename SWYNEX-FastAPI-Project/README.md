# SWYNEX Task Manager API

A beginner-friendly Task Manager API built using Python and FastAPI.

## Features

- Create a new task
- View all tasks
- View a task by its ID
- Delete a task
- Input validation
- Error handling for tasks that do not exist

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## How to Run

1. Install the required packages:

   `python -m pip install -r requirements.txt`

2. Start the server:

   `python -m uvicorn main:app --reload`

3. Open the API documentation in your browser:

   http://127.0.0.1:8000/docs

## Validation and Error Handling

- Returns a validation error if the task title is empty.
- Returns a 404 error if the requested task does not exist.
- Returns a success message when a task is deleted.

## Note

Tasks are stored temporarily in memory. They will reset when the server restarts.

## Author

SWYNEX