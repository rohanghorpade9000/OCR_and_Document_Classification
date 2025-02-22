import os
import fitz  # PyMuPDF
from PIL import Image
import shutil

def create_output_folder():
    output_folder = "../../data/extracted_images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder

def extract_images_from_pdf(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            img_ext = base_image["ext"]
            img_path = os.path.join(output_folder, f"page_{i+1}_img_{img_index+1}.{img_ext}")
            with open(img_path, "wb") as img_file:
                img_file.write(image_bytes)
    print(f"Images extracted and saved in '{output_folder}'")

def is_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()  # Verify if it's an image
        return True
    except Exception:
        return False

def process_file(file_path):
    output_folder = create_output_folder()
    if file_path.lower().endswith(".pdf"):
        extract_images_from_pdf(file_path, output_folder)
    elif is_image(file_path):
        shutil.copy(file_path, output_folder)
        print(f"Image copied to '{output_folder}'")
    else:
        print("Unsupported file format. Please provide a PDF or an image.")

if __name__ == "__main__":
    file_path = "../../data/pdfs/Sample Medical Claim Form-1.pdf"  # Remove quotes if pasted with them
    process_file(file_path)
