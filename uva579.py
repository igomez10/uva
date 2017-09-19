def solve():
	entrada = list(map(lambda x: int(x) , input().split(':')))
	if entrada[0] == 0:
		return 
	hora = entrada[0] 
	minuto = entrada[1]

	anguloHora = (hora / 12) * 360  + 30*(minuto / 60)
	anguloMinuto = (minuto / 60) * 360
#	print(anguloHora, anguloMinuto)
	a = max(anguloHora , anguloMinuto) - min(anguloHora, anguloMinuto)
	
	b = 360 - max(anguloHora, anguloMinuto) + min(anguloHora, anguloMinuto)
	print( '{0:.3f}'.format(float(min(a, b))))


while(True):
	try:
		solve()
	except:
		break