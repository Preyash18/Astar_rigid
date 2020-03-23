import sys
sys.path.remove(sys.path[1])
import cv2
import numpy as np
from obstacle import Obstructions
import time
import argparse
from heapq import heappush, heappop
import math
import matplotlib.pyplot as plt

#dist_threshold = 1

STEP = int(input('Enter STEP size:'))


class PathFinder():
	def __init__(self, start, end, robotRadius, clearance):
		self.start = (start[1], start[0],start[2])
		self.end = (end[1], end[0])
		self.allNodes = []
		############### nodeID [0], pareent [1], node [2], cost [3]  ## For BFS
		# self.mainData = [[0, 0, self.start, 0]]
		############### cost , node  #### For Dijkstar
		self.Data = []
		self.allPose = [self.start]
		self.actionSet(self.start)
		self.possibleMove = len(self.actionset)
		self.temp = []
		self.obss = Obstructions(300,200, robotRadius, clearance)

		self.goalReach = False
		self.view = True
		self.finalGoalState = []
		self.trace = []
		self.showCounter = 0
		self.skipFrame = 1


		#self.dg = math.sqrt(abs(((action[0] - end [0])** 2) + ((action1[1] - end [1])** 2)))
	def vect(self,start, fig, ax, node):

		X0 = np.array((0))
		Y0 = np.array((0))
		U0 = np.array((2))
		V0 = np.array((-2))
		#fig, ax = plt.subplots()
		#q0 = ax.quiver(X0, Y0, U0, V0, units='xy', scale=1, color='r', headwidth=1, headlength=0)
		Node = [X0 + U0, Y0 + V0]
		print('Node0: ')
		print(Node)

		#straight
		x2, y2 = node[1], node[0]
		u2, v2 = tuple(np.subtract([x2, y2], [self.actionset[0][0], self.actionset[0][1]]))
		# U2 = np.array((self.end[0]))
		# V2 = np.array((self.end[1]))
		print(u2,v2)

		ax.quiver(x2, y2, u2, v2, units='xy', scale=1,color='r')
		Node2 = [x2 + u2, y2 + v2]
		print('Node2: ')
		print(Node2)

		#moveup1
		x3, y3 = node[1], node[0]
		u3, v3 = tuple(np.subtract([x3, y3], [self.actionset[1][0], self.actionset[1][1]]))
		# U2 = np.array((self.end[0]))
		# V2 = np.array((self.end[1]))
		ax.quiver(x3, y3, u3, v3, units='xy', scale=1)
		Node3 = [x3 + u3, y3 + v3]
		print('Node3: ')
		print(Node3)

		#moveup2
		x4, y4 = node[1], node[0]
		u4, v4 = tuple(np.subtract([x4, y4], [self.actionset[2][0], self.actionset[2][1]]))
		# U2 = np.array((self.end[0]))
		# V2 = np.array((self.end[1]))
		ax.quiver(x4, y4, u4, v4, units='xy', scale=1)
		Node4 = [x4 + u4, y4 + v4]
		print('Node4: ')
		print(Node4)

		# movedown1
		x5, y5 = node[1], node[0]
		u5, v5 = tuple(np.subtract([x5, y5], [self.actionset[3][0], self.actionset[3][1]]))
		# U2 = np.array((self.end[0]))
		# V2 = np.array((self.end[1]))
		ax.quiver(x5, y5, u5, v5, units='xy', scale=1)
		Node5 = [x5 + u5, y5 + v5]
		print('Node5: ')
		print(Node5)

		#movedown2
		x6, y6 = node[1], node[0]
		u6, v6 = tuple(np.subtract([x6, y6], [self.actionset[4][0], self.actionset[4][1]]))
		# U2 = np.array((self.end[0]))
		# V2 = np.array((self.end[1]))
		ax.quiver(x6, y6, u6, v6, units='xy', scale=1)
		Node6 = [x6 + u6, y6+ v6]
		print('Node6: ')
		print(Node6)



	def plot_arrow(self, node, parentnode, ax, color):
		ax.quiver(parentnode[1], parentnode[0], node[1]-parentnode[1], node[0]-parentnode[0], units='xy', scale=1, color=color)
		#Node6 = [x6 + u6, y6 + v6]


	def initialCheck(self):
		if not self.obss.checkFeasibility(self.start):
			print("Start node is in obstacle field. Please provide correct starting position.")
			return False
		elif not self.obss.checkFeasibility(self.end):
			print("Goal node is in obstacle field. Please provide correct goal position.")
			return False
		else:
			return True

	def actionSet(self, node):
		################# [ h,  w, cost]
		ang = 30
		#print('aaaaaa',start)
		#print('bbbbb', self.start)
		self.actionset = ([round(node[0] + STEP*math.sin(math.radians(node[2] + 0)), 2),round(node[1] + STEP*math.cos(math.radians(node[2] + 0)), 2), node[2]],      #straight

						  [round(node[0] + STEP*math.sin(math.radians(node[2] + ang)), 2), round(node[1] + STEP*math.cos(math.radians(node[2] + ang)),2), node[2] + ang],		#moveup1

						  [round(node[0] + STEP*math.sin(math.radians(node[2] + ang*2)), 2), round(node[1] + STEP*math.cos(math.radians(node[2] + ang*2)), 2), node[2] + ang * 2], #moveup2

						  [round(node[0] + STEP*math.sin(math.radians(node[2] - ang)), 2), round(node[1] +STEP* math.cos(math.radians(node[2] - ang )), 2),node[2] - ang],     #movedown1

						  [round(node[0] + STEP*math.sin(math.radians(node[2] - ang * 2)), 2),round(node[1] + STEP*math.cos(math.radians(node[2] - ang * 2)), 2), node[2] - ang * 2]  #movedown2
						 )
		pass

	def checkEnd(self, currentNode):
		return (((currentNode[0]-self.end[0])**2)+((currentNode[1]-self.end[1])**2)) <= 2.25


	def findNewPose(self, nodeState, action):
		tmp = nodeState[2]
		tmp = (tmp[0]+action[0], tmp[1]+action[1])
		return tmp

	def dijNewPose(self, node, action):
		tmp = (node[0]+action[0], node[1]+action[1], node[2]+ action[2])
		return tmp

	def viewer(self, num):
		self.showCounter += 1
		if self.showCounter%num == 0:
			cv2.imshow("Solver", self.obss.animationImage)
			#plt.show(self.obss.obstaclespace)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				self.view = False
		pass


	def trackBack(self, node, ax):
		path = [self.end]
		child = tuple(node)
		print("child",tuple(child), self.start)
		while child != self.start:
			#self.obss.path(tmp)
			parent = self.obss.getParent(child)
			#print("temp",temp)
			self.plot_arrow(child, parent, ax, 'b')
			tmp = (int(child[0]), int(child[1]))


			# print(tmp)
			path.append(tmp)

			print('parent', parent)
			child = parent
			#self.viewer(1)
		return


	def DijkstarSolve(self):
		fig, ax = plt.subplots()
		plt.grid()
		ax.set_aspect('equal')
		plt.xlim(0, 300)
		plt.ylim(0, 200)
		plt.title('How to plot a vector in matplotlib ?', fontsize=10)
		plt.savefig('how_to_plot_a_vector_in_matplotlib_fig3.png', bbox_inches='tight')

		heappush(self.Data, (0, self.start,0))
				#self.obss.astar(start, end)
		while len(self.Data) > 0:
			cost, node, costtocome = heappop(self.Data)
			print("cost",cost)
			if self.checkEnd(node):
				self.goalReach = True
				print("goal reached")
				self.trackBack(node, ax)
				break
				#return

			self.actionSet(node)
			for action in self.actionset:
				#self.dg = math.sqrt(abs(((action[0] - end[0]) ** 2) + ((action[1] - end[1]) ** 2)))
				newPose =  action
				#self.vect(newPose, fig, ax,newPose)
				#print("newpose",newPose)
				if self.obss.checkFeasibility(newPose):
					dg = math.sqrt(((newPose[0] - self.end[0]) ** 2) + ((newPose[1] - self.end[1]) ** 2))
					newCost = costtocome + 1

					#print("dg",self.dg)

					if self.obss.checkVisited(newPose):
						self.obss.addExplored(newPose)
						self.plot_arrow(newPose, node, ax, 'g')
						self.obss.addParent(newPose, node, newCost)
						heappush(self.Data, (newCost + dg, newPose, newCost))

					else:
						if self.obss.getCost(newPose) > newCost+dg :

							#self.obss.addExplored(newPose)
							self.obss.addParent(newPose, node, newCost)
					if self.view:
						pass
						#self.viewer(30)
		if self.goalReach:
			self.obss.showMap(ax)
			fig.show()
			plt.draw()
			plt.show()
		else:
			print("Could not find goal node...Leaving..!!")



		return

Parser = argparse.ArgumentParser()
Parser.add_argument('--Start', default="[51,31,60]", help='Give inital point')
Parser.add_argument('--End', default="[150,150]", help='Give inital point')
Parser.add_argument('--RobotRadius', default=1, help='Give inital point')
Parser.add_argument('--Clearance', default=1, help='Give inital point')
Parser.add_argument('--ShowAnimation', default=1, help='1 if want to show animation else 0')
Parser.add_argument('--Framerate', default=30, help='Will show next step after this many steps. Made for fast viewing')
Args = Parser.parse_args()

start = Args.Start
end = Args.End
r = int(Args.RobotRadius)
c = int(Args.Clearance)




start = [int(i) for i in start[1:-1].split(',')]
#start[1] = 200- start[1]
end = [int(i) for i in end[1:-1].split(',')] 
#end[1] = 200 - end[1]

solver = PathFinder(start, end, r, c)
solver.view = int(Args.ShowAnimation)
solver.skipFrame = int(Args.Framerate)

if solver.initialCheck():
	startTime = time.time()
	solver.DijkstarSolve()
	print(time.time() - startTime)
	print("Press (q) to exit")
	#solver.viewer(1)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
else:
	pass