import cv2

src = cv2.imread("src.jpg", cv2.IMREAD_COLOR)

W = 11

inpormation = src.shape
height = inpormation[0]
width = inpormation[1]
print(height,width)
a = int(width/W)
a_1 = 0

for l in range(W):
    roi = src[0:height, a_1:a]
    dst = cv2.resize(roi, dsize=(120, 120), interpolation=cv2.INTER_AREA)
    for i in range(120):
        for j in range(120):
            if dst.item(i, j, 0) + dst.item(i, j, 1) + dst.item(i, j, 2) > 500:
                for m in range(3):
                    dst.itemset(i, j, m, 255)
            else:
                for m in range(3):
                    dst.itemset(i, j, m, 0)

    cv2.imwrite(f"crop_image/{l}.jpg", dst)
    a_1 = a
    a += int(width / W)