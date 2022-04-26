# API-Wrapper

## Purpose
The purpose of this package is to simplify development of packages that use certain Public APIs. 
The package wraps specific Public Restful APIs and generates a dataframe that can then be used in external packages for data analysis.

## Goals

* Develop a package that is designed specifically for Python to access Public APIs (Matheus 2022), taking advantage of Python's unique language features and working smoothly with Python's data types.

* The API wrapper will encapsulate multiple API calls and simplify the process of interacting with Web APIs by running functions for accessing the data.

* Document the API purely in Python terms, convert the JSON data into data frame, so that the programmer does not need to read the documentation, and translate into Python.
 
## Features
* Getting and setting Public Restful APIs information( base-url and endpoints)
* Wrapping the Public Restful APIs and returns a json response
* Support for Restful APIs with authentication keys or tokens
* Generating a pandas dataframe 

## Usage 
Below is an example of how to use the package after installing and importing it in your package. 

Simple Restful APIs:- 
* Dog Facts API: https://dukengn.github.io/Dog-facts-API/
```
    api = PublicApi("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all")
    wrap_api = ApiWrapper(api.api_url())
    data = wrap_api.get_data()
    df = wrap_api.generate_df(data)
    print(df)
```

* COVID-19 API 
```
    covid_api = PublicApi("https://covid-api.mmediagroup.fr/v1/", "vaccines")
    wrap_covid_api = ApiWrapper(covid_api.api_url())
    covid_df = wrap_covid_api.generate_df(wrap_covid_api.get_data())
    print(covid_df)
```

## Future / Upcoming Work
* Generation of dataframes from complex Json responses that include multiple nested layers.
* Uploading the package on PYPI

## Contribute
To contribute to the development of our package, fork the main repo https://github.com/yixuan-feng/API-Wrapper/fork and send a 
pull request of any added functionalities or enhancements for our team to review and merge accordingly. 
