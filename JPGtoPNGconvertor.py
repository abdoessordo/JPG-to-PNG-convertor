import os
from PIL import Image

#grab start and end folders


def mkdir(folder):
	newfolder = f'{folder}/converted_imgs'
	if not os.path.exists(newfolder):
		os.mkdir(newfolder)
	return newfolder

def get_images(input):
	return [file for file in os.listdir(input)]

def load_img(input,file):
	return Image.open(f'{input}/{file}')

def get_file_name(file):
	return file.split('.')[0]

def convert_img(file, input, output):
	return load_img(input, file).save(f'{output}/converted_imgs/{get_file_name(file)}.png')

def convert_all_imgs(input, output):
	global msg
	mkdir(output)
	for img in get_images(input):
		convert_img(img, input, output)

