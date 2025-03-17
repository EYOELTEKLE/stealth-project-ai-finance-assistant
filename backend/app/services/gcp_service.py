# app/service/gcp_service.py
import json

import requests
from fastapi import UploadFile
from io import BytesIO
from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException
import logging
import base64
# Configure logging
logging.basicConfig(level=logging.ERROR)
load_dotenv()

# Read the GCF_URL from the environment
GCF_URL = os.getenv("GCF_URL")


class GCPService:
    @staticmethod
    def send_invoice_to_gcp(file: UploadFile):
        """Send the uploaded invoice image to Google Cloud Function"""
        try:
            file_bytes = file.file.read()

            print(f"File size: {len(file_bytes)} bytes")
            print(f"First 10 bytes: {file_bytes[:10]}")

            # Encode the file data as base64
            file_data_base64 = base64.b64encode(file_bytes).decode("utf-8")

            # Prepare the request payload
            payload = {
                "file": file_data_base64,  # Base64-encoded file data
                "filename": file.filename,  # Optional: Include filename
                "filetype": file.content_type,  # Optional: Include file type
            }

            # Send the file to the GCF
            print(payload)
            response = requests.post(
                GCF_URL,
                json=payload,  # Send as JSON in the body
                headers={"Content-Type": "application/json"},
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(response.text, response.content)  # Log for debugging
                error_message = f"Error sending file to GCP. Status: {response.status_code}, Response: {response.text}"
                print(response.text,response.content)  # Log for debugging
                logging.error(response.text or response.content)
                raise HTTPException(
                    status_code=500,
                    detail=error_message
                )

        except Exception as e:
            logging.error(e)
            error_message = f"Exception occurred: {str(e)}"
            print(e)  # Log for debugging
            raise HTTPException(status_code=500, detail=error_message)