import os


class Config:
    # General Config
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    DEBUG = os.getenv('DEBUG', False)

    # API Config
    API_V1_STR = "/api/v1"
    PROJECT_NAME = "Jesus Paz's Backend"
    ALLOWED_HOSTS = ["localhost", "jesuspaz.com"]

    # CORS Configuration (si quieres permitir CORS)
    ORIGINS = [
        "http://localhost:8000",
        "http://localhost:3000",
        "https://localhost:8000",
        "http://localhost",
        "http://jesuspaz.com",
        "https://jesuspaz.com",
    ]
