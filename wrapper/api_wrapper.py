from requests_oauthlib import OAuth1
import requests
import pandas as pd


class PublicApi:
    """ A class for storing the public APIs data including base urls and endpoints. """
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
        """ Initialize the APIWrapper with the API URL and Authorizations. """
        self.api_url = api_url
        self.username = username
        self.password = password
        self.api_key = api_key
        self.secret_key = secret_key
        self.token = token
        self.auth = None

    def create_auth(self):
        """
        Create an authorization header.
        Returns: The authorization header composed of either username, password or api_key, secret_key, token
        """
        if self.username and self.password:
            self.auth = (self.username, self.password)
        elif self.api_key and self.secret_key and self.token:
            self.auth = OAuth1(self.api_key, self.secret_key, self.token)
        elif self.token:
            self.auth = {'Authorization': 'Bearer {}'.format(self.token)}
        elif self.secret_key:
            self.auth = {'Authorization': 'Bearer {}'.format(self.secret_key)}
        elif self.api_key:
            self.auth = {'Authorization': 'Bearer {}'.format(self.api_key)}
        else:
            self.auth = None
        return self.auth

    def __format__(self, response):
        """
        Formats API request response into a json object
        Params: Restful API response
        Return: json object.
        """
        return response.json()

    def get_data(self):
        """
        Makes a get request to the API and returns a json object.
        Returns: Json object
        """
        return self.__format__(requests.get(self.api_url, self.auth))

    def generate_df(self, json_data):
        """
        Generates a dataframe from a json object using Pandas normalize function
        (Normalize semi-structured JSON data into a flat table) https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.json_normalize.html.
        Params: Json object
        Returns: A dataframe from a simple json object.
        """
        return pd.json_normalize(json_data, max_level=5)








