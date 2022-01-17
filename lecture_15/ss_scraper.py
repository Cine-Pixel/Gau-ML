from bs4 import BeautifulSoup
import requests


url = "https://ss.ge/ka/udzravi-qoneba/l/bina/iyideba?MunicipalityId=95&CityIdList=95&StatusField.FieldId=34&StatusField.Type=SingleSelect&StatusField.StandardField=Status&PriceType=false&CurrencyId=1"
print(requests.get(url))