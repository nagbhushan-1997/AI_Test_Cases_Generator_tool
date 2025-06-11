import subprocess

def run_tests(path):
    result = subprocess.run(["pytest", path], capture_output=True, text=True)
    return result.stdout