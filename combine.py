import os
import cv2
import numpy as np

base = cv2.imread("correct_image/test.png")


def double(mo_name, mo_path, ja_dir, mo_start, ja_start):
    """초성, 중성으로 구성된 음운 생성"""
    mo_unicode_name = str(mo_name.encode("unicode_escape")).replace(
        "b'\\\\u", "").replace("'", "")  # 유니코드 값

    ja_list = os.listdir(ja_dir)

    mo = cv2.imread(mo_path)  # 모음 불러오기
    mo_height, mo_width, _ = mo.shape  # 모음 픽셀 정보

    # 모음 합성 시작점 설정
    mo_height_start = mo_start[0]
    mo_width_start = mo_start[1]

    """모음의 전체 개수로 변경 예정"""
    for ja_filename in ja_list:
        base[mo_height_start:mo_height_start+mo_height,
             mo_width_start:mo_width_start+mo_width] = mo  # 모음 합성

        ja = cv2.imread(f"{ja_dir}/{ja_filename}")  # 자음 불러오기
        ja_height, ja_width, _ = ja.shape  # 자음 픽셀 정보

        # 자음 합성 시작점 설정
        ja_height_start = ja_start[0]
        ja_width_start = ja_start[1]

        base[ja_height_start:ja_height_start+ja_height,
             ja_width_start:ja_width_start+ja_width] = ja  # 자음 합성

        cv2.imshow("base", base)
        cv2.waitKey(0)

        base[:, :] = 255  # 베이스 초기화


def triple(mo_name, mo_path, ja1_dir, ja2_dir, mo_start, ja1_start, ja2_start):
    """초성, 중성, 종성으로 구성된 음운 생성"""
    mo_unicode_name = str(mo_name.encode("unicode_escape")).replace(
        "b'\\\\u", "").replace("'", "")  # 유니코드 값

    ja1_list = os.listdir(ja1_dir)  # 초성 이미지 목록
    ja2_list = os.listdir(ja2_dir)  # 종성 이미지 목록

    mo = cv2.imread(mo_path)  # 모음 불러오기
    mo_height, mo_width, _ = mo.shape  # 모음 픽셀 정보

    # 모음 합성 시작점 설정
    mo_height_start = mo_start[0]
    mo_width_start = mo_start[1]

    """모음의 전체 개수로 변경 예정"""
    for ja1_filename in ja1_list:
        for ja2_filename in ja2_list:
            base[mo_height_start:mo_height_start+mo_height,
                 mo_width_start:mo_width_start+mo_width] = mo  # 모음 합성

            ja1 = cv2.imread(f"{ja1_dir}/{ja1_filename}")  # 초성 불러오기
            ja1_height, ja1_width, _ = ja1.shape  # 초성 픽셀 정보

            # 초성 합성 시작점 설정
            ja1_height_start = ja1_start[0]
            ja1_width_start = ja1_start[1]

            base[ja1_height_start:ja1_height_start+ja1_height,
                 ja1_width_start:ja1_width_start+ja1_width] = ja1  # 초성 합성

            '''초성/종성 구분선'''

            ja2 = cv2.imread(f"{ja2_dir}/{ja2_filename}")  # 종성 불러오기
            ja2_height, ja2_width, _ = ja2.shape  # 종성 픽셀 정보

            # 종성 합성 시작점 설정
            ja2_height_start = ja2_start[0]
            ja2_width_start = ja2_start[1]

            base[ja2_height_start:ja2_height_start+ja2_height,
                 ja2_width_start:ja2_width_start+ja2_width] = ja2  # 종성 합성

            cv2.imshow("base", base)
            cv2.waitKey(0)

            base[:, :] = 255  # 베이스 초기화


double(mo_name="ㅏ", mo_path="glyph/mo/7.jpg",
       ja_dir="glyph/cho", mo_start=(75, 110), ja_start=(80, 60))
double(mo_name="ㅔ", mo_path="glyph/mo/8.jpg",
       ja_dir="glyph/cho", mo_start=(53, 110), ja_start=(80, 60))

triple(mo_name="ㅏ", mo_path="glyph/mo/7.jpg", ja1_dir="glyph/cho",
       ja2_dir="glyph/jong", mo_start=(55, 110), ja1_start=(60, 60), ja2_start=(130, 80))

cv2.destroyAllWindows()
