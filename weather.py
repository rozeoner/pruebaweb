from urllib.request import urlopen
import bs4

class WeatherClient(object):
    """WeatherClient class"""
    def __init__(self):
        super(WeatherClient, self).__init__()
    def download_page(arg):
        #connect to the website
        f = urlopen("")
        #get the download download_page
        page = f.read()
        #close the connection
        f.close()
        return page
    def search_activities(self,page):
        tree = bs4.BeautifulSoup(page,"lxml")
        t = tree.find("temperature)
        w = tree.find("weather")
        print(t["value"]+ "and "+["value"])
        return None

    def run(self):
        # download a web page
        page = self.download_page()
    # seach activities in web page
        data = self.search_activities(page)
    # print the activities
        print(data)


if __name__=="__main__":
    c = BanggoodClient()
    c.run()
