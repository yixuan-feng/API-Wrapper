import unittest
import api_wrapper


class TestPublicApi(unittest.TestCase):
    def test_get_base_url(self):
        api = api_wrapper.PublicApi("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all")
        self.assertEqual(api.get_base_url(), "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all")

    def test_get_endpoint(self):
        api = api_wrapper.PublicApi("https://covid-api.mmediagroup.fr/v1/", "vaccines")
        self.assertEqual(api.get_endpoint(), "vaccines")

    def test_set_base_url(self):
        api = api_wrapper.PublicApi("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all")
        api.set_base_url("https://covid-api.mmediagroup.fr/v1/")
        self.assertEqual(api.get_base_url(), "https://covid-api.mmediagroup.fr/v1/")

    def test_set_endpoint(self):
        api = api_wrapper.PublicApi("https://covid-api.mmediagroup.fr/v1/")
        api.set_endpoint("vaccines")
        self.assertEqual(api.get_endpoint(), "vaccines")

    def test_api_url(self):
        api = api_wrapper.PublicApi("https://covid-api.mmediagroup.fr/v1/")
        api.set_endpoint("vaccines")
        self.assertEqual(api.api_url(), "https://covid-api.mmediagroup.fr/v1/vaccines")
