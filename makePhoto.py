from PIL import Image

frame = (3060, 2040)
frame_width, frame_height = frame
네칸사진넓이 = 345
네칸사진높이 = 345
세칸사진높이 = 657


def threeCut(value, TOTALCNT, photo, photo2, photo3, color):
    print(f"{value}장 인쇄")
    backimg = Image.open(f"인생세컷프레임{color}.png")
    backimg = backimg.convert("RGB")

    # photo = Image.open("이나영배경.jpg")
    # photo2 = Image.open("원본사진.png")
    # photo3 = Image.open("숀고화질.jpg")

    backimg = backimg.convert("RGB")

    photo = photo.resize(frame, Image.LANCZOS)
    photo2 = photo2.resize(frame, Image.LANCZOS)
    photo3 = photo3.resize(frame, Image.LANCZOS)
    # photo4 = photo4.resize(frame, Image.LANCZOS)

    x_offset1 = 345
    y_offset1 = 세칸사진높이
    y_offset2 = y_offset1 * 2 + frame[1]
    y_offset3 = y_offset1 * 3 + frame[1] * 2
    # y_offset4 = y_offset1 * 4 + frame[1] * 3

    backimg.paste(photo, (x_offset1, y_offset1))
    backimg.paste(photo2, (x_offset1, y_offset2))
    backimg.paste(photo3, (x_offset1, y_offset3))
    # backimg.paste(photo4, (x_offset1, y_offset4))

    # 이미지를 크기를 조절하지 않고 그대로 저장
    backimg.save(f"결과이미지{TOTALCNT}.png", compression="raw", format="PNG")


def fourCut(value, arr, TOTALCNT):
    print(f"{value}장 인쇄")
    backimg = Image.open("인생네컷프레임검은색.png")
    backimg = backimg.convert("RGB")

    # photo = Image.open("이나영배경.jpg")
    # photo2 = Image.open("원본사진.png")
    # photo3 = Image.open("숀고화질.jpg")
    # photo4 = Image.open("숀고화질.jpg")

    photo = Image.open(f"{arr[0]}.jpg")
    photo2 = Image.open(f"{arr[1]}.jpg")
    photo3 = Image.open(f"{arr[2]}.jpg")
    photo4 = Image.open(f"{arr[3]}.jpg")

    backimg = backimg.convert("RGB")

    photo = photo.resize(frame, Image.LANCZOS)
    photo2 = photo2.resize(frame, Image.LANCZOS)
    photo3 = photo3.resize(frame, Image.LANCZOS)
    photo4 = photo4.resize(frame, Image.LANCZOS)

    x_offset1 = 345
    y_offset1 = 네칸사진높이
    y_offset2 = y_offset1 * 2 + frame[1]
    y_offset3 = y_offset1 * 3 + frame[1] * 2
    y_offset4 = y_offset1 * 4 + frame[1] * 3

    backimg.paste(photo, (x_offset1, y_offset1))
    backimg.paste(photo2, (x_offset1, y_offset2))
    backimg.paste(photo3, (x_offset1, y_offset3))
    backimg.paste(photo4, (x_offset1, y_offset4))

    # 이미지를 크기를 조절하지 않고 그대로 저장
    backimg.save(f"결과이미지{TOTALCNT}.png", compression="raw", format="PNG")
