import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask_query" 

st.title("Medical RAG")
st.markdown("Enter you query below : ")

# Input fields
query = st.text_input("Query")

if st.button("Generate RAG response"):
    input_data = {
        "query" : query
    }

    try:
        response = requests.get(API_URL, json=input_data)
        result = response.json()
    
        if response.status_code == 200:
            resp = result["response"]
            st.success(f"RAG response : **{resp}**")

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")