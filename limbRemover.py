import Image
import numpy as np
import sunpy as sp

img = Image.open("sun.jpg") # Opens the specified image
pixels = img.load() # create the pixel map
midValue = [255,155,40]#pixels[512,512] #Currently hardcoded centre intensity values, RGB respectively
minValue = [166,56,4]	#Approximate intensity values at the limb, RGB respectively
test = pixels[510,52] #Not actually used
threshold = 30	#Threshold is the intensity value that will be used in the condition

#This was an attemt to make limb darkening coefficients, not used for now.
limbCoeffR = (midValue[0] - minValue[0]) / midValue[0]
limbCoeffG = (midValue[1] - minValue[1]) / midValue[1]
limbCoeffB = (midValue[2] - minValue[2]) / midValue[2]
print midValue[0]
print minValue
print limbCoeffR
for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
	value = pixels[i,j]	#Gets the intensity value of the current pixel
	if value[0] <= midValue[0] and value[1] > 20 and value[0] > 0:
		#print "Changing Value"
		val = value[1]
		if j > 30 and j < 994 and i > 30 and i < 994:
			if pixels[i+30,j][1] > val + threshold and pixels[i,j+30][1] > val + threshold and pixels[i-30,j][1] > val + threshold and pixels[i,j-30][1] > val + threshold:
				do = 1
			if do == 0:
				pixels[i,j] = (midValue[0], midValue[1], midValue[2]) # set the colour accordingly
	do = 0

img.show()
