import cv2
import os
img_path = "./hyang_video5_5.jpg"
ann_path = "./hyang_video5_5.txt"

img = cv2.imread(img_path)

f=open(ann_path)
os.system("identify reference.jpg > temp.txt")
f1 = open("temp.txt","r")
dim = (f1.readline().split(' ')[2]).split('x')
dim_x,dim_y = float(dim[0]),float(dim[1])
os.system("rm temp.txt")

dictionary = {0:"Pedestrian", 1:"Biker", 2:"Bus", 3:"Car",4:"Skater",5:"Cart"}

for line in f:
	temp = line.split(' ')
	temp[-1] = (temp[-1])[:-1]
	lab = int(temp[0])
	temp = [float(i) for i in temp]
	x_min = int(dim_x*(temp[1]-(temp[3]/2)))
	y_min = int(dim_y*(temp[2]-(temp[4]/2)))
	x_max = int(dim_x*(temp[1]+(temp[3]/2)))
	y_max = int(dim_y*(temp[2]+(temp[4]/2)))
	cv2.rectangle(img,(x_min,y_min),(x_max,y_max),(0,0,255),2)
	cv2.putText(img,dictionary[lab],(x_min,y_min+4),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),1)

cv2.imshow("heading",img)
cv2.waitKey(0)
cv2.destroyAllWindows()