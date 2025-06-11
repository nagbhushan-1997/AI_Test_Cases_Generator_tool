from git import Repo

def get_changed_files(repo_path):
    repo = Repo(repo_path)
    return [item.a_path for item in repo.index.diff(None)]

def get_file_diff(repo_path, filename):
    repo = Repo(repo_path)
    diff = repo.git.diff(filename)
    return diff