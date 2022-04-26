from api_wrapper import *

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
