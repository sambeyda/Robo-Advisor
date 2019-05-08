#Robo Advisor Testing

from app.robo_advisor import to_usd, compile_url

def test_to_usd(): #Taken from executive dashboard testing
    #Tests whether number is returned with $ sign and two decimal places
    assert to_usd(10) == "$10.00"

    #Tests whether number rounds decimal places
    assert to_usd(10.33333333333333) == "$10.33"

    #Tests whether there is a thousand seperator
    assert to_usd(10000) == "$10,000.00"

def test_compile_url():
    #Tests whether a sample symbol constructs necessary expected url in proper format
    stock_symbol = "MU" #sample

    parsed_response = compile_url(stock_symbol)

    assert isinstance(parsed_response, dict) #Checks if its in proper original format: Dictionary
    assert "Meta Data" in parsed_response.keys() #Checks whether correct header
    assert "Time Series (Daily)" in parsed_response.keys() #''
    assert parsed_response["Meta Data"]["2. Symbol"] == stock_symbol #Checks whether Symbol is in fact Correct!
