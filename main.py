import csolver
import urllib.parse
import urllib.request
import http.cookiejar
import ssl

print(csolver.csolver("sample.jpg"))

url = "https://ebideb.tubitak.gov.tr/olimpiyatSinavSonucSistemi.htm"

headers = {
  'Connection': 'keep-alive',
  'Cache-Control': 'max-age=0',
  'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
  'sec-ch-ua-mobile': '?0',
  'Upgrade-Insecure-Requests': '1',
  # 'Origin': 'https://arionline.ariokullari.k12.tr',
  'Content-Type': 'application/x-www-form-urlencoded',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-User': '?1',
  'Sec-Fetch-Dest': 'document',
  # 'Referer': 'https://arionline.ariokullari.k12.tr/login/index.php',
  'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
}

cookie_jar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
urllib.request.install_opener(opener)

payload = {
  "hdnSinavBilgileriniGetir": 1,
  "TCKimlikNo": 1,
  "sinavYili": 2023,
  "olimpiyatDal.id": 4,
  "olimpiyatSinavTurleri.id": 1,
  "guvenlik": "een3"
}

data = urllib.parse.urlencode(payload)
binary_data = data.encode('UTF-8')

request = urllib.request.Request(url, binary_data, headers)
response = urllib.request.urlopen(request)
contents = response.read()
contents = contents.decode("utf-8")

print(contents.find("2023 yılı Bilgisayar 1. Aşama Sınavının sonucu açıklanmamıştır."))