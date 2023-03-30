#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

from matplotlib import pyplot as plot

image = cv2.imread('download.jpeg')

plot.hist(image.ravel(),256)
plot.show()


# In[ ]:




