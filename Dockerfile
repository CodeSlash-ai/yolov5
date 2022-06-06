FROM python:3.8

RUN apt-get update && apt-get install -y libgl1

RUN pip install --upgrade pip

# COPY yolov5/requirements.txt /tmp
# RUN pip3 install -r ./tmp/requirements.txt

RUN pip3 install matplotlib>=3.2.2
RUN pip3 install numpy>=1.18.5
RUN pip3 install opencv-python>=4.1.1
RUN pip3 install Pillow>=7.1.2
RUN pip3 install PyYAML>=5.3.1
RUN pip3 install requests>=2.23.0
RUN pip3 install scipy>=1.4.1
RUN pip3 install torch>=1.7.0
RUN pip3 install torchvision>=0.8.1
RUN pip3 install tqdm>=4.41.0
RUN pip install protobuf==3.20.1
RUN pip3 install tensorboard>=2.4.1
RUN pip3 install pandas>=1.1.4
RUN pip3 install seaborn>=0.11.0
RUN pip3 install ipython
RUN pip3 install psutil
RUN pip3 install thop


COPY yolov5 yolov5
