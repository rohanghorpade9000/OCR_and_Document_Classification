import json
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get Gemini API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=gemini_api_key)

# Load LangChain Gemini Model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5, google_api_key=gemini_api_key)

# ✅ Load JSON File
input_json_path = "../../data/grouped_classified_documents.json"  # Change this to your JSON file

try:
    with open(input_json_path, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
except FileNotFoundError:
    print(f"❌ ERROR: {input_json_path} not found!")
    exit()

# ✅ Convert JSON Data to Text (Extract All Text)
json_text = json.dumps(json_data, indent=4)  # Converts JSON to string format

# ✅ Define Summarization Prompt
summarization_prompt = f"""
You are a highly detail-oriented AI assistant. Your task is to read the following JSON data—which contains information extracted from various documents—and produce a comprehensive and structured JSON output that captures every available detail. 

Include all pieces of information present in the input, such as dates, names, locations, numerical values, textual descriptions, labels, contact details, and any other context or metadata. Ensure no detail is omitted, regardless of how minor it might seem. Organize the output logically and use clear field names to represent each data point.

JSON Data:
{json_text}

**Summary:**
"""

# ✅ Get Summary from Gemini
response = llm.invoke(summarization_prompt)

# ✅ Print the Summary
print("🔹 Summary of JSON File:\n")
print(response.content)
