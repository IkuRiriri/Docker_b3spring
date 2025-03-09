import cv2
import numpy as np
import os

def process_image(input_image_path, output_folder='output'):
    """
    Function to read a JPG image and apply grayscale conversion and edge detection
    
    Parameters:
    -----------
    input_image_path : str
        Path to the input image
    output_folder : str
        Folder to save the output images
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Load the image
    img = cv2.imread(input_image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Edge detection (Canny)
    edges = cv2.Canny(gray, 100, 200)
    
    # Save the images
    cv2.imwrite(f'{output_folder}/grayscale.jpg', gray)
    cv2.imwrite(f'{output_folder}/edges.jpg', edges)
    
    return img, gray, edges

if __name__ == "__main__":
    # Specify the path to the input image
    input_image = "input.jpg"
    
    try:
        results = process_image(input_image)
        print("Image processing completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")