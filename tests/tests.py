from wrapper.api_wrapper import PublicApi, ApiWrapper
import unittest
import vcr


class TestPublicApi(unittest.TestCase):
    def setUp(self):  # runs before every single test
        self.api_dog_facts = PublicApi("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all")
        self.api_covid_19 = PublicApi("https://covid-api.mmediagroup.fr/v1/", "vaccines")

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
    def setUp(self):  # runs before every single test
        self.api_key = "DummyToken"
        self.api_url = "https://api.thedogapi.com/v1/images/search"

    @vcr.use_cassette('fixtures/cassettes/test_create_auth.yaml')
    def test_create_auth(self):
        self.wrap_api = ApiWrapper(api_url=self.api_url, api_key=self.api_key)
        self.wrap_api.create_auth()
        self.assertEqual(self.wrap_api.auth, {'Authorization': 'Bearer DummyToken'})

    @vcr.use_cassette('fixtures/cassettes/test_get_data.yaml')
    def test_get_data(self):
        self.wrap_api = ApiWrapper(api_url=self.api_url, api_key=self.api_key)
        json_data = self.wrap_api.get_data()
        self.assertEqual(json_data[0]['breeds'][0]['name'], 'Alaskan Husky')

    @vcr.use_cassette('fixtures/cassettes/test_generate_df.yaml')
    def test_generate_df(self):
        wrap_api = ApiWrapper(api_url=self.api_url, api_key=self.api_key)
        json_data = wrap_api.get_data()
        df = wrap_api.generate_df(json_data)
        self.assertEqual(len(df), 1)


