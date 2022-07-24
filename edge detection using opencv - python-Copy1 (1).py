#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install opencv-python')


# In[2]:


# libraries to import
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt
# to read the particular image
img=cv.imread("C://Users//josep//Downloads//Web capture_24-7-2022_8711_www.bing.com.jpeg")


# In[3]:


# just converting the image into gray scale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# In[4]:


# display the gray scale image
# cv.imshow('pic', gray)
# cv.waitKey(0)
# cv.destroyAllWindow()


# In[ ]:


# perform the canny edge detector to detect image edges
edges=cv.Canny(gray, threshold1=20, threshold2=70)
# for better edges detection can change the 
#these threshold values again and again, we can try here lets see
cv.imshow('results', edges)
cv.imshow('orginal_image', img)
cv.waitKey(0)
cv.destroyAllWindow()


# In[ ]:





# In[ ]:




