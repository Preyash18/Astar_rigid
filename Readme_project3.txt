
Group :- Ajinkya Parwekar and Preyash Parikh

Nodes are explored by A* algorithm and backtracking was applied with same giving the most optimal path and avoiding the obstacles.

The code is to be run in Python 3

There are two files name "Astar_rigid.py" and "obstacle.py"
"obstacle" file is imported to "Astar_rigid" file

1) Imported libraries :
     	-import numpy as np
     	-import matplotlib.pyplot as plt
     	-import time
     	-import math
     	-import cv2
	-import sys


2) User inputs :-  
     	- Step Size is asked to enter by user.


4) Rigid robot:- 
     	-Clearance of 'c' is given with the added clearance of radius of robot (r) making it total of r+c
     	-Predefined values of r and c is 1. 
     	-You can vary value of r and c by varying values at line number at 245 and 246 respectively. 
     	

5) Color:-
	- Blue color shows backtracking.
	- Green Color shows exploration.

6) Given Image:-
	- STEP size is 1
	- Start node is 50,30
	- Goal node is 150,150
	- Orientation is 60 Degree.

7) Start Node, Goal Node, Orientation
	- Start node can be changed from line 243 in "main.py" file.
	-Goal node can be changed from line 244 in "main.py" file
	-orientation can be changed from line 243 index 2 in "main.py" file
