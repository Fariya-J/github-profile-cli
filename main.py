import requests
import csv
usernames = []
all_users = []
for i in range(3):
    name = input("Enter the username: ")
    usernames.append(name)
for i in usernames:
    for attempt in range(3):
        try:
            response = requests.get(
                f"https://api.github.com/users/{i}", timeout=10
            )
        except requests.Timeout:
           print(f"Request timed out for {i}")

           with open("errors.log", "a") as file:
            file.write(f"Request timed out for {i}\n")
           continue

        if response.status_code == 200:
            data = response.json()

            login = data["login"]
            repos = data["public_repos"]
            name = data["name"]
            followers = data["followers"]

            user_data = {
                "login": login,
                "name": name,
                "public_repos": repos,
                "followers": followers
            }

            all_users.append(user_data)
            break

        else:
            print(f"Request failed for {i}: {response.status_code}")

            with open("errors.log", "a") as file:
                file.write( f"Request failed for {i}: {response.status_code}\n")
            continue
# CSV-writing code
fieldnames = ["login" , "name" , "public_repos" , "followers"]
with open("github_users.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_users)
