from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

grey = np.array([[1,4,2,5],[5,7,2,6],[6,3,4,5],[9,5,6,1]])
#grey = np.array([np.amax(grey)-i for i in grey])

#First projection
p1 = np.zeros(len(grey))
for i in range(len(grey)):
	p1[i] = np.sum(grey[i])
p1_arr = [p1]*len(grey)
p1_arr = np.transpose(p1_arr)



#Second projection
p2 = np.zeros(len(grey)*2 - 1)
for i in range(len(grey)*2 -1):
	p2[i] = np.sum(grey.diagonal(i-(len(grey)-1))) * float(len(grey)) /float(len(grey.diagonal(i-(len(grey)-1))))

p2_arr = np.zeros([len(grey), len(grey)])
for i in range(len(p2_arr)):
	p2_arr[i] = p2[(len(p2)+1)/2-(i+1):len(p2)-i]


#plt.show()

#Third projection
p3 = np.zeros(len(grey))
for j in range(len(grey)):
	sum = 0
	for i in range(len(grey)):
		sum = sum + grey[i][j]
	p3[j] = sum

p3_arr = np.array([p3]*len(grey))
#plt.show()

#Fourth projection
grey2 = np.zeros([len(grey), len(grey)])

for i in range(len(grey2)):
	grey2[i] = grey[len(grey)-(1+i)]

p4 = np.zeros(len(grey2)*2 -1)
for i in range(len(grey2)*2 - 1):
	p4[i] = np.sum(grey2.diagonal(i-(len(grey2)-1))) * float(len(grey)) /float(len(grey.diagonal(i-(len(grey)-1))))

p4_arr = np.zeros([len(grey2), len(grey2)])
for i in range(len(p4_arr)):
	p4_arr[i] = p4[i:len(p4) - (len(p4)+1)/2 +1 + i]

projection_sum1 = np.add(p1_arr, p2_arr)
projection_sum2 = np.add(p3_arr, p4_arr)
projection_sum = np.add(projection_sum1, projection_sum2)

print grey
print p1_arr
print p2_arr
print p3_arr
print p4_arr
print projection_sum

plt.subplot(3, 2, 1)
plt.imshow(p1_arr, cmap = cm.Greys_r)

plt.subplot(3, 2, 2)
plt.imshow(p2_arr, cmap = cm.Greys_r)
plt.subplot(3, 2, 3)
plt.imshow(p3_arr, cmap = cm.Greys_r)
plt.subplot(3, 2, 4)
plt.imshow(p4_arr, cmap = cm.Greys_r)
plt.subplot(3, 2, 5)

plt.imshow(grey, cmap = cm.Greys_r)
plt.subplot(3, 2, 6)
plt.imshow(projection_sum, cmap = cm.Greys_r)
plt.show()
