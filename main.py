from fastapi import FastAPI

app = FastAPI()

exercises =[
    {
        "exercise_id":1,
        "target" :"足",
        "exercise": "デッドリフト"
    }
]

set_logs = [
    {
        "id": 1,
        "exercise_id": 1,
        "weight": 60,
        "reps": 10,
        "set_number": 1
    },
    {
        "id": 2,
        "exercise_id": 1,
        "weight": 60,
        "reps": 8,
        "set_number": 2
    }
]


@app.get("/exercises")
def get_exercises():
    return exercises


@app.get("/set-logs")
def get_set_logs():
    return set_logs