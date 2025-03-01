import cv2

def analyse_image(sat_image_path: str, lidar_image_path: str) -> dict:
    """ Perform analysis on the given image data

    Args:
        sat_image_path (str): Path of sattelite image
        lidar_image_path (str): Path of LIDAR image

    Returns:
        dict: Results
    """
    
    # Load images into memory
    # Perform analyses
    # Check against thresholds
    pass


def percent_green(sat_image_path: str) -> float:
    pass


def average_elevation(lidar_image_path: str) -> float:
    pass


def percent_water(sat_image_path: str, lidar_image_path: str) -> float:
    pass


def edge_density(sat_image_path: str) -> float:
    pass


def percent_horizontal(sat_image_path: str) -> float:
    pass


def percent_vertical(sat_image_path: str) -> float:
    pass