# GitHub Profile CLI

## Description
A Python command-line program that fetches GitHub profile information for multiple usernames and saves the results in a CSV file.

The program retrieves:
- Login
- Name
- Public repositories
- Followers

It also retries timed-out requests and logs timeout and HTTP errors to a file.

## Requirements
- Python 3
- Git
- A virtual environment
- The `requests` package

## Setup Instructions

1. Clone this repository.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment.
4. Install the required package:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the Python program:

   ```bash
   python main.py
   ```

   Replace `main.py` with your actual Python filename if it is different.

## Example Output

The CSV file `github_users.csv` contains columns like these:

| login | name | public_repos | followers |
|---|---|---:|---:|
| octocat | The Octocat | 8 | 1000 |

*Example values are illustrative.*

## Error Logging

Errors are recorded in `errors.log` when a request times out or GitHub returns a non-success HTTP status code.