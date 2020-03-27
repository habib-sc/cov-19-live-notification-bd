from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

ntimegap = int(input("Enter the time delay in second & press enter: "))


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=30
    )


def getData(url):
    d = requests.get(url)
    return d.text


if __name__ == "__main__":
    while True:
        # notifyMe("Covid-19 Notify", "Stay home & decrease the spread of coronavirus")
        myHtmlData = getData('https://campaign.thedailystar.net/covid19/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        myDataStr = ""
        for section in soup.find_all('div', {'class': 'info-box-content'}):
            myDataStr += section.get_text()

        itemList = myDataStr.split()
        nTotalConfirmed = f"Total Confirmed: {itemList[0]}"
        nTotalDeath = f"Total Death: {itemList[10]}"
        nTotalQuarantine = f"Total Quarantine: {itemList[3]}"
        nQuarantineReleased = f"Quarantine Released: {itemList[6]}"

        nText = f"{nTotalConfirmed} \n{nTotalDeath} \n{nTotalQuarantine} \n{nQuarantineReleased}"
        if True:
            nTitle = "Covid-19 Live Update Bangladesh"
            notifyMe(nTitle, nText)

        time.sleep(ntimegap)