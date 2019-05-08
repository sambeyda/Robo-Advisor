#Robo Advisor Testing

from app.robo_advisor import to_usd, compile_url, api_key, get_response
import os

#Basic Challenge
def test_to_usd(): #Taken from executive dashboard testing
    #Tests whether number is returned with $ sign and two decimal places
    assert to_usd(10) == "$10.00"

    #Tests whether number rounds decimal places
    assert to_usd(10.33333333333333) == "$10.33"

    #Tests whether there is a thousand seperator
    assert to_usd(10000) == "$10,000.00"

#Basic Challenge
def test_compile_url():
    #Tests whether a sample symbol constructs necessary expected url in proper format
    stock_symbol = "MU" #sample
    result = compile_url(stock_symbol)
    assert result == f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MU&apikey={api_key}"

#Intermediate Challenge 
def test_get_response():
    #request_url=compile_url(stock_symbol)
    stock_symbol= "MU"
    parsed_response = get_response(compile_url(stock_symbol))

    assert isinstance(parsed_response, dict) #Checks if its in proper original format: Dictionary
    assert "Meta Data" in parsed_response.keys() #Checks whether correct header
    assert "Time Series (Daily)" in parsed_response.keys() #''
    assert parsed_response["Meta Data"]["2. Symbol"] == stock_symbol #Checks whether Symbol is in fact Correct!
#Intermediate Challenge
#def test_write_to_csv():
    #Setting up example data output
    #example_data = [
        #{"timestamp": "2019-05-08", "open": "97", "high": "99", "low": "95", "close": "98.5", "volume": "10"},
        #{"timestamp": "2019-05-07", "open": "96", "high": "98", "low": "94", "close": "97.5", "volume": "9"},
        #{"timestamp": "2019-05-06", "open": "95", "high": "97", "low": "93", "close": "96.5", "volume": "8"}
    #]
    #csv_file_path= os.path.join(os.path.dirname(__file__), "..", "data", "temp_stock_prices.csv") #taken from base code

    #if os.path.isfile(csv_file_path): #Remove file
        #os.remove(csv_file_path)

    #assert os.path.isfile(csv_file_path) == False #Checking if file is properly removed: SETUP GOOD
    #Check if CSV file is written
    #expectation = write_to_csv(csv_file_path)

    #assert expectation == True #Checks if CSV was written
    #assert os.path.isfile(csv_file_path) == True
