OCR and Document Classification Pipeline

This project utilizes LangChain to build an AI-driven pipeline for processing and classifying documents. 
It integrates minicpm-v via Ollama for detailed vision-based OCR and Google's Gemini AI for classification, ensuring an end-to-end automated document analysis workflow.


Overview

The pipeline consists of the following stages:

1) Image Extraction - Extracts images from PDFs or processes standalone images.

2) Image Description - Uses minicpm-v via Ollama and LangChain to generate detailed descriptions of the images.

3) Document Grouping - Classifies documents based on their descriptions and Organizes classified documents by category using Google's Gemini AI.

4) Summarization - Produces a structured summary of grouped classified documents.

5) Evaluation - Compares AI classifications to ground truth labels to assess accuracy.

Features

✅ Extract images from PDFs and standalone image files
✅ Analyze images using minicpm-v via Ollama for highly detailed descriptions
✅ Classify documents into predefined categories using Gemini AI
✅ Generate structured summaries of classified documents
✅ Evaluate accuracy of AI-based document classification

Prerequisites

Python Version: 3.7 or higher
Ollama Installed (Installation Guide)
Dependencies: Listed in requirements.txt
APIs:
Ollama (for minicpm-v model)
Google Gemini API (set in .env file)


Installation

1. Clone the Repository
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository

2. Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Install Ollama and Load minicpm-v Model
ollama pull minicpm-v

5. Configure Environment Variables
Create a .env file and add:
GEMINI_API_KEY=your_gemini_api_key_here

6. Prepare Data
Place source PDFs in data/pdfs/ before running the pipeline.


Usage

1. Image Extraction
Extract images from PDF files:
python src/extraction/extract_images.py
Input: PDFs in data/pdfs/
Output: Extracted images saved to data/extracted_images/

2. Image Description
Generate descriptions using minicpm-v via Ollama:
python src/description/describe_images.py
Output: extracted_descriptions.json in data/

3. Document Classification and Grouping Documents
Classify extracted images using Gemini AI:
python src/classification/group_documents.py
Output: grouped_classified_documents.json

4. Summarization
Summarize the grouped classified documents:
python src/summarization/summarize_documents.py
Output: A structured summary of classified documents

5. Accuracy Evaluation
Evaluate classification accuracy:
python src/evaluation/calculate_accuracy.py
Output: Accuracy score printed in the console
