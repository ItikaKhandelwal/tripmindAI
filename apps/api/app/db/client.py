from supabase import create_client, Client
from app.config import settings

def get_supabase() -> Client:
    """Returns a Supabase client using the anon key."""
    return create_client(
        settings.supabase_url,
        settings.supabase_anon_key
    )

def get_supabase_admin() -> Client:
    """Returns a Supabase client using the service role key.
    Use this only for admin operations (bypasses RLS).
    """
    return create_client(
        settings.supabase_url,
        settings.supabase_service_role_key
    )