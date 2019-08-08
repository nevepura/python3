'''
Punti:
x0,y0
x1,y0
x0,y1
x1,y1
'''

import json
import pprint
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as xdm

INPUT_FILE = 'Latex_sample.json'
OUTPUT_PATH = './output/'

def collect_points(annotation):
	x0 = annotation['segmentation'][0][0]
	y0 = annotation['segmentation'][0][1]
	x1 = annotation['segmentation'][0][4]
	y1 = annotation['segmentation'][0][5]
	points = [x0, y0, x1, y1]
	return points


def write_on_new_xml(OUTPUT_PATH, file_name, points):
	root = ET.Element('document')
	root.attrib['filename'] = file_name[:-4]
	tableRegion = ET.SubElement(root, 'tableRegion')
	Coords = ET.SubElement(tableRegion, 'Coords')

	x0 = points[0]
	y0 = points[1]
	x1 = points[2]
	y1 = points[3]
	stringified_points = "{},{} {},{} {},{} {},{}".format(x0, y0, x1, y0, x0, y1, x1, y1)
	
	Coords.attrib['points'] = stringified_points
	tree = ET.ElementTree(root)
	tree.write(OUTPUT_PATH + file_name, encoding = "UTF-8", xml_declaration=True)


# aggiunge i punti di una tabella a un file già presente
def add_points_to_old_xml(old_file, points):
	tree = ET.parse(old_file)
	root = tree.getroot()
	docum = root.find('document')
	tableRegion = ET.SubElement(root, 'tableRegion')
	Coords = ET.SubElement(tableRegion, 'Coords')
	x0 = points[0]
	y0 = points[1]
	x1 = points[2]
	y1 = points[3]
	stringified_points = "{},{} {},{} {},{} {},{}".format(x0, y0, x1, y0, x0, y1, x1, y1)
	
	Coords.attrib['points'] = stringified_points
	tree.write(OUTPUT_PATH + file_name, encoding = "UTF-8", xml_declaration=True)	


# MAIN
data = json.load(open(INPUT_FILE, 'r'))
#pprint.pprint(data, depth = 1) # mosta la struttura del json, 1° livello

number_of_images = len(data['images'])
number_of_annotations = len(data['annotations'])

# array contenente tutte le immagini
images = []
for i in range(number_of_images):
	images.append(data['images'][i])
#print('IMAGES: ' + str(images[0:10]))

# array contenente tutte le annotazioni
annotations = []
for i in range(number_of_annotations):
	annotations.append(data['annotations'][i])
#print(annotations[0:5])

image_ids = [] # id delle immagini già inserite

for i, annotation in enumerate(annotations):
	
	image_id = annotations[i]['image_id']
	image_index = image_id - 1 # id=1 corrisponde a elemento=0 dell'array images
	file_name = str(images[image_index]['file_name'][:-4]) + '.xml' # il nome dell'xml è pari al nome dell'immagine, ma con estensione '.xml'
	points = collect_points(annotation)

	if image_id not in image_ids: # id non presente -> crea new xml file
		# aggiunge l'id corrente agli id delle immagini inserite
		image_ids.append(image_id)
		write_on_new_xml(OUTPUT_PATH, file_name, points)

	else: # id già presente -> inserisci annotazione di questa tabella in file xml già esistente
		add_points_to_old_xml(OUTPUT_PATH + file_name, points)
		

