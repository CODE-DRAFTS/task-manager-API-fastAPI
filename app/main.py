from fastapi import FastAPI
from app import model, database
import psycopg2
from time import sleep


app = FastAPI()

while True:
    try:
        conn = psycopg2.connect( host="localhost",database="TaskManager", user="postgres", password="root")
        cursor = conn.cursor()
        break
    except Exception as error:
        print( error)
        sleep(2)


@app.get("/api/v1/tasks")  #get all tasks
async def get_all_tasks():
    return await database.get_all_tasks()

@app.post("/api/v1/tasks") #add a new task
async def get_all_tasks(task: model.AddTask):
    return await database.add_new_task(task)

@app.get("/api/v1/tasks/{task_id}") #get a single task
async def get_all_tasks(task_id: int):
    return await database.get_single_task(task_id)

@app.put("/api/v1/tasks/{task_id}") #update a task
async def update_tasks(task_id: int , task: model.UpdateTask):
    title = task.title
    completed = str( task.completed)
    return await database.update_task(str(task_id), title,  completed) 

@app.delete("/api/v1/tasks/{task_id}") # delete a task
async def get_all_tasks(task_id: int):
    return await database.delete_post( str(task_id) )



