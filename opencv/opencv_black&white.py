import cv2

W = 17
H = 6

for l in range(H):
    for k in range(W):
        img = cv2.imread(f"image/{l}_{k}.jpg", cv2.IMREAD_COLOR)

        dst = cv2.resize(img, dsize=(120, 120), interpolation=cv2.INTER_AREA)

        for i in range(120):
            for j in range(120):
                if dst.item(i, j, 0) + dst.item(i, j, 1) + dst.item(i, j, 2) > 500:
                    for m in range(3):
                        dst.itemset(i, j, m, 255)
                else:
                    for m in range(3):
                        dst.itemset(i, j, m, 0)

        cv2.imwrite(f"image/{l}_{k}.jpg", dst)




"""cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()"""