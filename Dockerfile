FROM jeguzzi/ros:armhf-melodic-ros-dev
MAINTAINER Jerome Guzzi "jerome@idsia.ch"

RUN apt-get update && apt-get install -y \
    python-dev python-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install max7219

COPY . src/mt_led_matrix

RUN catkin build
