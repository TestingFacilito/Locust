from locust import HttpUser, task, constant

class generar_token(HttpUser):
    wait_time = constant(3)
    host = "https://bookstore.demoqa.com"
    token = ""

    def on_start(self):
        self.token()

    @task
    def token(self):
        response = self.client.post("/account/v1/GenerateToken", json={"userName": "Qa2022","password": "QaPassword@2022"}, name="Generar_token")
        if response.status_code == 200:
            self.token = response.json().get("token")
            print(f"Token exitoso: {self.token}")
        else:
            print(f"Token fallido: {response.status_code}")
            