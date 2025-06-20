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

# Create FastAPI app with metadata
app = FastAPI(
    title="FastAPI MCP Email Server",
    description="A simple email server simulation using FastAPI and MCP"
)



class EmailRequest(BaseModel):
    recipients: List[EmailStr]
    html_body: str

class EmailResponse(BaseModel):
    delivered: List[EmailStr]
    bounced: List[EmailStr]

@app.post("/send-emails", response_model=EmailResponse,operation_id="send_emails")
async def send_emails(request: EmailRequest):
    recipients = request.recipients
    html = request.html_body

    if not html.strip():
        raise HTTPException(status_code=400, detail="HTML body cannot be empty")

    # Handle empty recipient list
    if not recipients:
        logger.info("No recipients provided")
        return EmailResponse(delivered=[], bounced=[])

    # Simulate random bounces (e.g., 10–20% of emails)
    # Use min() to ensure we don't try to bounce more emails than we have
    max_bounces = len(recipients) // 5  # 20% bounce rate
    bounce_count = random.randint(0, max(0, max_bounces))
    
    if bounce_count > 0:
        bounced = set(random.sample(recipients, bounce_count))
    else:
        bounced = set()
    
    delivered = [email for email in recipients if email not in bounced]

    # Log the simulation
    logger.info("Simulating sending email.")
    logger.info(f"HTML content:\n{html}")
    logger.info(f"Delivered to: {delivered}")
    logger.info(f"Bounced: {list(bounced)}")

    return EmailResponse(delivered=delivered, bounced=list(bounced))


# Optional: Add this to run the server directly
if __name__ == "__main__":
    mcp = FastApiMCP(app,include_operations=["send_emails"])
    mcp.mount()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)