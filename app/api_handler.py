import requests
import json


class APIHandler:
    def __init__(self, api_url):
        self.api_url = api_url

    def send_summary(self, summary_data):
        """Sends the summary data to the model API."""
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(
                self.api_url, data=json.dumps(summary_data), headers=headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None


# Example usage:
if __name__ == "__main__":
    api_url = "https://example.com/api/summarize"
    api_handler = APIHandler(api_url)

    sample_summary = {
        "project": "Test Project",
        "modules": {
            "module1.py": {
                "functions": {"func1": "This function processes data."},
                "classes": {"Class1": "This class handles user interactions."},
            }
        },
    }

    response = api_handler.send_summary(sample_summary)
    print("API Response:", response)
