from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import math

#Source for converting to greyscale from https://samarthbhargav.wordpress.com/2014/05/05/
#image-processing-with-python-rgb-to-grayscale-conversion/
def weightedAverage(pixel):
    return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]

def y_value(x, alpha, offset):
	return x * math.tan((90-alpha)*math.pi / 180) + offset

im = misc.imread('test_image.jpg')

grey = np.zeros((im.shape[0], im.shape[1]))

for rownum in range(len(im)):
	for colnum in range(len(im[rownum])):
		grey[rownum][colnum] = weightedAverage(im[rownum][colnum])

L = len(grey)


#Make it a square
if grey.shape[0] < grey.shape[1]:
	grey = grey[:, :grey.shape[0]]
else: 
	grey = grey[:grey.shape[1], :] 

#x = []
#y = []
#for i in range(0, 21):
#	x.append(i)
#	y.append(int(round(y_value(i, 20, 0))))

#x2=[]
#y2 = []
#for i in range(0, 21-int(round(5 * math.tan(20*math.pi / 180)))):
#	x2.append(i)
#	y2.append(int(round(y_value(i, 20, 5))))

#plt.scatter(x, y)
#plt.scatter(x2, y2)
#plt.show()


a = np.array([[4,5,6],[5,6,2],[5,2,5]])
L=len(a)
p = []
projection1 = []

#for offset in range(0, L):
#	print "offset", offset
#	for j in range(0, L-int(round(offset * math.tan(45*math.pi / 180)))):
#		print "x", len(a)-1-j
#		y = int(round(y_value(j, 45, offset)))
#		print "y", j
		#print "value", a[y][len(a)-1-j]
		#y_vals.append(a[j][y])
	#line_sum.append(sum(y_vals))

print a
for n in range(L):
	del p[:]
	for j in range(L):
		p.append(a[n][j])
	print p
#	print projection1

#for angles 45 to 90 degrees
for i in range(L):
	j = int(round(i / math.tan(90 * math.pi / 180)))
	print i
	print j
#for 0 to 45 degrees
for j in range(L):
	i = int(round(i * math.tan(20 * math.pi / 180)))
	print i
	print j
		

#picture = [[a[]]]

#print line_sum
#print len(line_sum)





