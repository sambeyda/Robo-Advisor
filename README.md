# "Robo Adivsor" Project

A solution for the ["Robo Advisor" project](https://github.com/sambeyda/Robo-Advisor/blob/master/Robo-Advisor-Master/App/robo_advisor.py)

Issues requests to the [AlphaVantage Stock Market API](https://alphavantage.co/) in order to provide automated stock or cryptocurrency trading reccommendations.

## Prerequisities

    + Anaconda 3.7
    + Python 3.7
    + Pip

## Installation

Clone or download [this repository](https://github.com/sambeyda/Robo-Advisor) onto your computer
Then navigate to there from the command line:

'''sh
cd Robo-Advisor-Master
'''

Use Anaconda to create a new virtual environment where you will download package dependencies

'''sh
pip install requests, csv, os, json, python-dotenv, datetime,statistics

## Setup

Before using or developing this application, take a moment to [obtain an AlphaVantage API Key](https://www.alphavantage.co/support/#api-key) (e.g. "abc123").

After obtaining an API Key, create a new file in this repository called ".env", and update the contents of the ".env" file to specify your real API Key:

    API_KEY="abc123"

## USAGE

Run the robo_advisor tool script to find your stock recommendation

'''py
python app/robo_advisor.py
