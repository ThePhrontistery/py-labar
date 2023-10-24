from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    return {"user_id": user_id}
