#python script to generate a datset inisde the data folder in whihc we have 2 sub folder for original image and ascii art for those images
import os
import os.path
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from torchvision import datasets, transforms
import random

#1st step: load images from a dataset and stoer them in the original_images folder with name img1,img2.....
#2nd step: convert images by using the main function of the Font_generator module and store them in the ascii_art folder with name img1,img2.....

class LoadImg: 
    def __init__(self,max_images=150):
        self.max_images = max_images
        self.original_images_dir='./original_images'
        self.ascii_art_dir='./ascii_art_images'
        # os.makedirs(self.original_images_dir, exist_ok=True)
        # os.makedirs(self.ascii_art_dir, exist_ok=True)
        # self.data = datasets.VOCDetection('.',year='2012', download=True, image_set='train')
    def save_images(self):
        for i, (img, _) in enumerate(random.sample(self.data, self.max_images)):
            if i >= self.max_images:
                break
            img.save(f'{self.original_images_dir}/img{i}.jpg','JPEG')
            
    def rename_images(self):
        images = sorted(os.listdir(self.original_images_dir))  
        
        for i, filename in enumerate(images):
            old_path = os.path.join(self.original_images_dir, filename)
            new_filename = f'img_{i + 1}.jpg'
            new_path = os.path.join(self.original_images_dir, new_filename)
            
            os.rename(old_path, new_path)
            print(f"Renamed {old_path} to {new_path}")
    def generate_ascii(self):
        images=os.listdir(self.original_images_dir)
    def process_img(self):
        # self.rename_images()
        self.generate_ascii()

if __name__== "__main__":
    loader=LoadImg()
    loader.process_img()
