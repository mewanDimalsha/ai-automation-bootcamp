import requests
import json

users = requests.get("https://jsonplaceholder.typicode.com/users")
posts = requests.get("https://jsonplaceholder.typicode.com/posts")

users_response = users.json()
posts_response = posts.json()
responseLength = len(users_response)
# print(users_response)
# print(posts_response)
# print("Number of users retrieved:", responseLength)

user_posts = {}

for user in users_response:
    user_posts[user["id"]] = [
        post for post in posts_response if post["userId"] == user["id"]
    ]

# Save users_response to a JSON file
file_path = "data.json"
try:
    with open(file_path, "w") as json_file:
        json.dump(user_posts, json_file, indent=4)
    print(f"Data successfully written to {file_path}")
except IOError as e:
    print(f"Error writing to file {file_path}: {e}")
