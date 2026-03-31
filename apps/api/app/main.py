from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.config import settings
from app.routers import health, trips, expenses

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs on startup
    print(f"TripMind API starting in {settings.app_env} mode")
    yield
    # Runs on shutdown
    print("TripMind API shutting down")

app = FastAPI(
    title="TripMind API",
    description="Backend API for TripMind travel expense tracker",
    version="1.0.0",
    docs_url="/docs" if settings.app_env != "production" else None,
    redoc_url="/redoc" if settings.app_env != "production" else None,
    lifespan=lifespan
)

# CORS
origins = settings.allowed_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, tags=["health"])
app.include_router(trips.router)
app.include_router(expenses.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to TripMind API",
        "version": "1.0.0",
        "environment": settings.app_env
    }