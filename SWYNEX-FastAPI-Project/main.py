
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="SWYNEX Task Manager API",
    description="A beginner-friendly task management API",
    version="1.0.0"
)

# Temporary storage for tasks
tasks = []
next_id = 1


class Task(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=100,
        description="Task title"
    )
    completed: bool = False


@app.get("/")
def home():
    return {
        "message": "Welcome to SWYNEX Task Manager API!",
        "docs": "/docs"
    }


@app.post("/tasks", status_code=201)
def create_task(task: Task):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title.strip(),
        "completed": task.completed
    }

    if not new_task["title"]:
        raise HTTPException(
            status_code=422,
            detail="Task title cannot be empty or spaces only"
        )

    tasks.append(new_task)
    next_id += 1
    return new_task


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
