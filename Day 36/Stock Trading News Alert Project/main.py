import os
import requests
from twilio.rest import Client
STOCK_NAME = "AMD"
COMPANY_NAME = "Advanced Micro Devices"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY") #get it here: https://www.alphavantage.co/
NEWS_API_KEY = os.environ.get("NEWS_API_KEY") #get it here: https://newsapi.org/

TWILIO_SID = os.environ.get("TWI_ACC_SID") #get it here: https://www.twilio.com/
TWILIO_TOKEN = os.environ.get("TWI_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")


#Getting yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"] #holds json value
#print(data)
data_list = [value for (key, value) in data.items()] #creates a list from JSON
yesterday_data = data_list[0] #gets yesterday data
#print(yesterday_data)
yesterday_closing_price = yesterday_data["4. close"] #gets closing price
#print(yesterday_closing_price)

#Getting the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
#print(day_before_yesterday_closing_price)

#Finding the positive difference between 1 and 2.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) #abs() gives absolute values
#print(difference)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#The percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference/ float(yesterday_closing_price)) * 100)
#print(diff_percent)

#If percentage is greater than 5 then Get the News.
if diff_percent > 5:
    #print("get news")
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": STOCK_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    #print(articles)

#Using Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#Creating a new list of the first 3 articles' headline and description using list comprehension.
formated_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']} " for article in three_articles]
#more information can be added by tapping other keys into the list

#Send each article as a separate message via Twilio.
client = Client(TWILIO_SID, TWILIO_TOKEN)


for article in formated_articles:
    message = client.messages.create(
        body=article,
        from_=TWILIO_NUMBER,
        to=MY_NUMBER
    )
    #print("message sent")