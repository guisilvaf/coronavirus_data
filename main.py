import requests
import json

API_KEY = "t4X-z_dkhzJ-"
PROJECT_TOKEN = "tt6E2QT3bNuU"
RUN_TOKEN = "t_sWJ9oGLvry"


class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data',
            params=self.params)
        self.data = json.loads(response.text)

    def get_total_cases(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Coronavirus Cases:":
                return content['value']

    def get_total_deaths(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Deaths:":
                return content['value']

    def get_country_data(self, country):
        data = self.data['country']

        for content in data:
            if content['name'].lower() == country.lower():
                return content

    def get_recovery_data(self):
        data = self.data['total']

        for content in data:
            if content['name'] == "Recovered:":
                return content['value']


data = Data(API_KEY, PROJECT_TOKEN)