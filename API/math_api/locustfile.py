from locust import HttpUser, task, between, random

AUTH_HEADER = {"Authorization": "Bearer supersecrettoken"}

class MathApiUser(HttpUser):
    wait_time = between(1, 3)  # Simulate real user delays

    @task(3)    # decorator for frequency, task will be executed 3 times more frequently than tasks with @task(1).
    def test_addition(self):
        a, b = random.randint(1, 100), random.randint(1, 100)
        self.client.post("/calculate", json={"operation": "add", "a": a, "b": b}, headers=AUTH_HEADER)

    @task(2)
    def test_subtraction(self):
        a, b = random.randint(1, 100), random.randint(1, 100)
        self.client.post("/calculate", json={"operation": "subtract", "a": a, "b": b}, headers=AUTH_HEADER)

    @task(1)
    def test_division(self):
        a = random.randint(1, 100)
        b = random.randint(1, 10)  # Avoid division by zero
        self.client.post("/calculate", json={"operation": "divide", "a": a, "b": b}, headers=AUTH_HEADER)