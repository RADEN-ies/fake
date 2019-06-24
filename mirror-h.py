#!/usr/bin/python
import requests

# c =  "\033[0;36m"
# y =  "\033[93m"
# w =  "\033[0m"
# g =  "\033[92m"
# r =  "\033[91m"

print """
\033[0;36m#####################	\033[91m| \033[0mAuto Submit mirror-h.org 
\033[0;36m# \033[93m|SUBMITER| \033[0;36m#	\033[91m| \033[92m@Author : MR.W4HYU
\033[0;36m# \033[93m|DONG    | \033[0;36m#	\033[91m| \033[92m@Github : https://github.com/RADEN-ies
\033[0;36m#####################	\033[91m| \033[92m@Version : 1.0
"""
nick = raw_input("\033[91mNick Kamu: \033[0m")
liat = raw_input("\033[91mList Website: \033[0m")
def cek(nik, web):
	req = requests.post("https://mirror-h.org/site-send", {'user': nik, 'url': web}).status_code
	if req == 200:
		print "\033[92m[\033[93m+\033[92m] Sukses: \033[0m"+web+""
	else:		
		print "\033[91m[\033[0m-\033[91m] Gagal: \033[0m"+web+""
	
f=open(liat,'r')
kontent=f.read()
x=kontent.split("\n")		
for i in x:
cek(nick ,i)
