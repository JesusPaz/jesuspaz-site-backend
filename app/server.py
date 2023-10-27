from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import Config
from app.api import api

app = FastAPI(
    title=Config.PROJECT_NAME,
    openapi_url=f"{Config.API_V1_STR}/openapi.json",
)

# Including CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Including the main router that encompasses all endpoints
app.include_router(api.router)

# Including the router for the docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
