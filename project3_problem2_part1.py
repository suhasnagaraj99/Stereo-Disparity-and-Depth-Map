import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
import os
from project3 import Project3

## Reading the images
traproom_img_0 = cv.imread('traproom_im0.png')
traproom_img_1 = cv.imread('traproom_im1.png')

## Converting the images to grayscale
traproom_img_0_gray = cv.cvtColor(traproom_img_0, cv.COLOR_BGR2GRAY)
traproom_img_1_gray = cv.cvtColor(traproom_img_1, cv.COLOR_BGR2GRAY)

## Referring to the calib text file, the following parameters are declared and values are assigned

## Part 1: Traproom
traproom_cam_0 = np.array([[1769.02,0,1271.89],[0,1769.02,527.17],[0,0,1]])
traproom_cam_1 = np.array([[1769.02,0,1271.89],[0,1769.02,527.17],[0,0,1]])
traproom_doffs=0
traproom_focal_length=traproom_cam_0[0,0]
traproom_baseline=295.44
traproom_width=1920
traproom_height=1080
traproom_ndisp=140
traproom_vmin=25
traproom_vmax=118
traproom_blocksize=7
traproom_mindisp=0
traproom_disp12MaxDiff=1
traproom_uniquenessRatio=10
traproom_depth_limit=8000

p3=Project3("traproom")

## Finding the fundamental matrix for traproom stereo problem
traproom_F,traproom_points1,traproom_points2=p3.Fundamental_Matrix(traproom_img_0_gray,traproom_img_1_gray)
print(traproom_F)

## Finding the Essential matrix for traproom stereo problem
traproom_E=p3.Essential_matrix(traproom_F,traproom_cam_0,traproom_cam_1)
print(traproom_E)

## Finding the R matrix and T vector for traproom stereo problem
traproom_R,traproom_T = p3.get_T_R(traproom_E,traproom_points1,traproom_points2)
print("The R matrix is: ",'\n',traproom_R,'\n')
print("The T matrix is: ",'\n',traproom_T,'\n')

## Finding the rectified images for traproom stereo problem
traproom_img1_rectified,traproom_img2_rectified,traproom_img1_rectified_draw,traproom_img2_rectified_draw,traproom_F_rectified,traproom_points1_rectified,traproom_points2_rectified = p3.do_rectification(traproom_points1,traproom_points2, traproom_img_0, traproom_img_1, traproom_F,traproom_cam_0,traproom_cam_1,traproom_R,traproom_T)

## Drawing the epipolar lines on the rectified images for traproom stereo problem
p3.draw_epilines(traproom_img1_rectified_draw,traproom_img2_rectified_draw,traproom_F_rectified,traproom_points1_rectified,traproom_points2_rectified)

## Computing the disparity map for traproom stereo problem
traproom_disparity_map=p3.get_disparity_map(traproom_img1_rectified,traproom_img2_rectified,traproom_ndisp,traproom_blocksize,traproom_mindisp,traproom_disp12MaxDiff,traproom_uniquenessRatio)

## Computing the depth map for traproom stereo problem
p3.get_depth_map(traproom_disparity_map,traproom_baseline,traproom_focal_length,traproom_depth_limit)