from locust import HttpUser, TaskSet, task, between, LoadTestShape, constant

class UserTaks(TaskSet):
    @task
    def get_simple(self):
        response = self.client.get("/api/users/2")
        if response.status_code == 200:
            print(f"GET Exito: {response.status_code}")
        else:
            print(f"GET Fallo: {response.status_code}")


class User(HttpUser):
    wait_time = constant(0.5)
    tasks = [UserTaks]
    host = "https://reqres.in"

class CustomShape(LoadTestShape):
        stages = [
            {"duration": 15, "users": 10, "spawn_rate": 10},
            {"duration": 45, "users": 50, "spawn_rate": 10},
            {"duration": 75, "users": 100, "spawn_rate": 10},
            {"duration": 90, "users": 30, "spawn_rate": 10},
            {"duration": 105, "users": 10, "spawn_rate": 10},
            {"duration": 120, "users": 1, "spawn_rate": 1},
        ]

        def tick(self):
            run_time = self.get_run_time()
            for stage in self.stages:
                if run_time < stage["duration"]:
                    return (stage["users"], stage["spawn_rate"])
                run_time -= stage["duration"]
            return None

