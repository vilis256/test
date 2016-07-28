def tr(n):
		tot=0
		counter=0
		for i in xrange(n+1):
			tot+=i
		return tot
def div(n):
		counter=0
		for i in xrange(1,int(round(n**0.5))+1):
			if n%i==0:
				counter+=2
			if i*i==n:
				counter-=1
		return counter
i=0
while True:
	if div(tr(i))>=500:
		print tr(i),div(tr(i)),i
		break
	else:
		i+=1 

