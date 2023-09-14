from augmentations import *
import cv2
import os
import random
from natsort import natsorted

def Augmentation_Worker(output_param= None, dataset_input=None, aug_list=None, out_path=None):
	# inputs
	output_parameters = output_param
	dataset_input_path = dataset_input
	augmentation_list = aug_list
	output_path = out_path

	image_files = natsorted([os.path.join(dataset_input_path, f) for f in os.listdir(dataset_input_path) if f.endswith(('.jpg', '.jpeg', '.png'))])
	annotation_files = natsorted([os.path.join(dataset_input_path, f) for f in os.listdir(dataset_input_path) if f.endswith(('.txt'))])
	
	current_index = 0
	do_random = False
	file_name = 0

	# original dataset images will distributed among augmenteds in the end
	output_number = (len(image_files) * output_parameters['size'])
	augmentation_number = output_number - len(image_files)

	#Create output folder
	folder_name = "Augmented-Dataset"
	output_folder = ""
	number = 1
	while True:
		new_name = folder_name if number == 1 else f"{folder_name}{number}"
		output_folder = os.path.join(output_path, new_name)
		if not os.path.exists(output_folder):
			os.makedirs(output_folder)
			break
		number += 1

	# Per loop makes an augmented image
	for i in range(augmentation_number):
		#kaynak image olarak bir image birden çok kez kullanılabilir. Eğer tüm liste kullanılırsa random index alacak
		if current_index == len(image_files) or do_random:
			do_random = True
			current_index = random.randint(0, len(image_files)-1)

		
		the_name = image_files[current_index]
		base_name = os.path.splitext(os.path.basename(the_name))[0]
		the_annot_path = os.path.join(dataset_input_path, f"{base_name}.txt")

		#The processing image in this loop
		the_img = cv2.imread(the_name)
		the_annots, class_id = getAnnotList(the_annot_path, the_img.shape)


		total_aug_num = len(augmentation_list)
		# Kaç defa augmentation yapılacağını belirledik.
		aug_process_num = random.randint(1, total_aug_num)

		counter = 0
		for process in augmentation_list:
			counter+=1

			if process == "blur":
				a = Blur(augmentation_list['blur'], the_img)
				the_img = a.ApplyBlur()
			elif process == "brightness":
				a = Brightness(augmentation_list['brightness'], the_img)
				the_img = a.ApplyBrightness()
			elif process == "flip":
				if augmentation_list['flip'][0] and augmentation_list['flip'][1]:
					p1 = random.choice([True, False])
					p2 = random.choice([True, False])
					p1 = True if p1 == False and p2 == False else p1
					a = Flip(the_img, p1, p2, the_annots)
					the_img, the_annots = a.ApplyFlip()
				else:
					a = Flip(the_img, augmentation_list['flip'][0], augmentation_list['flip'][1], the_annots)
					the_img, the_annots = a.ApplyFlip()
			elif process == "hue":
				a = Hue(augmentation_list['hue'], the_img)
				the_img = a.ApplyHue()
			elif process == "noise":
				a = Noise(augmentation_list['noise'], the_img)
				the_img = a.ApplyNoise()
			elif process == "rotation":
				angle = 0
				if augmentation_list['rotation'].count('True') > 1:
					index_list = [i for i, value in enumerate(augmentation_list['rotation']) if value=='True']
					random_index = random.choice(index_list)
					angle = 90 if random_index == 0 else (180 if random_index == 2 else 270)
				else:
					if augmentation_list['rotation'][0] == 'True':
						angle = 90
					elif augmentation_list['rotation'][1] == 'True':
						angle = 270
					elif augmentation_list['rotation'][2] == 'True':
						angle = 180
					else:
						print("NO WAY")
				
				a = Rotate(the_img, angle, the_annots)
				the_img, the_annots = a.ApplyRotate()
			elif process == "saturation":
				a = Saturation(augmentation_list['saturation'], the_img)
				the_img = a.ApplySaturation()
			elif process == "sensitive_rotation":
				a = SensitiveRotate(the_img, augmentation_list['sensitive_rotation'], the_annots)
				the_img, the_annots = a.ApplySensitiveRotate()
			elif process == "grayscale":
				a = Grayscale(the_img)
				the_img = a.ApplyGrayscale()

			if counter == aug_process_num:
				break
					
		#Save images
		tempo = os.path.join(output_folder, f"{file_name}.jpg")
		cv2.imwrite(tempo, the_img)
		#Save annotations
		annot_out_name = os.path.join(output_folder, f"{file_name}.txt")
		annot_out_file = open(annot_out_name, 'w')

		for bbox in the_annots:
			yolo_formmatted_annot = pascal_voc_to_yolo(bbox[0], bbox[1], bbox[2], bbox[3], the_img.shape[1], the_img.shape[0])
			yolo_formmatted_annot.insert(0, str(int(class_id)))
			annot_to_print = " ".join(yolo_formmatted_annot)

			
			annot_out_file.write(annot_to_print)
			annot_out_file.write('\n')
		annot_out_file.close()


		current_index+=1	
		file_name+=1

	#Orijinal dataseti ekle
	for i in range(len(image_files)):
		im = cv2.imread(image_files[i])
		cv2.imwrite(os.path.join(output_folder, f"{file_name}.jpg"), im)

		annot_out_name = os.path.join(output_folder, f"{file_name}.txt")
		with open(annotation_files[i], "r") as source, open(annot_out_name, "w") as annot_out_file:
		    for line in source:
		        # Her satırı yazılacak dosyaya yaz
		        annot_out_file.write(line)

		file_name+=1

	#train-val-test spliti yap

		

def getAnnotList(path, shape):
	annotations = []
	class_id = 0
	with open(path, 'r') as f:
		lines = f.readlines()
		for line in lines:
			parts = line.strip().split()
			if len(parts) == 5:
				class_id, x_center, y_center, width, height = map(float, parts)

				img_width, img_height = shape[1], shape[0]
				x = int(x_center * img_width)
				y = int(y_center * img_height)
				w = int(width * img_width)
				h = int(height * img_height)

				# [xmin,ymin,xmax,ymax] formatted
				annotations.append([x - w // 2, y - h // 2, x + w // 2, y + h // 2])
	return annotations, class_id

def pascal_voc_to_yolo(x1, y1, x2, y2, image_w, image_h):
	# [x_min, y_min, x_max, y_max] to [x_center, y_center, width, height]
	return [str((x2 + x1)/(2*image_w)), str((y2 + y1)/(2*image_h)), str((x2 - x1)/image_w), str((y2 - y1)/image_h)]