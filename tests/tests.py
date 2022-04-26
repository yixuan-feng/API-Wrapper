import unittest
from wrapper.api_wrapper import PublicApi, ApiWrapper


class TestPublicApi(unittest.TestCase):
    def setUp(self):  # runs before every single test
        self.api_dog_facts = PublicApi("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all")
        self.api_covid_19 = PublicApi("https://covid-api.mmediagroup.fr/v1/", "vaccines")

    def tearDown(self):  # runs after every single test
        pass

    def test_get_base_url(self):
        self.assertEqual(self.api_dog_facts.get_base_url(),
                         "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all")

    def test_get_endpoint(self):
        self.assertEqual(self.api_covid_19.get_endpoint(), "vaccines")

    def test_set_base_url(self):
        self.api_dog_facts.set_base_url("https://covid-api.mmediagroup.fr/v1/")
        self.assertEqual(self.api_dog_facts.get_base_url(), "https://covid-api.mmediagroup.fr/v1/")

    def test_set_endpoint(self):
        self.api_covid_19.set_endpoint("cases")
        self.assertEqual(self.api_covid_19.get_endpoint(), "cases")

    def test_api_url(self):
        self.assertEqual(self.api_covid_19.api_url(), "https://covid-api.mmediagroup.fr/v1/vaccines")


class TestApiWrapper(unittest.TestCase):
    pass
