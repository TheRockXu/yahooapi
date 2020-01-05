# Inroduction

This is a simple API that pulls yahoo finance company price history page, parse it and return and panda dataframe

## Requirements
> `python-3.7`\
> `pandas-0.25`

> Install with pip ` pip install -e git://github.com/TheRockXu/yahooapi.git#egg=yahooapi`

The yahoo finance html syntax will change. So, this api might now work consistently.

## Usage

`get_pricing(["AAPL", "IBM"], start_date ="2006-1-1", end_date="2018-1-1")`
