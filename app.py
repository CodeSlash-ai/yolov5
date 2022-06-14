import uvicorn
from fastapi import FastAPI, File, UploadFile, Depends
import shutil
import torch
from pydantic import BaseModel
from fastapi_health import health
from PIL import Image
from io import BytesIO
import base64
import pathlib


class Result(BaseModel):
    image: str
    detections: list

def get_session():
    return {"detector": "online"}

def is_detector_online(session: bool = Depends(get_session)):
    return session


# init app
app = FastAPI()

#Routes
@app.get('/')
async def index():
    return {"text": "Hello World"}

# @app.post("/uploadfile/")
@app.post("/uploadfile/", response_model=Result)
async def create_upload_file(file: UploadFile = File(...)):


    # Creating a temp directory to store the data recieved from the client
    p = pathlib.Path('temp/')
    p.mkdir(parents=True, exist_ok=True)


    # Reading the filestream from the client and saving it in a temporary file
    with open(f'temp/{file.filename}.jpg', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    #Loading the YOLOv5 Model
    model = torch.hub.load('yolov5', 'custom', path='yolov5/yolov5s.pt', source='local', _verbose=False)  # local repo

    # Running predictions
    results = model(f'temp/{file.filename}.jpg')

    # Deleting the file created
    file_to_be_removed = pathlib.Path(f'temp/{file.filename}.jpg')
    file_to_be_removed.unlink(missing_ok=True)

    #Deleting the temp directory created
    p.rmdir()


    # Encoding the resultant image with boxes and labels
    results.imgs # array of original images (as np array) passed to model for inference
    results.render()  # updates results.imgs with boxes and labels
    for im in results.imgs:
        buffered = BytesIO()
        im_base64 = Image.fromarray(im)
        im_base64.save(buffered, format="JPEG")
        res_img = base64.b64encode(buffered.getvalue()).decode('utf-8')  # base64 encoded image with results
    

    # Saving the detections
    res_detections = results.pandas().xyxy[0].to_dict(orient='records')

    # Returning the JSON including the encoded image and the detections
    return Result(image=res_img, detections=res_detections)

app.add_api_route("/health", health([is_detector_online]))


