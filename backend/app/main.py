from fastapi import FastAPI
from app.api.routes.upload_invoice import router as file_router
from fastapi.middleware.cors import CORSMiddleware
import os

from dotenv import load_dotenv
load_dotenv()

print(os.getenv("GCF_URL"))
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500","http://127.0.0.1:5500"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
# Include File Routes
app.include_router(file_router, prefix="/api/files", tags=["files"])

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI with in-memory file storage!"}