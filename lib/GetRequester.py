import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def load_json(self):
        response = requests.get(self.url)
        return response.json()
        
    
    # def load_json(self):
    #     response = self.get_response_body()
    #     if response is not None:
    #         try:
    #             return response.json()
    #         except json.JSONDecodeError:
    #             print("Error decoding JSON")
    #             return None
            
    #     return None