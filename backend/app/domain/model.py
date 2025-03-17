from pydantic import BaseModel

class FileMetadata(BaseModel):
    filename: str
    size: int
    content_type: str