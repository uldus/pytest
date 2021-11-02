#https://statsapi.web.nhl.com/api/v1/schedule
import requests
import json
def get_data():
    url = 'https://statsapi.web.nhl.com/api/v1/schedule'
    # url = 'https://statsapi.web.nhl.com/api/v1/schedule?date=2021-10-31'
    #url = 'https://statsapi.web.nhl.com/api/v1/schedule?startDate=2021-11-01&endDate=2021-11-02'
    req = requests.get(url)
    response = req.json()
    totalGames = response["totalGames"]
    totalEvents = response["totalEvents"]
    #print(totalGames,totalEvents)
    text = ''
    for totalGame in range(0,totalGames):
       away = response["dates"][0]['games'][totalGame]['teams']['away']['team']['name']
       away_s =response["dates"][0]['games'][totalGame]['teams']['away']['score']
       home= response["dates"][0]['games'][totalGame]['teams']['home']['team']['name']
       home_s = response["dates"][0]['games'][totalGame]['teams']['home']['score']
       #print(f"{away}) {away_s} - {home_s} {home}")
       text = text + (f"{away} {away_s} - {home_s} {home}") + "\n"
    return text
    #sell_price = response["btc_usd"]["sell"]
    #print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")
    #print(dates)

if __name__ == '__main__':

    get_data()
    #telegram_bot(token)