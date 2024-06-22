from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)
    host = "https://reqres.in"

    @task
    def get_example(self):
        response = self.client.get("/api/users/2") 
        print(f"Response body: {response.text}")
        # print(f"Response json: {response.json()}")          
        # print(f"Headers: {response.headers}")
        # print(f"Tiempo de respuesta: {response.elapsed.total_seconds() * 1000} ms")
        # print(f"URL de la solicitud: {response.request.url}")
        # print(f"Método HTTP: {response.request.method}")
        # print(f"Código de estado: {response.status_code}")
        # print(f"Razón del estado: {response.reason}")
        # print(f"Código de estado: {response.status_code} {response.reason}")
        # print(f"Cookies: {response.cookies}")
        # print(f"Redirecciones: {response.history}")
        # print(f"Codificación de la respuesta: {response.encoding}")
        # print(f"Tamaño del contenido: {len(response.content)} bytes")
        # print(f"Versión del protocolo: {response.raw.version}")
        # print(f"Cabeceras de la solicitud: {response.request.headers}")

        # total_time = response.elapsed.total_seconds()
        # print(f"Tiempo total de ejecución: {total_time * 1000} ms")
