import cv2

src = cv2.imread("src.jpg", cv2.IMREAD_COLOR)

W = 17
H = 6

inpormation = src.shape
height = inpormation[0]
width = inpormation[1]
print(height,width)
a = int(width/W)
a_1 = 0
b = int(height/H)
b_1 = 0
"""dst = src[0:a, 0:b]
cv2.imshow("src", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
for j in range(H):
    for i in range(W):
        roi = src[b_1:b, a_1:a]
        cv2.imwrite(f"image/{j}_{i}.jpg", roi)
        a_1 = a
        a += int(width / W)
    b_1 = b
    b += int(height / H)
    a_1 = 0
    a = int(width/W)


#print()