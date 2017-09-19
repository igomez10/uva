import math

def solve():
	firstLine = list(map(lambda x: int(x) , input().split(' ')))
	minimumPrice = math.inf

	for i in range(firstLine[2]):
		price = input()
		beds = list(map(lambda x: int(x) , input().split(' ')))
		if (firstLine[0] * int(price)) > firstLine[1] or firstLine[0] > max(beds):
	#		precio mayor a presupuesto
	#		camas insuficientes
			continue
	#	se cumplen condiciones en este hotel
		costo = firstLine[0] * int(price)
		if costo < minimumPrice:
			minimumPrice = costo

	if minimumPrice == math.inf:
		print ('stay home')
	else:
		print(minimumPrice)


while(True):
	try:
		solve()
	except:
		break

