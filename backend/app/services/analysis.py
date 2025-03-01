import cv2
import numpy as np
from ..main import log

def analyse_image(sat_image_path: str, lidar_image_path: str) -> dict:
    """ Perform analysis on the given image data

    Args:
        sat_image_path (str): Path of sattelite image
        lidar_image_path (str): Path of LIDAR image

    Returns:
        dict: Results
    """
    
    # Load images into memory
    sat_image: cv2.typing.MatLike = cv2.imread(sat_image_path)
    lidar_image: cv2.typing.MatLike = cv2.imread(lidar_image_path)

    # Check if images are loaded
    if sat_image is None:
        log.error("analyse_image", "Satellite image not loaded")
    if lidar_image is None:
        log.error("analyse_image", "LIDAR image not loaded")
        
    # Perform analyses
    # percent_green = percent_green(sat_image)
    # average_elevation = average_elevation(lidar_image)
    # percent_water = percent_water(sat_image, lidar_image)
    # edge_density = edge_density(sat_image)
    # percent_horizontal = percent_horizontal(sat_image)
    # percent_vertical = percent_vertical(sat_image)
    # Check against thresholds
    pass

def proportion_image_white(image: cv2.typing.MatLike) -> float:
    height, width = image.shape[:2]
    total_pixels = height * width
    count_white = np.count_nonzero(image)
    return count_white / total_pixels
 
def percent_green(sat_image: cv2.typing.MatLike):
    # Define the upper and lower HSV thresholds for green
    # Array (H,S,V)
    # https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv/48367205#48367205
    lower_green = (40, 100, 100)
    upper_green = (100, 255, 255)

    # Convert image
    image_hsv = cv2.cvtColor(sat_image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image_hsv, lower_green, upper_green)
    return proportion_image_white(mask)


def average_elevation(lidar_image_path: str) -> float:
    pass

def edge_density(sat_image: cv2.typing.MatLike) -> float:
    # Apply Canny edge detection to the satellite image
    edges: cv2.typing.MatLike = cv2.Canny(sat_image, 110, 180)
    # cv2.imshow("edges", edges);cv2.waitKey();cv2.destroyAllWindows()
    return proportion_image_white(edges)


def percent_horizontal(sat_image: cv2.typing.MatLike) -> float:
    # Transform the image to grayscale
    gray_image: cv2.typing.MatLike = cv2.cvtColor(sat_image, cv2.COLOR_BGR2GRAY)
    
    gray_image = cv2.bitwise_not(gray_image)
    bw: cv2.typing.MatLike = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                cv2.THRESH_BINARY, 15, -2)
    
    cols: int = bw.shape[1]
    horizontal_size: int = cols // 30
    horizontal_structure: cv2.typing.MatLike = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
    
    horizontal = cv2.erode(bw, horizontal_structure)
    horizontal = cv2.dilate(horizontal, horizontal_structure)

    cv2.imshow("horizontal", horizontal);cv2.waitKey();cv2.destroyAllWindows()
    return proportion_image_white(horizontal)

def percent_vertical(sat_image: cv2.typing.MatLike) -> float:
    # Transform the image to grayscale
    gray_image: cv2.typing.MatLike = cv2.cvtColor(sat_image, cv2.COLOR_BGR2GRAY)
    
    gray_image = cv2.bitwise_not(gray_image)
    bw: cv2.typing.MatLike = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                cv2.THRESH_BINARY, 15, -2)
    
    rows: int = bw.shape[0]
    vertical_size: int = rows // 30
    vertical_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (vertical_size, 1))
    
    vertical = cv2.erode(bw, vertical_structure)
    vertical = cv2.dilate(vertical, vertical_structure)
    return proportion_image_white(vertical)