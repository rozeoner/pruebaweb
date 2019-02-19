from urllib.request import urlopen
import bs4

class BanggoodClient(object):
    """Banggood class"""
    def __init__(self):
        super(BanggoodClient, self).__init__()
    def download_page(arg):
        #connect to the website
        f = urlopen("https://www.banggood.com/es/Flashdeals.html")
        #get the download download_page
        page = f.read()
        #close the connection
        f.close()
        return page
    def search_prices(self,page):
        tree = bs4.BeautifulSoup(page,"lxml")
        prices = tree.find_all("div","priceitem")
        price_list = []
        for price in prices:
            price = price.find("span","price")
            price_list.append(price.text)
        return price_list

    def run(self):
        # download a web page
        page = self.download_page()
    # seach activities in web page
        data = self.search_prices(page)
    # print the activities
        print(data)


if __name__=="__main__":
    c = BanggoodClient()
    c.run()
