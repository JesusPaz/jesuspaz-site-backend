from fastapi import FastAPI
from app.api.endpoints import compound_interest

app = FastAPI()

# Middleware, CORS, and other settings (if needed) would go here.

# Route inclusion
app.include_router(compound_interest.router)

# Code to run the application (if desired)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
