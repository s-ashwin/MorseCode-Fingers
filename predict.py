import tensorflow.keras
from PIL import Image
import numpy as np
import cv2
import math
from itertools import groupby
a = []
str2=''
text=''
text_image = np.zeros((512, 512, 1), dtype = "uint8")

Dict = {"12":"A","2111":"B","2121":"C","211":"D","1":"E","1121":"F","221":"G","1111":"H","11":"I", "1222":"J","212":"K", "1211":"L","22":"M","21":"N","222":"O","1221":"P","2212":"Q","121":"R","111":"S","2":"T","112":"U","1112":"V", "122":"W","2112":"X","2122":"Y","2211":"Z","1222":"1","11222":"2","11122":"3","11112":"4","11111":"5","21111":"6","22111":"7","22211":"8","22221":"9","22222":"0"} #Morse codes for Alphabets and numbers

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

cap = cv2.VideoCapture(0)
#frameRate = cap.get(50)

while(True):
    #id = cap.get(10)
            ret, frame = cap.read()
            cv2.imshow('frame',frame)

    #if(id % math.floor(frameRate)==0) :
    

    # Make sure to resize all images to 224, 224 otherwise they won't fit in the array
            frame1 = cv2.resize(frame,(224, 224))
            image_array = np.asarray(frame1)

            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            # Load the image into the array
            data[0] = normalized_image_array

            # run the inference
            
            prediction = model.predict(data)
            #print(prediction)
            
            if (prediction[0][0] >= 0.90):
                print("one")
                a.append(1)
                
            elif (prediction[0][1] >= 0.90):
                print("two")
                a.append(2)
            elif(prediction[0][2] >= 0.90):
                print("none")
                #a = [x[0] for x in groupby(a)]
                #print(a)
                if(a!=[]):
                    text ="".join(map(str, a))
                    str1=Dict[text]
                    str2+=str1
                    a = []
                    cv2.putText(text_image, str2, (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 3.0, (255,210,65), 3, 1)
                    cv2.imshow('test', text_image)

            
            if cv2.waitKey(700) & 0xFF == ord('q'):
                break
    
cap.release()
cv2.destroyAllWindows()