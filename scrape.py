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


def scrape_pm25():
    try:
        url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON"
        datas = requests.get(url).json()["records"]
        columns = list(datas[0].keys())
        values = [list(data.values()) for data in datas]
        return columns, values
    except Exception as e:
        print(e)
    return None, 404


if __name__ == "__main__":
    print(scrape_pm25())
