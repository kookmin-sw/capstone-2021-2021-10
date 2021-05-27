import sys
import matplotlib.pyplot as plt

dic = {}
arr = [ 0 for _ in range(2501)]
under_2000 = 0
under_1500 = 0
for line in sys.stdin:
	n = len(line.strip().split())
	arr[n] += 1
	if n < 2000: under_2000 += 1
	if n < 1500: under_1500 +=1
	
	if n in dic:
		dic[n] += 1
	else:
		dic[n] = 1

print(dic)

print(f"under_2000: {under_2000} \nunder_1500L {under_1500}") 

#plt.plot( arr)
#plt.yscale('log')
#plt.show()


