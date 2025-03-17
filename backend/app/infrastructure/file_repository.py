# app/infrastructure/file_repository.py
from fastapi import UploadFile
from app.domain.model import FileMetadata
from io import BytesIO

class FileRepository:
    def __init__(self):
        self.file_store = {}  # In-memory storage

    def save_file(self, file: UploadFile) -> FileMetadata:
        file_bytes = BytesIO(file.file.read())  # Store file in buffer
        self.file_store[file.filename] = {
            "content": file_bytes,
            "content_type": file.content_type,
        }

        return FileMetadata(
            filename=file.filename,
            size=len(file_bytes.getvalue()),
            content_type=file.content_type,
        )

    def get_file(self, filename: str):
        return self.file_store.get(filename, None)
