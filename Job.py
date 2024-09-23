import streamlit as st
import pandas as pd
import numpy as np

# Mock function to simulate job recommendation
def mock_recommend_jobs(resume_text, job_title, top_x):
    # Simulate some recommendations
    jobs = [
        {"Job Title": "Data Scientist", "Company": "Company A", "Match Score": 92},
        {"Job Title": "Machine Learning Engineer", "Company": "Company B", "Match Score": 89},
        {"Job Title": "AI Specialist", "Company": "Company C", "Match Score": 85},
        {"Job Title": "Software Engineer", "Company": "Company D", "Match Score": 80},
    ]
    # Sort jobs based on the Match Score (mocked) and return top_x results
    recommended_jobs = sorted(jobs, key=lambda x: x["Match Score"], reverse=True)[:top_x]
    return recommended_jobs
def App():
    # Streamlit App
    st.title("Job Recommendation System")

    # User input: Resume upload
    st.header("Upload Your Resume")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])

    # User input: Desired job title
    job_title = st.text_input("Enter the job title you are looking for")

    # User input: Number of top results
    top_x = st.number_input("Enter the number of top results you want", min_value=1, max_value=10, value=3)

    if st.button("Get Recommendations"):
        if uploaded_file is not None and job_title:
            # Mock reading of resume content (In real scenario, you would parse the resume)
            resume_text = uploaded_file.getvalue().decode("utf-8", errors="ignore")
            print(resume_text)
            # Mock recommendation function
            recommendations = mock_recommend_jobs(resume_text, job_title, top_x)
            
            # Display the results
            st.header(f"Top {top_x} Job Recommendations")
            if recommendations:
                for i, job in enumerate(recommendations, 1):
                    st.write(f"{i}. **{job['Job Title']}** at **{job['Company']}** (Match Score: {job['Match Score']}%)")
            else:
                st.write("No recommendations found.")
        else:
            st.error("Please upload your resume and enter a job title.")

