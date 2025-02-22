import os
import uuid
import shutil
from fastapi import UploadFile
import fitz

# Function to save and extract text
def save_and_extract_pdf(directory: str, file: UploadFile):
    try:
        # Define upload path
        base_path = os.getcwd()
        upload_folder = os.path.join(base_path, "uploads", directory)
        os.makedirs(upload_folder, exist_ok=True)  # Ensure directory exists

        # Generate unique filename
        extension = file.filename.split(".")[-1]
        unique_id = str(uuid.uuid4())
        new_name = f"{unique_id}.{extension}"
        file_path = os.path.join(upload_folder, new_name)

        # Save file
        with open(file_path, "wb") as file_object:
            shutil.copyfileobj(file.file, file_object)

        # Extract text from PDF
        text = ""
        with fitz.open(file_path) as pdf_document:
            for page in pdf_document:
                text += page.get_text("text")  # Extract text from each page

        return {"file_path": f"/uploads/{directory}/{new_name}", "text": text}

    except Exception as e:
        return {"error": str(e)}


def delete_uploaded_image(image_path: str):
    try:
        full_path = os.path.join(os.getcwd(), image_path)
        if os.path.exists(full_path):
            os.remove(full_path)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False
