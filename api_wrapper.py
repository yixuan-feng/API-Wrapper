import requests
import pandas as pd


class PublicApi:
    def __init__(self, base_url, endpoint=None):
        self.base_url = base_url
        self.endpoint = endpoint

    def get_base_url(self):
        return self.base_url
    
    def set_base_url(self, url):
        self.base_url = url

    def get_endpoint(self):
        return self.endpoint

    def set_endpoint(self, endpoint):
        self.endpoint = endpoint

    def api_url(self):
        if self.endpoint is None:
            return self.base_url
        else:
            return self.base_url + self.endpoint


class ApiWrapper:
    def __init__(self, api_url):
        self.api_url = api_url

    def __format__(self, response):
        return response.json()

    def get_data(self):
        return self.__format__(requests.get(self.api_url))

    def generate_df(self, json_data):
        return pd.json_normalize(json_data)


if __name__ == '__main__': 
    #covid_api = PublicApi("https://covid-api.mmediagroup.fr/v1/", "vaccines")
    api = PublicApi("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all")
    print(api.api_url())
    wrapped_api = ApiWrapper(api.api_url())
    data = wrapped_api.get_data()
    df = wrapped_api.generate_df(data)
    print(df)

