# app/api/routes/file_routes.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from app.application.file_service import FileService


router = APIRouter()
file_service = FileService()

@router.post("/upload-invoice")
async def upload_file(file: UploadFile = File(...)):
    print(f"Received file: {file.filename}, size: {file.size} bytes")
    file_bytes = await file.read()
    print(f"File content size: {len(file_bytes)} bytes")
    print(f"First 10 bytes: {file_bytes[:10]}")

    # Reset the file pointer (important for future reads)
    await file.seek(0)
    file_metadata = file_service.upload_file(file)

    #trigger google cloud
    return {"message": "File uploaded successfully", "file": file_metadata}



