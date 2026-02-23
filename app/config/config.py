import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi_mail import ConnectionConfig

class Settings(BaseSettings):
    mail_username: str
    mail_password: str
    mail_from: str
    mail_port: int = 587
    mail_server: str = "smtp.gmail.com"
    
    model_config = SettingsConfigDict(env_file=".env.local", env_file_encoding="utf-8", extra="ignore")

settings = Settings()

email_conf = ConnectionConfig(
    MAIL_USERNAME = settings.mail_username,
    MAIL_PASSWORD = settings.mail_password,
    MAIL_FROM = settings.mail_from,
    MAIL_PORT = settings.mail_port,
    MAIL_SERVER = settings.mail_server,
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)