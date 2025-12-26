import streamlit as st
import google.generativeai as genai
import pandas as pd

# 1. Setup Page Config
st.set_page_config(
    page_title="AI Data Architect | Build the Future",
    page_icon="📊",
    layout="centered"
)

# Professional Header
st.title("🚀 AI Data Architect")
st.markdown("""
    **Transforming unstructured business chaos into structured insights.**
    This prototype uses Gemini 1.5 Flash to help small businesses automate data entry.
""")

# 2. Configure Gemini (Using Streamlit Secrets for Security)
# Session 4: "Guard Your Master Key (API Security)" - Never hardcode the key.
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # "Golden Prompt" Configuration
    # Session 4 Action Item: Encode your "Founder" Persona (Identity, Tone, Behavior, Constraints)
    model = genai.GenerativeModel(
        model_name="gemini-flash-latest", 
        system_instruction="You are a Data Expert. Convert messy input into a clean CSV-style table. Identify Date, Description, Category, and Amount. Output ONLY the data in a clear table format."
    )
    
else:
    st.error("Missing API Key! Please add 'GEMINI_API_KEY' to your Streamlit Secrets.")
    st.stop()

# 3. User Interface
st.divider()
data_input = st.text_area(
    "Paste messy data below:", 
    placeholder="Example: Dec 24, bought 50kg steel for 4000. Dec 26, paid 500 for transport...",
    height=200
)

# Advanced Options (Demonstrates 'Temperature' control from Session 4)
with st.expander("Advanced Settings"):
    temp = st.slider("Creativity (Temperature)", 0.0, 1.0, 0.1) 

if st.button("Generate Structured Table", type="primary"):
    if data_input:
        with st.spinner("Gemini is structuring your data..."):
            try:
                # Generate content with specific generation config
                response = model.generate_content(
                    data_input,
                    generation_config=genai.types.GenerationConfig(
                        temperature=temp,
                    )
                )
                
                # Display Result
                st.subheader("📊 Structured Business Data")
                st.markdown(response.text)
                
                # Final Professional Touch
                st.success("Prototype processing complete. Data ready for export.")
                st.info("💡 Tip: Use this to quickly update your SQL databases or Excel sheets.")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text to process.")

# Footer for Judges
st.divider()
st.caption("Submitted for Startup School: Prompt to Prototype | Build the Future Showcase")
