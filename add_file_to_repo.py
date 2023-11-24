import requests
import base64
import os
import json

# add/uploads given content as new file in github.com repo
def add_file_to_repo(token, username, repo, file_path, commit_message, content):
    url = f"https://api.github.com/repos/{username}/{repo}/contents/{file_path}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Prepare and upload data
    encoded_content = base64.b64encode(content.encode()).decode()
    data = {
        "message": commit_message,
        "content": encoded_content
    }
    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"File {file_path} added successfully.")
    else:
        print(f"Failed to add file {file_path}.")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")


# Github.com data
stored_token_path = '../private/credentials_github_api.json' # Contains the token as plain text
if os.path.exists(stored_token_path):
  with open(stored_token_path, 'r') as f:
      github_credentials = json.load(f)
else:
  github_credentials = {}
  github_credentials['api_token'] = "DUMMY_TOKEN"
  github_credentials['username']  = "DUMMY_OWNER"
  github_credentials['repo_name'] = "DUMMY_REPO"


# Content
repo_path_of_new_file = "automatic_upload.test"
commit_message = "File added"
content = "Dummy content of file."

add_file_to_repo(github_credentials['token'] , github_credentials['username'], github_credentials['repo_name'], 
                 repo_path_of_new_file, commit_message, content)