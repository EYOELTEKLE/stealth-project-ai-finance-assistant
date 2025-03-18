import os
from pydantic import BaseModel
from fastapi_mail import ConnectionConfig
from dotenv import load_dotenv
from pathlib import Path
# Load environment variables
load_dotenv()

# Debug: Check if environment variables are being read
print("MAIL_USERNAME:", os.getenv("email-username"))

script_dir = Path(__file__).parent

# Construct the correct path to the templates folder
template_folder = script_dir / "templates" / "email"
class EmailSettings(BaseModel):
    MAIL_USERNAME: str = os.getenv("MAIL_USERNAME")
    MAIL_FROM_NAME: str = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD: str = os.getenv("MAIL_PASSWORD")
    MAIL_FROM: str = os.getenv("MAIL_FROM")
    MAIL_SERVER: str = os.getenv("MAIL_HOST")
    MAIL_PORT: int = 465
    MAIL_TLS: bool = True
    MAIL_SSL: bool = True
    MAIL_STARTTLS: bool = False
    MAIL_SSL_TLS:bool = True
    TEMPLATE_FOLDER:Path = template_folder

mail_config = EmailSettings()


if not all([mail_config.MAIL_USERNAME, mail_config.MAIL_PASSWORD, mail_config.MAIL_FROM]):
    raise ValueError("Missing required email configuration in environment variables.")

# Configure FastAPI Mail
conf = ConnectionConfig(
    MAIL_USERNAME=mail_config.MAIL_USERNAME,
    MAIL_PASSWORD=mail_config.MAIL_PASSWORD,
    MAIL_FROM=mail_config.MAIL_FROM,
    MAIL_PORT=mail_config.MAIL_PORT,
    MAIL_SERVER=mail_config.MAIL_SERVER,
    MAIL_STARTTLS=mail_config.MAIL_STARTTLS,
    MAIL_SSL_TLS=mail_config.MAIL_SSL_TLS,
    TEMPLATE_FOLDER=mail_config.TEMPLATE_FOLDER
)

