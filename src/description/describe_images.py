import os
import base64
import json
from langchain_ollama import OllamaLLM

# Load the Ollama vision model
llm = OllamaLLM(model="minicpm-v:latest")

# Function to encode an image in base64 format
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Get first two images from 'extracted_images' folder
image_folder = "../../data/extracted_images"
image_files = sorted(os.listdir(image_folder))  # Pick first two images

# Dictionary to store image descriptions
image_descriptions = {}

# Loop through the selected images and generate descriptions
for image_name in image_files:
    image_path = os.path.join(image_folder, image_name)
    encoded_image = encode_image(image_path)

    # Define the prompt
    prompt = "You are a highly detailed vision AI assistant specialized in OCR. Your task is to analyze the following image and provide a comprehensive description in English that includes every visible detail. Include all text (including fonts, sizes, and styles), numbers, symbols, logos, dates, addresses, annotations, handwriting, colors, layout information, and any other visual elements. Do not omit any detail, no matter how minor."

    # Invoke the model with the images parameter
    response = llm.invoke(prompt, images=[encoded_image])

    # Store the response in the dictionary
    image_descriptions[image_name] = response

# Save the dictionary as a JSON file
json_path = "../../data/extracted_descriptions.json"
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(image_descriptions, json_file, indent=4)

print(f"Descriptions saved to {json_path}")