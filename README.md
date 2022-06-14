
# How to: Build the Dockerfile and run predictions.

This readme will guide you through the process of building the docker container and running predictions on your own custom data.

### Step 1

Clone the repository:

```bash
  git clone https://github.com/CodeSlash-ai/yolov5.git
```
### Step 2

Build the docker image:
```bash
  sudo docker build -t yolov5-docker .
```

**Note:** &nbsp; *yolov5-docker* &nbsp;is a custom name. You can change it to whatever you like.

### Step 3

Create the docker container:
```bash
  sudo docker run --name yolov5-docker-test1 -p 8000:8000 yolov5-docker
```
   
**Note:** &nbsp; *yolov5-docker-test1* &nbsp;is a custom names. You can change it to whatever you like.

### Step 4

Running detection:
```bash
  python3 request.py --source <path to image> --save <path to save>
```

Example:
```bash
  python3 request.py --source data/image1.jpg --save results/res1.jpg
```

If you have followed the steps correctly, there must be a new directory "results" in your home directory containing the image with predictions. You will also get predictions in your terminal.  