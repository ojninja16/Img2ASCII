from PIL import Image
from argparse import ArgumentParser
import numpy as np
sample_Width=20
sample_Height=20
def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--img_path", help="Path to the image to be processed",required=True)
    return parser.parse_args()
char_lookup = [" ", ".", ":","a", "@"]
def main(img_path):
    # print("Hello, World!",img_path)
    img=Image.open(img_path).convert(mode="L")
    img_array=np.array(img)
    # print(img_array[0:5,0:5])
    # print ("range doing what",range(img_array.shape[0]//sample_Height))
    # output=np.zeros((img_array.shape[0]//sample_Height,img_array.shape[1]//sample_Width))
    # Image segmentation breaking the image into  pixel chunks and then analyzing each chunk individually 
    for y in range(img_array.shape[0]//sample_Height):
        for x in range(img_array.shape[1]//sample_Width):
            # output= np.mean(img_array[y*sample_Height:(y+1)*sample_Height,x*sample_Width:(x+1)*sample_Width])
            y_start=y*sample_Height
            y_end=y_start+sample_Height
            x_start=x*sample_Width
            x_end=x_start+sample_Width
            # print("what is exactly yhis")
            # slicing the image array into chunks
            chunk=img_array[y_start:y_end,x_start:x_end]
            # print(chunk)
            # getting the cummulative brightness of the chunk array
            brightness=np.sum(chunk)
            # print("brightness of the chunk",brightness)
            max_brightness=sample_Height*sample_Width*255
            normalized_brightness=brightness/max_brightness 
            char_index=int(round(normalized_brightness*(len(char_lookup)-1)))
            # print("char index of the chunk",char_index)
            print(char_lookup[char_index],end="")
            # print(output)
    # print("new output shape",output.shape)
    Image.fromarray(img_array).save("test.jpg")
    
if __name__ == "__main__":
    main(**vars(parse_args()))