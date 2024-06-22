from locust import HttpUser, task, between

class MiUsuario(HttpUser):
    wait_time = between(1, 3)
    host = "https://www.python.org"

    @task
    def mi_tarea(self):
        self.client.get("/")