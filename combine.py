import cv2
import numpy as np




text = "abcdefghijk"

img = np.zeros((3,3) ,dtype=object)
img_info = np.zeros((3,3) ,dtype=object)


for j in range(3):
    for i in range(3):
        if j == 0 and i == 2 or j == 2 and i == 2:
            break
        print(f"{text[j]}_{i}")
        img[j][i] = cv2.imread(f"correct_image/{text[j]}_{i}.jpg", cv2.IMREAD_COLOR)
        img_info[j][i] = img[j][i].shape[0]


base = cv2.imread("correct_image/test.png")
rows, cols, channels = base.shape

base[75:img_info[0][0] + 75, 80:img_info[0][0] + 80] = img[0][0]
#base[75:img_info[0][1] + 75, 20:img_info[0][1] + 20] = img[0][1]
#base[75:img_info[2][0] + 75, 20:img_info[2][0] + 20] = img[2][0]
base[75:img_info[1][2] + 75, 20:img_info[1][2] + 20] = img[1][2]

cv2.imshow("base", base)
cv2.waitKey(0)
cv2.destroyAllWindows()










