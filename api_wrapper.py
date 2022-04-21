from requests_oauthlib import OAuth1
import requests
import pandas as pd


class PublicApi:
    """
    A class for storing the public APIs data including base urls and endpoints
    """
    def __init__(self, base_url, endpoint=None):
        """ Initialize the Public Api with a base URL and endpoint. """
        self.base_url = base_url
        self.endpoint = endpoint

    def get_base_url(self):
        """ Get the base url of the PublicAPI. """
        return self.base_url
    
    def set_base_url(self, url):
        """ Set the PublicAPI's base url. """
        self.base_url = url

    def get_endpoint(self):
        """ Get the endpoint of the PublicAPI. """
        return self.endpoint

    def set_endpoint(self, endpoint):
        """ Set the PublicAPI's endpoint. """
        self.endpoint = endpoint

    def api_url(self):
        """ Returns the PublicAPI's url to be used for the request formatted accordingly. """
        if self.endpoint is None:
            return self.base_url
        else:
            return self.base_url + self.endpoint


class ApiWrapper:
    """ Class  for wrapping the API and generating a data frame. """
    def __init__(self, api_url, username=None, password=None, api_key=None, secret_key=None, token=None):
        """ Initialize the APIWrapper with an API URL. """
        self.api_url = api_url
        self.username = username
        self.password = password
        self.api_key = api_key
        self.secret_key = secret_key
        self.token = token
        self.auth = None

    def __create_auth(self):
        if self.username and self.password:
            self.auth = (self.username, self.password)
        elif self.api_key and self.secret_key and self.token:
            self.auth = OAuth1(self.api_key, self.secret_key, self.token)
        else:
            self.auth = None

    def __format__(self, response):
        """ Returns a json response. """
        return response.json()

    def get_data(self):
        """ Makes a get request to the API and returns a json response. """
        return self.__format__(requests.get(self.api_url, self.auth))

    def generate_df(self, json_data):
        """ Returns a dataframe from a simple json. """
        return pd.json_normalize(json_data)


# Example Usage
if __name__ == '__main__':
    api = PublicApi("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all")
    wrap_api = ApiWrapper(api.api_url())
    data = wrap_api.get_data()
    df = wrap_api.generate_df(data)
    print(df)
    print("\n")
    covid_api = PublicApi("https://covid-api.mmediagroup.fr/v1/", "vaccines")
    wrap_covid_api = ApiWrapper(covid_api.api_url())
    covid_df = wrap_covid_api.generate_df(wrap_covid_api.get_data())
    print(covid_df)


