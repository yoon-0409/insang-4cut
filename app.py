from flask import Flask, render_template, request, Response, redirect, url_for, jsonify
import os
import makePhoto
import json
import time
from PIL import Image
import cv2

app = Flask(__name__)

# 사용자 모델 클래스 정의

TOTALCNT = 0


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/count")
def cnt_page():
    return render_template("count.html")


@app.route("/fivesec", methods=["GET"])
def fiveSec():
    if request.method == "GET":
        global value
        value = request.args.get("count-input")
        value = [int(char) for char in value if char.isdigit()]
        value = value[0]
        print(f"count {(value)}")
    return render_template("fivesec.html")


@app.route("/camera")
def camera():
    return render_template("camera.html")


@app.route("/select")
def select():
    return render_template("select.html")


@app.route("/frame", methods=["GET", "POST"])
def frameSelect():
    if request.method == "POST":
        global arr
        arr = []
        data_json = request.form.get("selecarr")
        # JSON 데이터를 파이썬 리스트로 변환
        selecarr = json.loads(data_json)
        # print(selecarr)
        # selecarr 데이터를 사용하여 원하는 작업 수행
        if isinstance(selecarr, list):
            # selecarr가 리스트인 경우에만 처리
            for i in range(0, len(selecarr)):
                if selecarr[i]:
                    arr.append(i + 1)
                    print(f"{i} true")
                else:
                    print(f"{i} false")
        else:
            return render_template("frame.html")
    return render_template("frame.html")


def gen():
    """Video streaming generator function."""
    cap = cv2.VideoCapture(0)  # 0 is the number of the webcam

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            ret, jpeg = cv2.imencode(".jpg", frame)
            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n"
            )


@app.route("/video_feed")
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/takephoto", methods=["GET", "POST"])
def takePhoto():
    if request.method == "GET":
        print("촬칵")
    return render_template("takephoto.html")


@app.route("/printphoto")
def printphoto():
    return render_template("print.html")


@app.route("/makephoto", methods=["GET", "POST"])
def make():
    if request.method == "POST":
        print(f"{value}{arr}{TOTALCNT}인쇄")
        start = time.time()
        img1 = str(arr[0] + TOTALCNT).zfill(5)
        img2 = str(arr[1] + TOTALCNT).zfill(5)
        img3 = str(arr[2] + TOTALCNT).zfill(5)
        photo = Image.open(f"./img/test1/000/IMG_{img1}.jpg")
        photo2 = Image.open(f"./img/test1/000/IMG_{img2}.jpg")
        photo3 = Image.open(f"./img/test1/000/IMG_{img3}.jpg")
        request_data = request.get_json()
        color = request_data.get("color")
        makePhoto.threeCut(value, TOTALCNT, photo, photo2, photo3, color)
        end = time.time()
        print(end - start)
        print("done")
        return jsonify({"process": "done"})
    return render_template("makephoto.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
