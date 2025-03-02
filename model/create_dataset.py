import analysis
import csv
import os
import cv2

# https://www.kaggle.com/datasets/apollo2506/eurosat-dataset/data
# Model was trained on the RGB images from this dataset

# Mapping
# 0 Agri, 1 COuntry, 2 URban, 3 Water
labels = {"Agriculture":0, "Rural":1, "Urban":2, "Water":3}

for k,v in labels.items():
    for root, dirs, files in os.walk(f"./{k}"):
        category = v
        path = root.split(os.sep)
        for file in files:
            # Process image
            i = cv2.imread(os.path.join(*path)+os.sep+file)
            green = analysis.percent_green(i)
            edges = analysis.edge_density(i)
            horiz = analysis.percent_horizontal(i)
            vert = analysis.percent_vertical(i)
            with open("data.csv", "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([category, green, edges, horiz, vert])
