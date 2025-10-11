import streamlit as st
import json
from agents.reader_agent import executor as reader_executor
from agents.categorizer_agent import executor as categorizer_executor
from agents.validator_agent import executor as validator_executor
from agents.self_healer_agent import executor as healer_executor
from langchain.memory import ConversationBufferMemory

st.set_page_config(page_title="Case Study Analyzer (MCP)", layout="centered")

st.title("📘 Case Study Analyzer — MCP Workflow")

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

user_input = st.text_input("Enter file path or URL to analyze:")

if st.button("Run Analysis") and user_input:
    with st.spinner("Running Reader Agent..."):
        reader_output = reader_executor.invoke({"input": user_input})
    st.success("Reader output ready ✅")

    with st.spinner("Running Categorizer Agent..."):
        categorizer_output = categorizer_executor.invoke({"input": reader_output["output"]})
    st.success("Categorizer output ready ✅")

    with st.spinner("Validating..."):
        validation_output = validator_executor.invoke({
            "input": f"Reader: {reader_output['output']} | Categorizer: {categorizer_output['output']}"
        })
    st.success("Validation done ✅")

    if "false" in validation_output["output"].lower():
        with st.spinner("Running Self-Healer..."):
            healer_output = healer_executor.invoke({"input": validation_output["output"]})
        st.success("Healed version generated ✅")
    else:
        healer_output = {"output": "All good! ✅"}

    # Display results
    st.subheader("Results")
    st.write("**Reader Output:**", reader_output["output"])
    st.write("**Categorizer Output:**", categorizer_output["output"])
    st.write("**Validator Output:**", validation_output["output"])
    st.write("**Self-Healer Output:**", healer_output["output"])
