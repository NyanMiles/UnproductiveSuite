import requests
from datetime import datetime, timezone

API_BASE_URL = "https://api.todoist.com"  # Cambia esto por la URL de tu API
API_KEY = "a0a95db84d3fdf7354127fd4cadfeed66003a4aa"  # Si tu API requiere autenticación


def get_iso_datetime(now=True):
    """
    Devuelve un string en formato ISO 8601 (<date-time>)
    Si now=True devuelve la fecha actual UTC
    """
    if now:
        return datetime.now(timezone.utc).isoformat()
    return None


def make_get_request(endpoint, params=None, headers=None):
    """
    Hace un GET request a la API y devuelve el JSON.
    """
    url = f"{API_BASE_URL}{endpoint}"
    if headers is None:
        headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


def make_post_request(endpoint, data=None, headers=None):
    """
    Hace un POST request a la API y devuelve el JSON.
    """
    url = f"{API_BASE_URL}{endpoint}"
    if headers is None:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code in [200, 201]:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


def obtener_datos_ejemplo():
    endpoint = "/api/v1/tasks"
    params = {
        "project_id": "6cXWqr73Hm8PvrW9"
    }
    return make_get_request(endpoint, params=params)


def enviar_datos_ejemplo(valor):
    endpoint = "/guardar"
    data = {
        "valor": valor,
        "timestamp": get_iso_datetime()
    }
    return make_post_request(endpoint, data=data)


# ==========================
# MAIN / PRUEBAS
# ==========================
if __name__ == "__main__":
    resultado = obtener_datos_ejemplo()
    print("GET resultado:", resultado)

    respuesta_post = enviar_datos_ejemplo(12345)
    print("POST resultado:", respuesta_post)