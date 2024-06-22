from locust import HttpUser, task, between

class crud(HttpUser):
    wait_time = between(1, 3)
    host = "https://reqres.in"

    @task
    def get_single_user(self):
        response = self.client.get("/api/users/2")
        if response.status_code == 200:
            print(f"GET Exitoso: {response.status_code}")
        else:
            print(f"GET Fallido: {response.status_code}")

    @task
    def post_create_user(self):
        header = {"Content-Type":"application/json"}
        body = {
                "name": "morpheus",
                "job": "leader"
        }
        response = self.client.post("/api/users", headers=header, json=body, name = "Crear usuarios post")
        if response.status_code == 201:
            print(f"POST Exitoso: {response.status_code}")
        else:
            print(f"POST Fallido: {response.status_code}")
        
    
    @task
    def put_update_user(self):
        header = {"Content-Type":"application/json"}
        body = {
                "name": "Jorge Miguel",
                "job": "QA Tester"
        }
        response = self.client.put("/api/users/5", headers=header, json=body)
        if response.status_code == 200:
            print(f"PUT Exitoso: {response.status_code}")
        else:
            print(f"PUT Fallido: {response.status_code}")


    @task
    def delete_user(self):
        response = self.client.delete("/api/users/5", name = "DELETE USER")
        if response.status_code == 204:
            print(f"DELETE Exitoso: {response.status_code}")
        else:
            print(f"DELETE Fallido: {response.status_code}")
