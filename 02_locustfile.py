from locust import HttpUser, task, between

class demoQA(HttpUser):
    wait_time = between(1, 3)
    host = "https://demoqa.com"

    @task
    def home(self):
        self.client.get("/")
    
    @task
    def libros(self):
        self.client.get("/books")