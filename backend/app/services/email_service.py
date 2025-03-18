from fastapi_mail import FastMail, MessageSchema
from app.config.email_config import conf


async def send_insight_email(email: str, subject: str, body: str):
    """Send investment insights via email."""
    message = MessageSchema(
        subject=subject,
        recipients=[email],
        body=body,
        subtype="html"
    )

    mail = FastMail(conf)
    await mail.send_message(message)
