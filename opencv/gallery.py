'''
Gallery
Show in sequence the images on my Pictures folder
Press q to quit
'''

import cv2 as cv
import os

base_path = '/home/hammer/Pictures'

names = os.listdir('/home/hammer/Pictures')
paths = list(map(lambda a : os.path.join(base_path, a), names))

pics = list(filter(os.path.isfile, paths))
n_pics = len(pics)

for i, pic in enumerate(pics, 1): 
	filename = os.path.basename(pic)
	print(f'Showing image {i}/{n_pics}: {filename}')
	img = cv.imread(pic)
	cv.imshow(filename, img)
	
	k = cv.waitKey(0)

	cv.destroyAllWindows()
	
	if k == ord('q'):
		break

print("Exit")
	


