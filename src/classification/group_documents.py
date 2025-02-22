import json
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access the Gemini API key
gemini_api_key = os.getenv('GEMINI_API_KEY')

# ✅ Explicitly set the API key
genai.configure(api_key=gemini_api_key)

# ✅ Pass the API key when creating the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=gemini_api_key)

# Load extracted descriptions from JSON file
json_path = "../../data/extracted_descriptions.json"

with open(json_path, "r", encoding="utf-8") as json_file:
    image_descriptions = json.load(json_file)

# Dictionary to store categorized descriptions
categorized_documents = {}

# Prompt template for classification
classification_prompt = """
You are a document classification expert. Given the description of an image, classify the document into one of the following categories:
- Prescription
- Discharge Summary
- Cancelled Cheque 
- Pharmacy Bill
- Bank Statement
- Clinic Payment Receipt
- Lab Report
- Cash Credit Memo

TEXT:
{description}

Return ONLY the category name.
"""

# Process each image description
for image_name, description in image_descriptions.items():
    # Format the prompt
    prompt = classification_prompt.format(description=description)

    # Get classification response from Gemini
    response = llm.invoke(prompt)
    category = response.content.strip()

    # ✅ Store descriptions grouped by category
    if category not in categorized_documents:
        categorized_documents[category] = []  # Create a list if category is new
    categorized_documents[category].append(description)

# ✅ Save Output JSON in grouped format
output_json_path = "../../data/grouped_classified_documents.json"

with open(output_json_path, "w", encoding="utf-8") as output_file:
    json.dump(categorized_documents, output_file, indent=4)

print(f"Classified results saved to {output_json_path}")
