from api_wrapper import *

# Example Usage
if __name__ == '__main__':
    api = PublicApi("https://api.tvmaze.com/search/shows?q=girls")
    wrap_api = ApiWrapper(api.api_url())
    data = wrap_api.get_data()
    df = wrap_api.generate_df(data)
    print(df)
    print("\n")
    covid_api = PublicApi("https://covid-api.mmediagroup.fr/v1/", "vaccines")
    wrap_covid_api = ApiWrapper(covid_api.api_url())
    covid_df = wrap_covid_api.generate_df(wrap_covid_api.get_data())
    print(covid_df)
