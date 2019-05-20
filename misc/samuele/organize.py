import os
import sys
import subprocess
import shutil as shu

def createFolder(directory):
	try:
		if not os.path.exists(directory):
		    os.makedirs(directory)
		else:
			shu.rmtree(directory)
			os.makedirs(directory)
	except OSError:
		print ('Error: Creating directory '+ directory)

if (len(sys.argv)!=2):
    print('usage: organize.py <duration of the sample with the format totalseconds_duration of a measure_pause> \n both the duration and the pause must be written as decimal number with at least a decimal digit')
    sys.exit()
#dictionary that contains the map currency->code 
currency={}
#dictionary that contains the map feature->code 
features={}

with open ('config.currency','rt') as curr:
    #read specific: 
    for line in curr:
        currency.update({line.split()[0].lower():line.split()[1]})
print('Number of supported currency: '+str(len(currency)))    

with open ('config.features','rt') as feat:
    #read specific: 
    for line in feat:
        features.update({line.split()[0].replace('/','-'):line.split()[1]})
        
print('Number of supported features: '+str(len(features))) 

#creare la directory datasets

createFolder('datasets')
path='./datasets'

folders=[i.decode('utf-8').replace('/','') for i in subprocess.check_output("ls -d */", shell=True).split()]
print('Trovate '+str(len(folders))+'cartelle')
min=320000
for folder in folders:
    #check if the folder name is in currency list
    if folder in currency:
        #scendere in profondo e creare tutti i file necessari
        subfolders=[i.decode('utf-8').replace('/','') for i in subprocess.check_output('ls '+folder, shell=True).split()]
        print('Dentro '+folder+' sono state trovate '+str(len(subfolders))+' cartelle')
        for feature in subfolders:
            if feature in features:

                #enter in the duration folder get it from the input
                if not os.path.exists(folder+'/'+feature+'/'+str(sys.argv[1])):
                    print('error: the folder with the info you passed was not found')
                    sys.exit()
                #the folder exists
                samples=[i.decode('utf-8').replace('/','') for i in subprocess.check_output('ls '+folder+'/'+feature+'/'+str(sys.argv[1]), shell=True).split()]
                #now for all the folders we access the file value.txt inside it and copy it changing the name
                for sample in samples:
                    new_file_name=folder+'_'+features.get(feature)+'_'+currency.get(folder)+'_'+sample.replace('sample_','')+'.txt'
                    shu.copy2(folder+'/'+feature+'/'+str(sys.argv[1])+'/'+sample+'/values.txt',path+'/'+new_file_name)
                    aux=0
                    with open (path+'/'+new_file_name, 'rt') as fil:
                        aux=sum(1 for line in fil)
                        if aux<min:
                            min=aux
                        
    else:
        print(folder+' skipped')
print('Done!')
print('Min number of line(s): '+str(min))
