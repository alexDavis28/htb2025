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


def percent_green(sat_image: cv2.typing.MatLike) -> float:
    # Define the upper and lower HSV thresholds for green
    # Array (H,S,V)
    # https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv/48367205#48367205
    lower_green = (35, 100, 20)
    upper_green = (70, 255, 255)

    # Convert image
    image_hsv = cv2.cvtColor(sat_image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image_hsv, lower_green, upper_green)
    cv2.imshow("green", mask);cv2.waitKey();cv2.destroyAllWindows()
    pass


def average_elevation(lidar_image_path: str) -> float:
    pass


def percent_water(sat_image_path: str, lidar_image_path: str) -> float:
    pass


def edge_density(sat_image: cv2.typing.MatLike) -> float:
    # Apply Canny edge detection to the satellite image
    edges: cv2.typing.MatLike = cv2.Canny(sat_image, 100, 200)

    # Pixels which are edges are marked as 1, all other pixels are marked as 0.
    edge_density: float = cv2.countNonZero(edges) / (sat_image.shape[0] * sat_image.shape[1])
    return edge_density


def percent_horizontal(sat_image: cv2.typing.MatLike) -> float:
    # Transform the image to grayscale
    gray_image = cv2.cvtColor(sat_image, cv2.COLOR_BGR2GRAY)
    
    gray_image = cv2.bitwise_not(gray_image)
    bw = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                cv2.THRESH_BINARY, 15, -2)
    
    cols: int = bw.shape[1]
    horizontal_size = cols // 30
    horizontal_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
    
    horizontal = cv2.erode(bw, horizontal_structure)
    horizontal = cv2.dilate(horizontal, horizontal_structure)

    percentage: float = cv2.countNonZero(horizontal) / (sat_image.shape[0] * sat_image.shape[1])
    return percentage

def percent_vertical(sat_image: cv2.typing.MatLike) -> float:
    # Transform the image to grayscale
    gray_image = cv2.cvtColor(sat_image, cv2.COLOR_BGR2GRAY)
    
    gray_image = cv2.bitwise_not(gray_image)
    bw = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                cv2.THRESH_BINARY, 15, -2)
    
    cols: int = bw.shape[1]
    horizontal_size = cols // 30
    horizontal_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
    
    horizontal = cv2.erode(bw, horizontal_structure)
    horizontal = cv2.dilate(horizontal, horizontal_structure)

    percentage: float = cv2.countNonZero(horizontal) / (sat_image.shape[0] * sat_image.shape[1])
    return percentage