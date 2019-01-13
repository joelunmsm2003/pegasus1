import numpy
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = "/home/andy/pegasus/PetImages"
CATEGORIES=['Dog','Cat']

for category in CATEGORIES:
    path =os.path.join(DATADIR,category)
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
        plt.imshow(img_array,cmap='gray')
        plt.show()
        break
    break


print (img_array)

img_array.shape

IMG_SIZE=500
new_array=cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
plt.imshow(new_array,cmap='gray')
plt.show()
new_array.shape


training_data=[]
def create_training_data():
    for category in CATEGORIES:
        path =os.path.join(DATADIR,category)
        class_num=CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                new_array =cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
                training_data.append([new_array,class_num])
            except Exception as e:
                pass
        
create_training_data()