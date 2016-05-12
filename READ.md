## Synopsis

This project is the backend to provide a REST API to an exchange rates analysis app.

## Getting de code

Go to your workspace folder and run:

```
git clone git@github.com:nandooliveira/exchange-client-test.git
```

## Installing requirements

To install the app's requirements you need to have installed pip tool.

To install all requirements just go to project folder and run:

```
pip install -r requirements.txt
```

## How to execute

To run this app in development environment you just need to execute the runserver.py file:

```
python runserver.py
```

## Endpoints

For while there is only a few endpoints at this API. There is a version of this API deployed on heroku (https://floating-spire-61246.herokuapp.com/api/v1/exchange_rate) to do some tests.

### /api/v1/exchange_rate - Get exchange rates considering passed parameters

We can pass get params to filter by register fields. For example datetime. This filters will use a regex expression, so the passed value don't need to match entire value.

Examples:
```
https://floating-spire-61246.herokuapp.com/api/v1/exchange_rate
```

```
https://floating-spire-61246.herokuapp.com/api/v1/exchange_rate?datetime=2016-05-11
```

### /api/v1/exchange_rate/current - Get current exchange rates

Example:

```
https://floating-spire-61246.herokuapp.com/api/v1/exchange_rate/current
```

### /api/v1/exchange_rate/<string:initial_date>/<string:final_date> - Get exchange rates from a period

Example:

```
https://floating-spire-61246.herokuapp.com/api/v1/exchange_rate/2016-05-03/2016-05-12
```


## Contributors

* [Fernando Oliveira](https://github.com/nandooliveira)

## License

[CC0 1.0 Universal](https://github.com/nandooliveira/exchange-client-test/blob/master/LICENSE)
