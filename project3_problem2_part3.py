import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
import os
from project3 import Project3

## Reading the images
classroom_img_0 = cv.imread('classroom_im0.png')
classroom_img_1 = cv.imread('classroom_im1.png')

## Converting the images to grayscale
classroom_img_0_gray = cv.cvtColor(classroom_img_0, cv.COLOR_BGR2GRAY)
classroom_img_1_gray = cv.cvtColor(classroom_img_1, cv.COLOR_BGR2GRAY)

## Referring to the calib text file, the following parameters are declared and values are assigned

## Part 2: Classroom
classroom_cam_0 = np.array([[1746.24,0,14.88],[0,1746.24,534.11],[0,0,1]])
classroom_cam_1 = np.array([[1746.24,0,14.88],[0,1746.24,534.11],[0,0,1]])
classroom_doffs=0
classroom_focal_length=classroom_cam_0[0,0]
classroom_baseline=678.37
classroom_width=1920
classroom_height=1080
classroom_ndisp=285
classroom_vmin=60
classroom_vmax=280
classroom_blocksize=3
classroom_mindisp=0
classroom_disp12MaxDiff=1
classroom_uniquenessRatio=10
classroom_depth_limit=18000

p3=Project3("classroom")

## Finding the fundamental matrix for classroom stereo problem
classroom_F,classroom_points1,classroom_points2=p3.Fundamental_Matrix(classroom_img_0_gray,classroom_img_1_gray)
print(classroom_F)

## Finding the Essential matrix for classroom stereo problem
classroom_E=p3.Essential_matrix(classroom_F,classroom_cam_0,classroom_cam_1)
print(classroom_E)

## Finding the R matrix and T vector for classroom stereo problem
classroom_R,classroom_T = p3.get_T_R(classroom_E,classroom_points1,classroom_points2)
print("The R matrix is: ",'\n',classroom_R,'\n')
print("The T matrix is: ",'\n',classroom_T,'\n')

## Finding the rectified images for classroom stereo problem
classroom_img1_rectified,classroom_img2_rectified,classroom_img1_rectified_draw,classroom_img2_rectified_draw,classroom_F_rectified,classroom_points1_rectified,classroom_points2_rectified = p3.do_rectification(classroom_points1,classroom_points2, classroom_img_0, classroom_img_1, classroom_F,classroom_cam_0,classroom_cam_1,classroom_R,classroom_T)

## Drawing the epipolar lines on the rectified images for classroom stereo problem
p3.draw_epilines(classroom_img1_rectified_draw,classroom_img2_rectified_draw,classroom_F_rectified,classroom_points1_rectified,classroom_points2_rectified)

## Computing the disparity map for classroom stereo problem
classroom_disparity_map=p3.get_disparity_map(classroom_img1_rectified,classroom_img2_rectified,classroom_ndisp,classroom_blocksize,classroom_mindisp,classroom_disp12MaxDiff,classroom_uniquenessRatio)

## Computing the depth map for classroom stereo problem
p3.get_depth_map(classroom_disparity_map,classroom_baseline,classroom_focal_length,classroom_depth_limit)