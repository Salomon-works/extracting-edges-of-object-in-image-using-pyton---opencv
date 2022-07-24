#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install opencv-python')


# In[ ]:


import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt
img=cv.imread("C://Users//josep//Downloads//Web capture_24-7-2022_8711_www.bing.com.jpeg")


# In[ ]:


gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# In[ ]:


# cv.imshow('pic', gray)
# cv.waitKey(0)
# cv.destroyAllWindow()


# In[27]:


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




