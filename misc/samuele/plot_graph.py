import os
import sys
import matplotlib.pyplot as plt
import subprocess

def createFolder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
	except OSError:
		print ('Error: Creating directory '+ directory)


crypto1= str(sys.argv[1])

target=str(sys.argv[2])
target2=target
target=target.replace('/','-')

total_time=int(sys.argv[3])
duration=float(sys.argv[4])
pause= float(sys.argv[5])

crypto=[crypto1]
currencies=len(sys.argv)-5
temp=currencies-1
index=6
while len(sys.argv)>6 and temp>0:
	crypto.append(sys.argv[index])
	index=index+1
	temp=temp-1
crypto=sorted(crypto)
path=[]
for i in range(0,currencies):
	path.append('./'+crypto[i]+'/'+target+'/'+str(total_time)+'_'+str(duration)+'_'+str(pause))

sample=[]
for i in range(0,currencies):
	temp=subprocess.check_output(["ls", path[i]]).split()
	temp=[int(sample.decode('utf-8').replace('sample_','')) for sample in temp]
	sample.append(temp)

values=[]
i=0

while i<min([len(x) for x in sample]):
	for j in range(0,currencies):
		with open(path[j]+'/'+'sample_'+str(sample[j][i])+'/values.txt', 'r') as f:
			temp=[]
			for val in f.read().split():
				temp.append(float(val))
			values.append(temp)

    
	
	crypto=[x.upper() for x in crypto]
	
	for j in range(currencies):
		plt.plot(values[j], label=crypto[j])
	
	plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
	plt.subplots_adjust(right=0.8)
	plt.grid(True)
	plt.xlabel('Number of sample(s)')
	plt.ylabel('Number of '+target2)
	nameOfCurrency=''
	for j in range(0,currencies):
		nameOfCurrency=nameOfCurrency+crypto[j]+'-'
	nameOfCurrency=nameOfCurrency[:-1]
	plt.suptitle(target2[0].upper()+target2[1:]+' comparison between '+nameOfCurrency)
	ymin=min(min(values))
	ymax=max(max(values))
	ymin=ymin*0.9
	ymax=ymax*1.10
	plt.ylim(ymin,ymax)


    #forse e' necessario creare la directory prima
	path_save='plot/'+nameOfCurrency+'/'+target+'/'+str(total_time)+'_'+str(duration)+'_'+str(pause)
    
	createFolder(path_save)
	
	plt.savefig(path_save+'/graph_'+str(i)+'.pdf')
    #dovrebbe uscire una roba del tipo plot/btc-xmr/cache-misses/600_10_10/graph1.pdf
    
    #pulisco i vettori
	del values[:]
	plt.clf()
	i=i+1
	
	
