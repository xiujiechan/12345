import requests
from bs4 import BeautifulSoup


def scrape_stocks():
    try:
        url = "https://histock.tw/%E5%9C%8B%E9%9A%9B%E8%82%A1%E5%B8%82"
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text.split("<h3>今年以來</h3>")[1], "lxml")
        trs = soup.find("div", class_="index-list").find_all("tr")
        datas = []
        for tr in trs:
            data = []
            for th in tr.find_all("th"):
                # print(th.text)
                data.append(th.text)
            for td in tr.find_all("td"):
                # print(td.text)
                data.append(td.text)
            datas.append(data)
        return datas
    except Exception as e:
        print(e)
    return None


if __name__ == "__main__":
    print(scrape_stocks())
