# MorseCode-Fingers
Communicate with your Machine using Morse Code (Finger Numeral Representations) 

## Demo 
[See the Working](https://youtu.be/k6iYVHb97zA)

## How Does It Work?
I made use of [Teachable Machine](https://teachablemachine.withgoogle.com/train/image) to train the image classification model with 3 classes (Finger Representation of 1, Finger Representation of  2, Blank Screen)

1 Represents Dot

2 Represents Dash

Once we move our hand out of the camera (Blank Screen), the respective alphabet or number for the pattern [Refer info.txt] will be displayed on the screen

My Model (keras_model.h5) works best only in plain background

You can Train your Model using Teachable Machine

## Requirements

Python3, OpenCV, Pillow, TensorFlow has to be installed
