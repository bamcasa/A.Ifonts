import cv2

src = cv2.imread("src10.jpg", cv2.IMREAD_COLOR)

W = 11
H = 2

inpormation = src.shape
height = inpormation[0]
width = inpormation[1]
print(height,width)
a = int(width/W)
a_1 = 0
b = int(height/H)
b_1 = 0

for l in range(H):
    for k in range(W):
        roi = src[b_1:b, a_1:a]

        dst = cv2.resize(roi, dsize=(224, 224), interpolation=cv2.INTER_AREA)

        for i in range(224):
            for j in range(224):
                if dst.item(i, j, 0) + dst.item(i, j, 1) + dst.item(i, j, 2) > 400:
                    for m in range(3):
                        dst.itemset(i, j, m, 255)
                else:
                    for m in range(3):
                        dst.itemset(i, j, m, 0)

        cv2.imwrite(f"model_image/{l}_{k}.jpg", dst)
        a_1 = a
        a += int(width / W)
    b_1 = b
    b += int(height / H)
    a_1 = 0
    a = int(width/W)


