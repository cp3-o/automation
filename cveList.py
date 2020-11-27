import requests 
import json 

def main(): 

		content = requests.get("httpsL//cve.circl.lu/api/last")
		json = content.json()

		for item in json
			print("{} {}".format("Vuln num:", item['id']))
			print("{} {}".format("Description:", item['summary']))

main()