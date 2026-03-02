import streamlit as st
import csv
import os
import re

st.title("My Small Business")
st.subheader("Description of my small business", divider="violet")

# Create the form
with st.form("ask_question_form", clear_on_submit=True):
    st.subheader("Ask me a question:")

    description = st.text_area(
        "A description of why you're reaching out, including any questions you have."
    )

    email = st.text_input(
        "What email can I reach you at?"
    )

    submitted = st.form_submit_button("Submit")

# Process form submission
if submitted:

    # Basic validation
    if not description.strip():
        st.error("Please enter a description.")
    elif not email.strip():
        st.error("Please enter your email.")
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        st.error("Please enter a valid email address.")
    else:
        file_exists = os.path.isfile("user_requests.csv")

        with open("user_requests.csv", "a", newline="") as csv_file:
            writer = csv.writer(csv_file)

            # Write header only once
            if not file_exists:
                writer.writerow(["Description", "Email"])

            writer.writerow([description, email])

        st.success("Your question has been submitted successfully!")
