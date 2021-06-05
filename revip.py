#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
import os
import requests
from colorama import Fore, init
from multiprocessing import Pool 
from multiprocessing.dummy import Pool as ThreadPool
from re import findall as reg
init(autoreset=True)

def repip(url):
	try:
		grab = requests.get('https://tools.webservertalk.com/?tool=reverseip&host='+url).content
		if 'Domain/IP:' in grab:
			regx = reg('<td class="text-left">(.*?)<', grab)
			for ckk in regx:
				mek = ckk.replace("Domain","")
				print "{}[Grabbed] {}".format(Fore.YELLOW, str(mek))
				open('grabbed.txt', 'a').write('http://'+mek+'\n')
			else:
				print "{}[Operation timed out] {}".format(Fore.RED, str(url))
	except:
		pass

banner =  """
   Reverse Ip MultiThread  |  Ajibarang 03/06/2k21{}
       Icq : https://icq.im/Shin403
       Blog : https://www.blog-gan.org          
       Online Tools : http://secpriv8.com
""".format(Fore.YELLOW)
print banner
url = open(raw_input(Fore.WHITE+'Input list:~# '),'r').read().splitlines()
Thread = raw_input(Fore.WHITE+'Thread :~# ')
pool = ThreadPool(int(Thread))
pool.map(repip, url)
pool.close()
pool.join()
