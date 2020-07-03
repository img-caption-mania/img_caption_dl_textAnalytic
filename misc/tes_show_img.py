import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

img=mpimg.imread(os.getcwd() + '/bahdanau_attention.png')
imgplot = plt.imshow(img)
plt.show()
