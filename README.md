
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
  sudo docker run --name yolov5-docker-test1 -it --shm-size=1g -d --rm -v <absolute path to data>:/mydata yolov5-docker
```

**Note:** &nbsp; Don't forget the add the absolute path to your data directory.   
**Note:** &nbsp; *yolov5-docker-test1* and *mydata*&nbsp;are custom names. You can change them to whatever you like.

### Step 4

Running detection:
```bash
  sudo docker exec -it yolov5-docker-test1 python yolov5/detect.py --source mydata --project mydata --name results
```

If you have followed the steps correctly, there must be a new directory "results" in your data directory containing all of the results. 