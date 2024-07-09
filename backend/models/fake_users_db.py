# fake_users_db.py

users_db = [
    {"id": 1, "username": "john", "email": "john@example.com", "hashed_password": "hashed_password_1"},
    {"id": 2, "username": "jane", "email": "jane@example.com", "hashed_password": "hashed_password_2"},
    {"id": 3, "username": "bob", "email": "bob@example.com", "hashed_password": "hashed_password_3"},
    # Add more users here...
]


def get_user(username: str):
    for user in users_db:
        if user["username"] == username:
            return user
    return None


def get_user_by_email(email: str):
    for user in users_db:
        if user["email"] == email:
            return user
    return None


