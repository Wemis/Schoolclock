import os
import time


alltime6=19800 # all time of 6 lessons in secounds
alltime7=23100 # all time of 7 lessons in secounds


lessons=int(input("Уроков(6/7) ")) 
if lessons==6:
	timel=19800
	while True:
		os.system("clear") 
		print("[*] Осталось секунд:", timel) 
		print("[*] Осталось минут:", int(timel/60))
		print("[*] Осталось часов:", round(timel/3600, 1)) 
		print("[*] DAY COMPLETE ",round(100-timel/alltime6*100, 2),"%")
		timel-=1
		time.sleep(1) 
		if timel==-1:
			break
	print("[✅] day complete! ") 

if lessons==7:
	timel=23100
	while True:
		os.system("clear") 
		print("[*] Осталось секунд:", timel) 
		print("[*] Осталось минут:", int(timel/60))
		print("[*] Осталось часов:", round(timel/3600, 1)) 
		print("[*] DAY COMPLETE ",round(100-timel/alltime7*100, 2),"%") 
		timel-=1
		time.sleep(1) 
		if timel==-1:
			break
	print(" [✅] day complete! ") 

else:
	print("Invalid name", "'",lessons,"'") 
	print("Введите значение 6 или 7") 
	print("Abort.") 
