# app/application/file_service.py
from fastapi import UploadFile
from app.domain.model import FileMetadata
from app.infrastructure.file_repository import FileRepository
from app.services.gcp_service import GCPService
class FileService:
    def __init__(self):
        self.repository = FileRepository()

    def upload_file(self, file: UploadFile):
       # file_metadata = self.repository.save_file(file)
        # Trigger Google Cloud Function API call
        processing_result = GCPService.send_invoice_to_gcp(file)

        return {"processing_result": processing_result}


    def get_file(self, filename: str):
        return self.repository.get_file(filename)
