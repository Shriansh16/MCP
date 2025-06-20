import os
import logging
from fastapi import FastAPI, HTTPException
from fastapi_mcp import FastApiMCP
from pydantic import BaseModel, EmailStr
from typing import List
import random

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure logger
logging.basicConfig(
    filename="logs/email_logs.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

app = FastAPI()
mcp = FastApiMCP(app,
            name="FastAPI MCP Email Server",
            description="A simple email server simulation using FastAPI and MCP")
mcp.mount()

class EmailRequest(BaseModel):
    recipients: List[EmailStr]
    html_body: str

class EmailResponse(BaseModel):
    delivered: List[EmailStr]
    bounced: List[EmailStr]

@app.post("/send-emails", response_model=EmailResponse)
async def send_emails(request: EmailRequest):
    recipients = request.recipients
    html = request.html_body

    if not html.strip():
        raise HTTPException(status_code=400, detail="HTML body cannot be empty")

    # Simulate random bounces (e.g., 10–20% of emails)
    bounce_count = random.randint(1, max(1, len(recipients) // 5))
    bounced = set(random.sample(recipients, bounce_count))
    delivered = [email for email in recipients if email not in bounced]

    # Log the simulation
    logger.info("Simulating sending email.")
    logger.info(f"HTML content:\n{html}")
    logger.info(f"Delivered to: {delivered}")
    logger.info(f"Bounced: {list(bounced)}")

    return EmailResponse(delivered=delivered, bounced=list(bounced))

mcp.setup_server()
