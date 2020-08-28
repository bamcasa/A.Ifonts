import cv2
import os

import os

path, dirs, files = next(os.walk(f"{os.getcwd()}\\aa"))
time = len(files)


for k in range(time):
    img = cv2.imread(f"aa/{k}.jpg", cv2.IMREAD_COLOR)
    up = 0
    down = 0
    left = 0
    right = 0
    height, width, channel = img.shape
    for i in range(height):
        for j in range(width):
            # print(j)
            if img.item(i, j, 0) == 0:
                down = i
                break
    for i in range(height-1, 0, -1):
        for j in range(width):
            if img.item(i, j, 0) == 0:
                up = i
                break
    for i in range(width):
        for j in range(height):
            if img.item(j, i, 0) == 0:
                right = i
    for i in range(width-1, 0, -1):
        for j in range(height):
            if img.item(j, i, 0) == 0:
                left = i

    cropped_img = img[up: down, left: right]
    cv2.imwrite(f"aa\{k}.jpg", cropped_img)
