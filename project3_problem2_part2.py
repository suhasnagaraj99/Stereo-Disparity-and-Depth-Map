import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
import os
from project3 import Project3

## Reading the images
storeroom_img_0 = cv.imread('storeroom_im0.png')
storeroom_img_1 = cv.imread('storeroom_im1.png')

## Converting the images to grayscale
storeroom_img_0_gray = cv.cvtColor(storeroom_img_0, cv.COLOR_BGR2GRAY)
storeroom_img_1_gray = cv.cvtColor(storeroom_img_1, cv.COLOR_BGR2GRAY)

## Referring to the calib text file, the following parameters are declared and values are assigned

## Part 2: storeroom
storeroom_cam_0 = np.array([[1742.11,0,804.90],[0,1742.11,541.22],[0,0,1]])
storeroom_cam_1 = np.array([[1742.11,0,804.90],[0,1742.11,541.22],[0,0,1]])
storeroom_doffs=0
storeroom_focal_length=storeroom_cam_0[0,0]
storeroom_baseline=221.76
storeroom_width=1920
storeroom_height=1080
storeroom_ndisp=80
storeroom_vmin=29
storeroom_vmax=61
storeroom_blocksize=3
storeroom_mindisp=0
storeroom_disp12MaxDiff=1
storeroom_uniquenessRatio=10
storeroom_depth_limit=5500

p3=Project3("storeroom")

## Finding the fundamental matrix for storeroom stereo problem
storeroom_F,storeroom_points1,storeroom_points2=p3.Fundamental_Matrix(storeroom_img_0_gray,storeroom_img_1_gray)
print(storeroom_F)

## Finding the Essential matrix for storeroom stereo problem
storeroom_E=p3.Essential_matrix(storeroom_F,storeroom_cam_0,storeroom_cam_1)
print(storeroom_E)

## Finding the R matrix and T vector for storeroom stereo problem
storeroom_R,storeroom_T = p3.get_T_R(storeroom_E,storeroom_points1,storeroom_points2)
print("The R matrix is: ",'\n',storeroom_R,'\n')
print("The T matrix is: ",'\n',storeroom_T,'\n')

## Finding the rectified images for storeroom stereo problem
storeroom_img1_rectified,storeroom_img2_rectified,storeroom_img1_rectified_draw,storeroom_img2_rectified_draw,storeroom_F_rectified,storeroom_points1_rectified,storeroom_points2_rectified = p3.do_rectification(storeroom_points1,storeroom_points2, storeroom_img_0, storeroom_img_1, storeroom_F,storeroom_cam_0,storeroom_cam_1,storeroom_R,storeroom_T)

## Drawing the epipolar lines on the rectified images for storeroom stereo problem
p3.draw_epilines(storeroom_img1_rectified_draw,storeroom_img2_rectified_draw,storeroom_F_rectified,storeroom_points1_rectified,storeroom_points2_rectified)

## Computing the disparity map for storeroom stereo problem
storeroom_disparity_map=p3.get_disparity_map(storeroom_img1_rectified,storeroom_img2_rectified,storeroom_ndisp,storeroom_blocksize,storeroom_mindisp,storeroom_disp12MaxDiff,storeroom_uniquenessRatio)

## Computing the depth map for storeroom stereo problem
p3.get_depth_map(storeroom_disparity_map,storeroom_baseline,storeroom_focal_length,storeroom_depth_limit)