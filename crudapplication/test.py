from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 5)  # Simulate users waiting between 1 and 5 seconds between tasks

    @task
    def test_get_endpoint(self):
        response = self.client.get("/api/employees/all")  # Replace with your API's GET endpoint
        if response.status_code == 200:
            print(f"Success: {response.status_code}")
        else:
            print(f"Failure: {response.status_code}")

    # @task
    # def test_post_endpoint(self):
    #     payload = {"key": "value"}  # Replace with your POST data
    #     response = self.client.post("/api/v1/example", json=payload)  # Replace with your API's POST endpoint
    #     if response.status_code == 201:
    #         print(f"POST Success: {response.status_code}")
    #     else:
    #         print(f"POST Failure: {response.status_code}")

# Command to run locust: locust -f <filename>.py
