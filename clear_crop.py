import cv2
import os


def classify(unicode_str, img):
    """유니코드 값에 따라 초/중/종성으로 분류하여 저장"""
    table = {
        "ja1": ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ",
                "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"],
        "mo": ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
               "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"],
        "ja2": ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ",
                "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
    }

    if not os.path.exists("glyph"):
        os.mkdir("glyph")

    if not os.path.exists("glyph/cho"):
        os.mkdir("glyph/cho")

    if not os.path.exists("glyph/mo"):
        os.mkdir("glyph/mo")

    if not os.path.exists("glyph/jong"):
        os.mkdir("glyph/jong")

    glyph_name = bytes(
        "\\u" + unicode_str.lower(), "utf8").decode("unicode_escape")

    if glyph_name in table["ja1"] and glyph_name in table["ja2"]:
        # 초성과 종성 모두 쓰이는 자음
        cv2.imwrite(f"glyph/cho/{unicode_str}.png", img)
        cv2.imwrite(f"glyph/jong/{unicode_str}.png", img)
    elif glyph_name in table["ja1"]:
        # 초성으로만 쓰이는 자음
        cv2.imwrite(f"glyph/cho/{unicode_str}.png", img)
    elif glyph_name in table["ja2"]:
        # 종성으로만 쓰이는 자음
        cv2.imwrite(f"glyph/jong/{unicode_str}.png", img)
    else:
        # 모음
        cv2.imwrite(f"glyph/mo/{unicode_str}.png", img)


path, dirs, files = next(os.walk("aa"))

for file_name in files:
    img = cv2.imread(f"{path}/{file_name}", cv2.IMREAD_COLOR)
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

    unicode_str = file_name[:4]  # 파일명에서 유니코드 값만 추출
    classify(unicode_str, cropped_img)
