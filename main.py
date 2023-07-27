import csolver
import scraper
import dotenv
import os

dotenv.load_dotenv()

url = "https://ebideb.tubitak.gov.tr/olimpiyatSinavSonucSistemi.htm"

ret = scraper.scrape(os.getenv("DWRSESSIONID"), os.getenv("TC"), url, "gh.jpg") # you could actually use anything for your session id

while ret == 0:
  ret = scraper.scrape(os.getenv("DWRSESSIONID"), os.getenv("TC"), url, "gh.jpg") # you could actually use anything for your session id

print(ret)