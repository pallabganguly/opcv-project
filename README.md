# Detection of Open Hand using HAAR Cascades
## opcv-project
Detection of Hands using HAAR Cascades in OpenCV for UG Project
Souce code, classifiers and associated data for UnderGraduate Project. This repository deals with detection of open hand
using OpenCV 3.1.0 on Python 3.5. Data files are omitted for now

## Requirements: 
* OpenCV for Python 3.5
* numpy
* matplotlib

## Work done:
In this repository, we explore the effects of various parameters on accuracy of detection. For training, about 8000 samples were used, and for testing, about 3000. We then tweak:
1. Size of window
2. No of neighbours 
3. Image scaling
We run the classifier after changing the above parameters one at a time, on a test set to generate plots of accuracy versus the parameter in question.
If you want the data for re-training, please contact pallab.ganguly@kgec.edu.in

## To run:
There are scripts to generate plots of accuracy versus several parameters of HAAR classifier
Navigate to ./src and run python <filename>.py to run the respective script

## Results:
![GitHub Logo](/graphs/diffclassifier.png)
![GitHub Logo](/graphs/stages15thres70scale103.png)

### Note: This repository contains original research work done by the author. Please include proper citations when using any of the results obtained from this repository.
