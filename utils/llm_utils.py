from ollama import Client

# Initialize Ollama client (works locally)
client = Client()

def suggest_test_changes(filename, code_diff):
    prompt = f"""You're an AI test expert. Given the following code diff from `{filename}`, generate or update the relevant Python test case accordingly.

Diff:
{code_diff}

Output only the updated or new test case code:"""

    response = client.chat(
        model='llama3.2',  # Or use your specific version like 'llama3:instruct' if tagged that way
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']