from PIL import Image,ImageDraw,ImageFont
from argparse import ArgumentParser
import numpy as np
sample_Width=20
sample_Height=40
def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--img_path", help="Path to the image to be processed",required=True)
    return parser.parse_args()
char_lookup = [" ", ".", ",", ":", ";", "i", "1", "t", "f", "L", "C", "G", "0", "8", "#", "@"]
# def render_glyph(glyph):
    
def main(img_path):
    # print("Hello, World!",img_path)
    img=Image.open(img_path).convert(mode="L")
    img_array=np.array(img)
    ascii_art=[]
    # print(img_array[0:5,0:5])
    # print ("range doing what",range(img_array.shape[0]//sample_Height))
    # output=np.zeros((img_array.shape[0]//sample_Height,img_array.shape[1]//sample_Width))
    # Image segmentation breaking the image into  pixel chunks and then analyzing each chunk individually 
    for y in range(img_array.shape[0]//sample_Height):
        line = ""
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
            line += char_lookup[char_index]
            # print(output)
        ascii_art.append(line)
        
    print (len(ascii_art ))
    return ascii_art
    # print("new output shape",output.shape)
    # Image.fromarray(img_array).save("test.jpg")
def render_ascii_art(ascii_art, font_path, font_size, output_image_path):
    char_height = font_size
    char_width = int(font_size *0.5)
    print("ascii_art",ascii_art)
    img_height = len(ascii_art) * char_height
    print("img_height",img_height)
    img_width = len(ascii_art[0]) * char_width

    output_image = Image.new('L', (img_width, img_height), color=255)
    draw = ImageDraw.Draw(output_image)
    font = ImageFont.truetype(font_path, font_size)

    y_offset = 0
    for line in ascii_art:
        x_offset = 0
        for char in line:
            draw.text((x_offset, y_offset), char, font=font, fill=0)
            x_offset += char_width
        y_offset += char_height
    
    output_image.save(output_image_path)
    return output_image
    
if __name__ == "__main__":
    main(**vars(parse_args()))
    font_path = "C:/Windows/Fonts/Arial.ttf"  
    font_size = 12
    output_image_path = "./ascii_art_image.png"

    ascii_image = render_ascii_art(main(**vars(parse_args())), font_path, font_size, output_image_path)
    ascii_image.show()