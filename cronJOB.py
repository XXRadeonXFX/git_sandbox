from github import Github
import os
import subprocess

# Configuration
GITHUB_TOKEN = "your_github_token_here"  # Replace with your GitHub Personal Access Token
REPO_NAME = "username/repository"  # Format: "owner/repo"
BRANCH = "main"  # Change this to your branch name
LAST_COMMIT_FILE = "/path/to/last_commit.txt"  # File to store the last checked commit hash
SCRIPT_TO_RUN = "/path/to/run_script.sh"  # Script to execute on new commit

def get_latest_commit():
    """Fetches the latest commit hash from GitHub."""
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    branch = repo.get_branch(BRANCH)
    return branch.commit.sha

def get_stored_commit():
    """Reads the last stored commit hash."""
    if os.path.exists(LAST_COMMIT_FILE):
        with open(LAST_COMMIT_FILE, "r") as file:
            return file.read().strip()
    return None

def update_stored_commit(commit_hash):
    """Updates the stored commit hash."""
    with open(LAST_COMMIT_FILE, "w") as file:
        file.write(commit_hash)

def run_script():
    """Executes the script when a new commit is detected."""
    subprocess.run(["bash", SCRIPT_TO_RUN], check=True)

def main():
    latest_commit = get_latest_commit()
    stored_commit = get_stored_commit()

    if latest_commit and latest_commit != stored_commit:
        print(f"New commit detected: {latest_commit}")
        run_script()
        update_stored_commit(latest_commit)
    else:
        print("No new commit detected.")

if __name__ == "__main__":
    main()
