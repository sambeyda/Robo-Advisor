# "Robo Adivsor" Project

[Original product description](https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/projects/robo-advisor.md)

This application issues requests to the [AlphaVantage Stock Market API](https://alphavantage.co/) in order to provide automated stock trading recommendations.

##Monitor Badge Status

[![Build Status](https://travis-ci.com/sambeyda/Robo-Advisor.svg?branch=revisited-testing)](https://travis-ci.com/sambeyda/Robo-Advisor)

## Prerequisities

    + Anaconda 3.7
    + Python 3.7
    + Pip

## Installation

Clone or download [this repository](https://github.com/sambeyda/Robo-Advisor) onto your computer
Then navigate to there from the command line:

```
cd Robo-Advisor-Master
```

Perhaps in a virtual environment, install required package dependencies
```
pip install -r requirements.txt
```
These depedencies are:
pip install requests, csv, os, json, python-dotenv, datetime,statistics


## Setup

Before using or developing this application, take a moment to [obtain an AlphaVantage API Key](https://www.alphavantage.co/support/#api-key) (e.g. "abc123").

After obtaining an API Key, create a new file in this repository called ".env", and update the contents of the ".env" file to specify your real API Key:

    API_KEY="abc123"

## USAGE

Run the robo_advisor tool script to find your stock recommendation

```
python app/robo_advisor.py
```

From here you will be prompted to enter the stock symbol over your choice, and subsequently be presented with your specific stock's necessary metrics, as well as a unique recommendation.

##TESTING

To test, install the `pytest` package if necessary, perhaps within a virtual environment
```
pip install pytest
``` 
And invoke it from the root directory of this repository to run tests:

```py
pytest
```

