# userInput = input("Enter the username")

# name = ["name1", "name2","name3","name4"]

# for i in name:
#     print(i)

# name = []
# for i in range(0,3):
#     userInput = input("Enter the username")
#     name.append(userInput)

# for i in name:
#     print(f"https://api.github.com/users/{i}")

# import requests
# url = []
# for i in range(0,3):
#     userInput = input("Enter the username")
#     url.append(f"https://api.github.com/users/{userInput}")

# for i in url:
#     print(i)

# for i in url:
#     try:
#         r = requests.get(i, timeout=10)
#         r.raise_for_status()
#         user = r.json()
#         print(user["name"], user["public_repos"])
#         # print(user)
#     except requests.Timeout:
#         print("Request timed out")
#     except requests.HTTPError as e:
#         print(f"HTTP error: {e.response.status_code}")
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

           with open("assignment/errors.log", "a") as file:
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
            break
# CSV-writing code
fieldnames = ["login" , "name" , "public_repos" , "followers"]
with open("github_users.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_users)
