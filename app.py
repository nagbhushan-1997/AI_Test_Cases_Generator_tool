import streamlit as st
from utils.git_utils import get_changed_files, get_file_diff
from utils.llm_utils import suggest_test_changes
from utils.test_runner import run_tests

st.title("🤖 AI Test Automation Tool")

repo_path = st.text_input("Enter Git Repo Path", value="./")

if st.button("Detect Changes"):
    files = get_changed_files(repo_path)
    for f in files:
        st.write(f"📄 {f}")
        diff = get_file_diff(repo_path, f)
        st.code(diff, language="diff")
        if st.button(f"Suggest Test Updates for {f}"):
            suggestions = suggest_test_changes(f, diff)
            st.code(suggestions, language="python")

if st.button("Run Tests"):
    output = run_tests(repo_path)
    st.code(output)