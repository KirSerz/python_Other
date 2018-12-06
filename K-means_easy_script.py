# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 14:34:51 2018

@author: Karter
"""

from PIL import Image, ImageDraw 
from skimage import io, color
import numpy as np
import math
import random


def CreateClaster(n):
    a=np.array([[random.random(),random.random(),random.random(),random.random()]])
    for i in range(0,n-1):
        a=np.append(a,[[random.random(),random.random(),random.random(),random.random()]], axis=0)
    return a

def KMeans(image,lab,clasters,kef1=0.5,kef2=0.1,metric=1):
    
    NormalMin1=np.min(image[:, :,1])    
    NormalMin2=np.min(image[:, :,2])
    NormalMax1=np.max(image[:, :,1])    
    NormalMax2=np.max(image[:, :,2])   
    tempClaster=np.copy(clasters)*0
    sizeByX,sizeByY,temp=image.shape
    D1=np.zeros((len(tempClaster))) 
    D1=D1.astype('float64')
    Error =np.array([ 0, 1 ])
    NumClasters=np.zeros((len(tempClaster)))   
    while(Error[0]!=Error[1]):       
        for i in range(0,sizeByX): 
            for j in range(0,sizeByY):               
                buffNormal1=(image[i][j][1]-NormalMin1)/(NormalMax1-NormalMin1) 
                buffNormal2=(image[i][j][2]-NormalMin2)/(NormalMax2-NormalMin2)
                distanceAfin=np.array([])
                for iterat in range(0,len(clasters)):
                    if (metric==1):
                        buff=math.sqrt(          pow(kef1*(buffNormal1 - clasters[iterat][0]), 2) 
                                                +pow(kef1*(buffNormal2 - clasters[iterat][1]), 2)
                                                +pow(kef2*((i/sizeByX) - clasters[iterat][2]), 2)
                                                +pow(kef2*((j/sizeByY) - clasters[iterat][3]), 2)
                                                )   
                    elif(metric==2):
                        buff=max(               abs(kef1*(buffNormal1 - clasters[iterat][0])),
                                                abs(kef1*(buffNormal2 - clasters[iterat][1])),
                                                abs(kef2*((i/sizeByX) - clasters[iterat][2])),
                                                abs(kef2*((j/sizeByY) - clasters[iterat][3]))
                                                )
                        
                    distanceAfin=np.append(distanceAfin, [buff])             
                for iterat in range(0,len(clasters)):
                    if ( distanceAfin[iterat] == np.min(distanceAfin)):                    
                            tempClaster[iterat][0]+=buffNormal1
                            tempClaster[iterat][1]+=buffNormal2
                            tempClaster[iterat][2]+=(i/sizeByX)
                            tempClaster[iterat][3]+=(j/sizeByY)
                            NumClasters[iterat]+=1
                            tempD1=pow(distanceAfin[iterat],2)
                            D1[iterat] =D1[iterat]+tempD1 
                            
                            lab2[i][j][0]=10*iterat
                            lab2[i][j][1]=10*iterat
                            lab2[i][j][2]=10*iterat

        for iterat in range(0,len(clasters)):
            if NumClasters[iterat]==0:
                NumClasters[iterat]=1
            clasters[iterat][0]=tempClaster[iterat][0]/NumClasters[iterat]
            clasters[iterat][1]=tempClaster[iterat][1]/NumClasters[iterat]
            clasters[iterat][2]=tempClaster[iterat][2]/NumClasters[iterat]
            clasters[iterat][3]=tempClaster[iterat][3]/NumClasters[iterat]
        tempClaster=tempClaster*0
        rgb=color.lab2rgb(lab2)
        io.imshow(rgb)
        io.show()
        Error[0] = Error[1]
        Error[1] = math.sqrt(np.sum(D1))
#        print(Error)
        NumClasters=NumClasters*0
        D1=D1*0;   
    return clasters

#rgb = io.imread("1111.jpg")
rgb = io.imread("test.jpg")
lab = color.rgb2lab(rgb)
lab2=np.copy(lab)
io.imshow(rgb)
io.show()
#print("введите коэффицент значимости цвета")
#k1=input()
#print("введите коэффицент значимости расположения")
#k2=input()



cl=CreateClaster(9)
claster=np.copy(cl)
x1=[1, 0]
x2=   [1, 0.25]
x3=   [1, 0.5]
x4=   [1, 0.75]
x5=   [1, 1]
x6=   [0.75, 1]
x7=   [0.5, 1]
x8=   [0.25, 1]
x0=   [1, 1]

 

#print("Новый круг \n","значения коэффицентов: ",x0[0]," ",x0[1])    
#ak=KMeans(lab,lab2,claster,x0[0],x0[1],1)


print("Новый круг \n","значения коэффицентов: ",x2[0]," ",x2[1])    
ak=KMeans(lab,lab2,claster,x2[0],x2[1],1)
    




