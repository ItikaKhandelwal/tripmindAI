from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    supabase_url: str
    supabase_anon_key: str
    supabase_service_role_key: str
    app_env: str = "development"
    allowed_origins: str = "http://localhost:3000,http://localhost:8081"

    class Config:
        env_file = ".env"

# Single instance used across the app
settings = Settings()