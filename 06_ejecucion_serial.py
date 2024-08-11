from locust import HttpUser, task, constant

class generar_token(HttpUser):
    wait_time = constant(2)
    host = "https://bookstore.demoqa.com"
    token = None

    @task
    def on_start(self):
        self.login()
        self.post_book()
        self.delete_book()


    def login(self):
        response = self.client.post("/account/v1/GenerateToken", json={"userName": "Qa2022","password": "QaPassword@2022"}, name="Generar_token")
        if response.status_code == 200:
            self.token = response.json().get("token")
            print(f"Token exitoso: {self.token}")
        else:
            print(f"Token fallido: {response.status_code}")

            
    def post_book(self):
        headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
        body = {
                "userId": "a2b32031-7777-49d6-a83f-a2e9725b4b6b",
                "collectionOfIsbns": [
                    {
                    "isbn": "9781449325862"
                    }
                ]
                }
        response = self.client.post("/BookStore/v1/Books?UserId=a2b32031-7777-49d6-a83f-a2e9725b4b6b", headers=headers, json=body, name = "Registro Libro")
        if response.status_code == 201:
             print(f"POST Exitoso: {response.status_code} {response.reason}")
        else:
            print(f"POST Fallido: {response.status_code} {response.reason}")

    
    def delete_book(self):
        headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
        body = {
                "userId": "a2b32031-7777-49d6-a83f-a2e9725b4b6b",
                "isbn": "9781449325862"
                }
        response = self.client.delete("/BookStore/v1/Book", headers=headers, json=body, name = "Eliminar Libro")
        if response.status_code == 204:
             print(f"DELETE Exitoso: {response.status_code} {response.reason}")
        else:
            print(f"DELETE Fallido: {response.status_code} {response.reason}")
        print("*************************************************************")

    

