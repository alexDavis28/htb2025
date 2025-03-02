import pickle
import cv2
import numpy as np
from .logs import log
from ..routers.validation import filestore
from matplotlib import pyplot as plt
from PIL import Image
import io

with open("app/data/model.pkl", "rb") as f:
    # Load the model
    # Predict: Category 0 Agricultural land 1 Countryside 2 Urban 3 Water
    # Features: Green percent, edge density, horizontal_percent, vertical_percent
    clf = pickle.load(f)


MatLike = cv2.typing.MatLike

def predict_with_model(green_percent: float, edge_density: float, horizontal_percent: float, vertical_percent: float) -> int:
    return int(clf.predict([[green_percent, edge_density, horizontal_percent, vertical_percent]])[0])

  
def proportion_image_white(image: MatLike) -> float:
    height, width = image.shape[:2]
    total_pixels = height * width
    count_white = np.count_nonzero(image)
    return count_white / total_pixels
 
def percent_green(sat_image: cv2.typing.MatLike) -> float:
    # Define the upper and lower HSV thresholds for green
    # Array (H,S,V)
    # https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv/48367205#48367205
    lower_green: MatLike= (40, 100, 100) # type: ignore
    upper_green: MatLike = (100, 255, 255) # type: ignore

    # Convert image
    image_hsv = cv2.cvtColor(sat_image, cv2.COLOR_BGR2HSV)
    mask: MatLike = cv2.inRange(image_hsv, lower_green, upper_green) 
    return proportion_image_white(mask)


def average_elevation(lidar_image_path: str) -> None:
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

    # cv2.imshow("horizontal", horizontal);cv2.waitKey();cv2.destroyAllWindows()
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



def analyse_image(sat_image_hash: str) -> list[float | str]:
    # Load images into memory
    
    # Get file
    file_data = filestore.get_file(sat_image_hash)
    if file_data is None:
        log.critical("analyse_image", "Failed to load file")
    nparr = np.fromstring(file_data, np.uint8) # type: ignore

    sat_image: cv2.typing.MatLike = cv2.imdecode(nparr, cv2.IMREAD_COLOR) # type: ignore
    # lidar_image: cv2.typing.MatLike = cv2.imread(lidar_image_path)

    # Check if images are loaded
    if sat_image is None:
        log.error("analyse_image", "Satellite image not loaded")
    # if lidar_image is None:
    #     log.error("analyse_image", "LIDAR image not loaded")
        
    
    # Retrieve model
    with open("app/data/model.pkl", "rb") as file:
        clf = pickle.load(file)

    # Split image into chunks
    chunks = []
    chunk_size = 30
    for i in range(0, sat_image.shape[0], chunk_size):
        row = []
        for j in range(0, sat_image.shape[1], chunk_size):
            row.append(sat_image[i:i+chunk_size, j:j+chunk_size])
        chunks.append(row)

    # Classify every chunk
    chunk_label_pairs = []
    for row in chunks:
        r = []
        for c in row:
            r.append((c, int(classify(c, clf)[0])))
            print(int(classify(c, clf)[0]))
        chunk_label_pairs.append(r)
    
    coloured_chunks = []
    for row in chunk_label_pairs:
        r = []
        for ch, l in row:
            r.append(color_chunk(ch, l))
        coloured_chunks.append(r)

    final = cv2.vconcat([cv2.hconcat(list_h)  
                        for list_h in coloured_chunks])
    final_2 = cv2.cvtColor(final, cv2.COLOR_BGR2RGB)
    final_pil = Image.fromarray(final_2)
    final_pil_byte_arr = io.BytesIO()
    final_pil.save(final_pil_byte_arr, format="PNG")
    final_pil_byte_arr = final_pil_byte_arr.getvalue()

    # Perform analyses
    green_percent = percent_green(sat_image)
    edge_density_stat = edge_density(sat_image)
    percent_horizontal_stat = percent_horizontal(sat_image)
    percent_vertical_stat = percent_vertical(sat_image)
    
    # Make prediction

    prediction = predict_with_model(green_percent, edge_density_stat, percent_horizontal_stat, percent_vertical_stat)
    print(prediction)
    mapping = {
        0: "Agricultural/farm",
        1: "Undeveloped/rural",
        2: "Developed/urban",
        3: "Water"
    }
    return {
        "category": mapping[prediction],
        "green": green_percent,
        "edge": edge_density_stat,
        "horizontal": percent_horizontal_stat,
        "vertical": percent_vertical_stat,
        "image": final_pil_byte_arr
    }


def classify(chunk: MatLike, clf) -> int:
    return clf.predict([[
        percent_green(chunk),
        edge_density(chunk),
        percent_horizontal(chunk),
        percent_vertical(chunk),
    ]])

def color_chunk(chunk: MatLike, label: int) -> MatLike:
    grey = cv2.applyColorMap(chunk, cv2.IMREAD_GRAYSCALE)
    match label:
        case 0:
            return cv2.applyColorMap(grey, get_mpl_colormap("Greens"))
        case 1:
            return cv2.applyColorMap(grey, get_mpl_colormap("Oranges"))
        case 2:
            return cv2.applyColorMap(grey, get_mpl_colormap("Reds"))
        case 3:
            return cv2.applyColorMap(grey, get_mpl_colormap("Blues"))
        case _:
            return grey

def get_mpl_colormap(cmap_name):
    cmap = plt.get_cmap(cmap_name)

    # Initialize the matplotlib color map
    sm = plt.cm.ScalarMappable(cmap=cmap)

    # Obtain linear color range
    color_range = sm.to_rgba(np.linspace(0, 1, 256), bytes=True)[:,2::-1]

    return color_range.reshape(256, 1, 3)

