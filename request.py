import base64
import pprint
import requests
import argparse

request_url = "http://127.0.0.1:8000/uploadfile/"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Fast API exposing Yolov5 model")
    parser.add_argument("--source", type=str)
    parser.add_argument("--save", type=str)
    opt = parser.parse_args()

    image = opt.source
    res_path = opt.save

    # Read Image
    with open(image, "rb") as f:
        image_data = f.read()


    response = requests.post(request_url, files={'file': image_data}).json()

    with open(res_path, 'wb') as f:
        img_bytes = base64.b64decode(response['image'])
        f.write(img_bytes)
    pprint.pprint(response['detections'])