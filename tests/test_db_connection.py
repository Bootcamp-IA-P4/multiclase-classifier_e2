import os
import pytest
from supabase import create_client
from dotenv import load_dotenv
load_dotenv()


# Comprobamos que el archivo .env está cargado correctamente y las variables existen.
def test_supabase_env_variables_exist():
    assert os.getenv("SUPABASE_URL") is not None, "SUPABASE_URL no está definida"
    assert os.getenv("SUPABASE_KEY") is not None, "SUPABASE_KEY no está definida"

def test_supabase_connection_valid():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        pytest.skip("Variables de entorno no definidas")

    client = create_client(url, key)
    response = client.table("diabetes_predictions").select("*").limit(1).execute()

    assert response.status_code == 200 or response.data is not None
