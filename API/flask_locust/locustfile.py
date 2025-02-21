from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:5000"  # Change this to your target website
    wait_time = between(1, 3)  # Simulated users wait between 1 and 3 seconds between tasks

    @task
    def load_homepage(self):
        self.client.get("/")  # Simulates a GET request to the homepage

    @task
    def load_about_page(self):
        self.client.get("/about")  # Simulates a GET request to the About page

    @task
    def submit_form(self):
        random_email = f"user{random.randint(1000, 9999)}@example.com"
        self.client.post("/submit", data={"name": "Test User", "email": random_email})  # Simulates a form submission
