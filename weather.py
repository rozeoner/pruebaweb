from urllib.request import urlopen
import bs4
import pprint
import xmltodict
import json

class WeatherClient(object):
    """WeatherClient class"""
    def __init__(self):
        super(WeatherClient, self).__init__()
    def download_page(self):
        #connect to the website
        f = urlopen("https://api.openweathermap.org/data/2.5/find?q=Lleida&units=metric&appid=b7b2e643ead5159c6a3155abbfa0607c&mode=json&lang=ca")
        #get the download download_page
        data = f.read()
        #close the connection
        f.close()
        return data
    def search_activities(self,html):
        dic = json.loads(html)
        temp = dic['list'][0]['main']['temp']
        weath = dic['list'][0]['weather'][0]['description']
        return (str(temp)+" and "+weath)

    def run(self):
        # download a web page
        data = self.download_page()
    # seach activities in web page
        data = self.search_activities(data)
    # print the activities
        print(data)


if __name__=="__main__":
    c = WeatherClient()
    c.run()
