from fastapi import FastAPI

from backend.app.api.router import api_router
from backend.app.core.lifespan import lifespan
from backend.app.utils.exception_handler import (
    register_exception_handlers,
)
from backend.app.middleware.request_id import RequestIDMiddleware
from backend.app.middleware.logging import LoggingMiddleware

from backend.app.core.config import settings

app = FastAPI(
    title="SecureGen AI Intrusion Detection API",
    description="Explainable AI-powered Network Intrusion Detection System",
    version="1.0.0",
    lifespan=lifespan,
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RequestIDMiddleware)
app.add_middleware(LoggingMiddleware)

app.include_router(api_router)

register_exception_handlers(app)

@app.get("/")
def root():

    return {

        "application": "SecureGen",

        "version": settings.API_VERSION,

        "status": "Running",

    }