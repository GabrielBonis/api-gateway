import httpx
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType
from pydantic import EmailStr, BaseModel
from typing import List
from app.config.config import email_conf

app = FastAPI(
    title="Api Gateway - Gbonis",
    version="1.0.0",
)

client = httpx.AsyncClient()

astro = "https://astro.gbonis.com.br"

class EmailSchema(BaseModel):
    email: List[EmailStr]
    subject: str
    body: str

@app.post("/send-email")
async def send_email(email: EmailSchema, background_tasks: BackgroundTasks):
    message = MessageSchema(
        subject=email.subject,
        recipients=email.email,
        body=email.body,
        subtype=MessageType.html
    )

    fm = FastMail(email_conf)
    background_tasks.add_task(fm.send_message, message)
    
    return {"status": "enviando", "to": email.email}

@app.on_event("shutdown")
async def shutdown_event():
    await client.aclose()

@app.get("/")
async def home(): 
    return {
        "Services": {
            "astro": astro
        }
    }
    
@app.get("/astro")
def get_astro():
    return {
        "teste": "testando"
    }
