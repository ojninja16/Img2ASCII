import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--img_path", help="Path to the image to be processed", required=True)
    return parser.parse_args()

# Extended ASCII character set for better gradation
char_lookup = ' .`^",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'[::-1]

def preprocess_image(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    return img

def pixel_to_ascii(pixel_value):
    index = int((pixel_value / 255.0) * (len(char_lookup) - 1))
    return char_lookup[index]

def main(img_path):
    img_array = preprocess_image(img_path)
    height, width = img_array.shape
    
    ascii_art = []
    for y in range(height):
        line = ''.join(pixel_to_ascii(img_array[y, x]) for x in range(width))
        ascii_art.append(line)
    
    return ascii_art, img_array.shape

def render_ascii_art(ascii_art, original_shape, output_image_path):
    height = len(ascii_art)
    width = len(ascii_art[0])
    
    # Define the font path and size
    font_path = "C:/Windows/Fonts/consola.ttf"  # Example path to a fixed-width font
    font_size = 12
    
    # Calculate the width and height of each character in the selected font
    dummy_img = Image.new('L', (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    font = ImageFont.truetype(font_path, font_size)
    char_width, char_height = int(font_size *.6),font_size
    
    # Create a new image with white background
    output_image = Image.new('L', (width * char_width, height * char_height), color=255)
    draw = ImageDraw.Draw(output_image)
    
    # Draw each character onto the image
    y_offset = 0
    for line in ascii_art:
        draw.text((0, y_offset), line, font=font, fill=0)
        y_offset += char_height
    
    # Resize the image to the original dimensions while preserving the aspect ratio
    output_image = output_image.resize(original_shape[::-1], Image.LANCZOS)
    output_image.save(output_image_path)
    return output_image

if __name__ == "__main__":
    args = parse_args()
    
    # Define the output image path
    output_image_path = "./ascii_art_image.png"
    
    ascii_art, original_shape = main(args.img_path)
    ascii_image = render_ascii_art(ascii_art, original_shape, output_image_path)
    ascii_image.show()
    
    print(f"Original image shape: {original_shape}")
    print(f"ASCII art dimensions: {len(ascii_art)} rows, {len(ascii_art[0])} columns")
    
    # Print a small sample of ASCII art to console
    print("\nSample of ASCII art (first 40x40 characters):")
    for line in ascii_art[:40]:
        print(line[:40])
