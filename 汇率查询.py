# encoding : utf-8

import requests
from bs4 import BeautifulSoup
import pyperclip
from 货币缩写库 import 缩写库 as sxk

requests.packages.urllib3.disable_warnings()

def GetRoot(_from = "CNY", _to = "ARS"):
	url = u"https://cn.exchange-rates.org/Rate/%s/%s"%(_to, _from)
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
	response = requests.get(url, headers = headers, verify=False)
	try:
		if response.status_code == 200:
			soup = BeautifulSoup(response.text, 'html.parser')
			rate_range = BeautifulSoup(str(soup.find("tbody")), 'html.parser')
			for i in rate_range.find_all("td"):
				if " " + _from in str(i):
					return float(i.text.replace(" " + _from, ""))
		else:
			return "Unknow Return!Status Code: %d"%response.status_code
	except:
		return "无相关汇率！"

def main():
	#for i in sxk:
	#	print(i)
	print(GetRoot())

if __name__ == '__main__':
	main()

