
# App/robo_advisor.py
 
#Importing Modules and Packages
import csv
import requests
import json
import os
from dotenv import load_dotenv
import datetime
from statistics import stdev


load_dotenv()
api_key= os.environ.get("API_KEY")
#Refactoring price formatting logic: Taken from previous examples
def to_usd(stock_price): 
    return "${0:,.2f}".format(stock_price)
#Refactoring compile url logic: Compiles url with given symbol and secret api_key
def compile_url(stock_symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"
    return request_url
#Refactoring issuing API requests: Uses JSON to convert parsed response into dictionary
def get_response(request_url):
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response
# Refactoring time stamp formatting logic: Ensures that human friendly current date/time is displayed
#Taken from shopping cart
def human_friendly_timestamp(date_time):
    return date_time.strftime("%m-%d-%Y %I:%M %p")

#Refactoring write to csv logic: COULD NOT GET TO RUN PROPERLY
# def write_to_csv(csv_file_path):
#     csv_headers= ["timestamp", "open", "high", "low", "close", "volume"] #creating headers from alpha csv file
#     with open(csv_file_path, "w") as csv_file: # 
#         writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
#         writer.writeheader() # uses fieldnames of the headers above
#         for date in dates:
#             daily_prices = tsd[date]
#             writer.writerow({
#                 "timestamp": date,
#                 "open": daily_prices["1. open"],
#                 "high": daily_prices["2. high"],
#                 "low": daily_prices["3. low"],
#                 "close": daily_prices["4. close"],
#                 "volume": daily_prices["5. volume"],
#             })
#     return True


#
# INFO INPUTS 
#

if __name__ == "__main__":

    #print(api_key)

    #
    ##USER INPUTTING STOCK SYMBOL
    #
    #Adapted from Ta's solution https://github.com/hiepnguyen034/robo-stock/blob/master/robo_advisor.py
    while True:  
        stock_symbol=input('Enter the stock symbol you want: ')
        if stock_symbol == "DONE": # Allows user to exit code if their symbol does not exist
            exit()
        else:
            if not stock_symbol.isalpha(): #Validation check if symbol is only alphabet letters!
                print('Please make sure to stock symbol in AAAA form')
            else: 
                request_url=compile_url(stock_symbol)
                if 'Error' in request_url:
                    print("Your desired stock does not exit. Try again or enter 'DONE' to exit")
                else:
                    break
    #Parse response from request
    parsed_response=get_response(request_url)
    tsd= parsed_response["Time Series (Daily)"]
    dates= list(tsd.keys())
    recent_day= dates[0]
    last_refreshed = parsed_response["Meta Data"] ["3. Last Refreshed"]
    latest_closing_price = tsd[recent_day]["4. close"]

    high_prices=[]
    low_prices= []

    for date in dates:    
        high_price= tsd[date]["2. high"]
        high_prices.append(float(high_price))
        low_price= tsd[date]["3. low"]
        low_prices.append(float(low_price))
    
    recent_high=max(high_prices) 
    recent_low=min(low_prices)

    #
    # Reading data into csv file
    #

    #Adapted from csv notes and professor's screencast!
    csv_file_path= os.path.join(os.path.dirname(__file__), "..", "data", "stock_prices.csv")

    csv_headers= ["timestamp", "open", "high", "low", "close", "volume"] #creating headers from alpha csv file
    with open(csv_file_path, "w") as csv_file: # 
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames of the headers above
        for date in dates:
            daily_prices = tsd[date]
            writer.writerow({
                "timestamp": date,
                "open": daily_prices["1. open"],
                "high": daily_prices["2. high"],
                "low": daily_prices["3. low"],
                "close": daily_prices["4. close"],
                "volume": daily_prices["5. volume"],
        })
    #write_to_csv(csv_file_path)
    #    
    ## INFO OUTPUT
    #  
    print("-----------------------")
    print(f"STOCK SYMBOL: {stock_symbol}") #Takes user stock symbol
    print("-----------------------")
    print("REQUESTING STOCK MARKET DATA") 
    print("REQUEST AT: ",human_friendly_timestamp(datetime.datetime.now()))  #datetime module for user access time
    print("-----------------------")
    print(f"LATEST DAY: {last_refreshed}") # Last refreshed stock data from alpha advantage
    print(f"LATEST CLOSE: {to_usd(float(latest_closing_price))}") #latest closing price from alpha
    print(f"RECENT HIGH: {to_usd(float(recent_high))}") #recent 12 month high from alpha
    print(f"RECENT LOW: {to_usd(float(recent_low))}") #recent 12 month low from alpha
    print("-----------------------")
    #Recommendation strategy: IDENTIFY UNDER-VALUED STOCKS THAT ARE WELL BELOW THEIR RECENT HIGH
        #INDICATES STOCK HAS POTENTIAL TO RETURN TO THIS PEAK
        #USING STANDARD DEVIATION OF HIGH PRICES TO GAUGE HOW FAR AWAY STOCK IS FROM PEAK
    if float(latest_closing_price) < (float(recent_high))-(1.5*float(stdev(high_prices))):
        print("RECOMMENDATION:")
        print("BUY because the latest closing price is at least 1.5 standard deviation away from its recent high; indicating future upside of the stock returning near that peak")
    else:
        print("RECOMMENDATION:")
        print("DON'T BUY because the latest closing price is relatively close to its recent high (within 1.5 standard deviations); indicating a lack of future upside as stock may have already reached its peak")
    print("-----------------------")
    print(f"WRITING DATA INTO CSV: {csv_file_path}...")
    print("-----------------------")
    print("HAPPY INVESTING")
    print("-----------------------")
