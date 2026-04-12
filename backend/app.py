import streamlit as st
from log_parser import extract_issues
from ai_engine import analyze_errors

st.set_page_config(page_title="AI Log Analyzer", layout="wide")

st.title("🚀 AI Log Analyzer")

uploaded_file = st.file_uploader("Upload your log file", type=["txt", "log"])

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")

    issues = extract_issues(content)
    analysis = analyze_errors(issues["errors"])

    st.subheader("❌ Errors")
    for e in issues["errors"]:
        st.error(f"{e['message']} ({e['severity']})")

    st.subheader("⚠️ Warnings")
    for w in issues["warnings"]:
        st.warning(f"{w['message']} ({w['severity']})")

    st.subheader("🧠 AI Analysis")
    st.code(analysis)