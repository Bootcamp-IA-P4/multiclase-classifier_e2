import os
import pytest
from supabase import create_client
from dotenv import load_dotenv
# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

# Primer test: comprobar que las variables necesarias están definidas
def test_supabase_env_variables_exist():
    assert os.getenv("SUPABASE_URL") is not None, "SUPABASE_URL no está definida"
    assert os.getenv("SUPABASE_KEY") is not None, "SUPABASE_KEY no está definida"

# Segundo test: probar conexión real a Supabase y verificar respuesta
def test_supabase_connection_valid():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

# Si no están definidas, saltamos el test (útil para evitar errores en entornos sin .env)
    if not url or not key:
        pytest.skip("Variables de entorno no definidas")

    client = create_client(url, key)
    try:
        # Ejecutamos una consulta simple a la tabla 'diabetes_predictions'
        response = client.table("diabetes_predictions").select("*").limit(1).execute()
        # Verificamos que el resultado es una lista (aunque vacía)
        assert isinstance(response.data, list)  # si no lanza error, todo va bien
    except Exception as e:
        # Si ocurre un error al ejecutar la consulta, fallamos el test
        pytest.fail(f"No se pudo conectar correctamente a Supabase: {e}")