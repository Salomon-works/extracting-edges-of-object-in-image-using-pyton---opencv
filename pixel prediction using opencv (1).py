#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().system('pip install opencv-python')
get_ipython().system('pip install opencv-contrib-python')


# In[10]:


# to find x and y coordinates or pixel value on image 
import cv2 as cv
import numpy as num


# In[11]:


# just importing the image
img=cv.imread("C://Users//josep//Downloads//Web capture_24-7-2022_805_www.bing.com.jpeg")
# cv.imshow("image", img)
# cv.waitKey(0)
# cv.destroyAllWindows()


# In[13]:


# defining the functions to be act
def find_coord(event, x, y, flags,params):
    if event==cv.EVENT_FLAG_LBUTTON:
        # for the use of left mouse click
        print(x,',',y)
        # to define or print on the same image or windows
        font=cv.FONT_HERSHEY_PLAIN
        cv.putText(img,str(x) +','+ str(y), (x,y), font, 1,(255,0,0))
        # to show the text on the image itself
        cv.imshow("image", img)

if __name__=="__main__":
    # read and display the image
    img=cv.imread("C://Users//josep//Downloads//Web capture_24-7-2022_805_www.bing.com.jpeg")
    # display the image
    cv.imshow("image", img)
    # just calling back the functions
    cv.setMouseCallback("image", find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()
    


# In[ ]:





# In[ ]:




