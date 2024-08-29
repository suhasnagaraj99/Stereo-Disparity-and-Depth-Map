# Stereo-Disparity-and-Depth-Map

## Project Description
This repository contains code for ENPM673 Project 3B - Getting Disparity and depth maps from stereo images

![alt text](https://github.com/suhasnagaraj99/Stereo-Disparity-and-Depth-Map/blob/main/Results/traproom_depth.jpg?raw=false)

![alt text](https://github.com/suhasnagaraj99/Stereo-Disparity-and-Depth-Map/blob/main/Results/storeroom_depth.jpg?raw=false)

![alt text](https://github.com/suhasnagaraj99/Stereo-Disparity-and-Depth-Map/blob/main/Results/classroom_depth.jpg?raw=false)

### Required Libraries
Before running the code, ensure that the following Python libraries are installed:

- `cv2`
- `numpy`
- `matplotlib`

You can install if they are not already installed:

```bash
sudo apt-get install python3-opencv python3-numpy python3-matplotlib
```

### Running the Code
Follow these steps to run the code:

1. Make sure the images `traproom_im0.png`,`traproom_im1.png`,`storeroom_im0.png`,`storeroom_im2.png`,`classroom_im0.png` and `classroom_im1.png` are pasted in the same directory as the `project3.py`, `project3_problem2_part1.py`, `project3_problem2_part1.py` and `project3_problem2_part1.py` files.
2. The file `project3.py` contains the main class and the required functions to get the output.
3. Files `project3_problem2_part1.py`, `project3_problem2_part1.py` and `project3_problem2_part1.py` are used to create an object of the class (`project3.py`) and use the functions to get the disparity and depth map.
4. Execute `project3_problem2_part1.py` file to get the outputs for traproom; run the following command in your terminal:
```bash
python3 project3_problem2_part1.py
```
5. Execute `project3_problem2_part2.py` file to get the outputs for storeroom; run the following command in your terminal:
```bash
python3 project3_problem2_part2.py
```
6. Execute `project3_problem2_part3.py` file to get the outputs for classroom; run the following command in your terminal:
```bash
python3 project3_problem2_part3.py
```
7. The disparitry and depth images are saved as the outputs
