import requests
import json

# Gitea API base URL
API_URL = "https://vcs.zapuza.com/api/v1/admin/"
# USER_DATA_FILE = "users.csv"

def create_user(username, email, password):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic c2tiZWxhbHNhaGViOkJlbGFsQDA5OCM=" #https://vcs.zapuza.com/api/swagger (Get Auth Token)
    }
    data = {
        "username": username,
        "email": email,
        "password": password,
        "name": username, # or use a real full name
        "admin": False, # or set to True for admin users
    }
    url = f"{API_URL}/users"
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        return True, response.json() # Return success and the response data
    except requests.exceptions.RequestException as e:
        print(f"Error creating user {username}: {e}")
        return False, str(e)

# --- Main ---
if __name__ == "__main__":
    user_data = [
        {"username": "user1", "email": "user1@example.com", "password": "password1"},
        {"username": "user2", "email": "user2@example.com", "password": "password2"},
        # ... Add more users
    ]

    for user in user_data:
        username = user["username"]
        email = user["email"]
        password = user["password"]

        success, result = create_user(username, email, password)
        if success:
            print(f"User {username} created successfully!")
        else:
            print(f"Failed to create user {username}: {result}")