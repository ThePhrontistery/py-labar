from fastapi import FastAPI

app = FastAPI()

mock_users = [
    {"id": 1, "username": "pchocron", "name": "Paola Chocron"},
    {"id": 2, "username": "jjarbona", "name": "Juan Arbona"},
    {"id": 3, "username": "andsanchez", "name": "Andrés Sánchez"},
]

@app.get("/user_data")
def get_users():
    """
    This route (endpoint) allows a client to retrieve all user data from the mock dataset. The path for this endpoint is //user_data
    Retrieve the list of all users from the mock dataset.
    Returns: A list of dictionaries, where each dictionary represents a user's information.
    """
    return mock_users

@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    """
    Retrieve a specific user's information by their ID.
    Args: user_id (int): The ID of the user to retrieve.
    Returns:  A dictionary containing the user's information or an error message if not found.
    """
    user = next((u for u in mock_users if u["id"] == user_id), None)
    if user is None:
        return "Usuario no encontrado"
    return user