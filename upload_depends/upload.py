import os
import uuid
import shutil
from fastapi import UploadFile

def upload_image(directory: str, file: UploadFile):
    try:
        # Construct upload folder path
        base_path = os.getcwd()
        upload_folder = os.path.join(base_path, "uploads", directory)

        # Ensure the directory exists
        os.makedirs(upload_folder, exist_ok=True)
        print(f"Upload folder created at: {upload_folder}")

        # Create unique filename
        extension = file.filename.split(".")[-1]
        unique_id = str(uuid.uuid4())
        new_name = f"{unique_id}.{extension}"

        # Save the file
        file_path = os.path.join(upload_folder, new_name)
        with open(file_path, "wb") as file_object:
            shutil.copyfileobj(file.file, file_object)

        # Return relative path for database storage
        return f"/uploads/{directory}/{new_name}"
    except Exception as e:
        print(f"Error during file upload: {e}")
        return False
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
