import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Define the system message
system_message = {"role": "system", "content": "You are a helpful assistant that answers Python programming questions."}

# Define a function to get a response from the model
def get_response(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[system_message, {"role": "user", "content": message}]
    )
    return response.choices[0].message.content

# Streamlit app
def main():
    st.title("Python Programming Assistant")
    user_input = st.text_input("Ask a Python programming question:")
    if st.button("Submit"):
        if user_input:
            st.write("Please wait, generating response...")
            response = get_response(user_input)
            st.write(response)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()