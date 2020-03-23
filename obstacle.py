import matplotlib.pyplot as plt
import numpy as np
import math




class Obstructions():
    def __init__(self, width, height, r, c):
        self.W = width +1
        self.H = height +1
        self.r = r
        self.c = c
        self.x_obs = []
        self.y_obs = []
        self.showObstacle = False
        # self.map = np.zeros([self.H, self.W], dtype=np.int8)
        self.obstaclespace = []
        self.animationImage = np.zeros([self.H, self.W, 3])
        self.generateMap()
        #self.showMap()
        self.r = 0
        self.c = 0
        self.showObstacle = True
        self.generateMap()
        self.explored = np.zeros([self.H, self.W, 12], dtype=np.int8) #self.obstaclespace.copy()
        self.parentData = np.zeros([self.H, self.W, 12, 4])
        self.dist_threshold = 1
        self.visited_matrix = np.zeros([int(300 / self.dist_threshold), int(200 /self. dist_threshold), 12])
        pass

    def generateMap(self):
        self.circle((225, 150), 25)
        self.ellipse((150, 100), 20, 40)
        #self.quad1((25, 200-15), (75, 200-15), (50, 200-50), (20, 200-80), (100, 200-50))
        #self.quad2((75, 200-15), (100, 200-50), (75, 200-80), (50, 200-50), (25, 200-15))
        #self.quad3((225, 200-160), (250, 200-175), (225, 200-190), (200, 200-175))
        self.quad1()
        self.quad2()
        self.quad3()
        self.quad4()
        self.border()
        pass

    def circle(self, center, radius):
        center_x, center_y = center[0], center[1]
        for i in range(center_x - (radius + self.r + self.c), center_x + (radius + self.r + self.c)):
            for j in range(center_y - (radius + self.r + self.c), center_y + (radius + self.r + self.c)):
                if ((i - center_x) ** 2 + (j - center_y) ** 2) <= (radius + self.r + self.c) ** 2:
                    if not self.showObstacle:
                        self.obstaclespace.append([i, j])
                    else:
                       # self.animationImage[j,i] = np.array([255,255,255])
                        self.animationImage[j,i] = np.array([255,255,255])

        return

    def check_circle(self, center, radius,i,j):
        center_x, center_y = center[0], center[1]
       # for i in range(center_x - (radius + self.r + self.c), center_x + (radius + self.r + self.c)):
        #    for j in range(center_y - (radius + self.r + self.c), center_y + (radius + self.r + self.c)):
        if ((i - center_x) ** 2 + (j - center_y) ** 2) <= (radius + self.r + self.c) ** 2:
            return True
        else:
            return False



    def ellipse(self, center, semiminor, semimajor):
        center_x, center_y = center[0], center[1]
        for i in range(center_x - (semimajor + self.r + self.c), center_x + (semimajor + self.r + self.c)):
            for j in range(center_y - (semiminor + self.r + self.c), center_y + (semiminor + self.r + self.c)):
                if (((i - center_x) / (semimajor + self.r + self.c)) ** 2 + ((j - center_y) / (semiminor + self.r + self.c)) ** 2) <= 1:
                    if not self.showObstacle:
                        self.obstaclespace.append([i, j])
                    else:
                       # self.animationImage.append([j, i])
                        #self.animationImage[j,i] = np.array([255,255,255])
                        pass
        return


    def check_ellipse(self, center, semiminor, semimajor,i,j):
        center_x, center_y = center[0], center[1]
       # for i in range(center_x - (semimajor + self.r + self.c), center_x + (semimajor + self.r + self.c)):
        #    for j in range(center_y - (semiminor + self.r + self.c), center_y + (semiminor + self.r + self.c)):
        if (((i - center_x) / (semimajor + self.r + self.c)) ** 2 + ((j - center_y) / (semiminor + self.r + self.c)) ** 2) <= 1:
            return True
        else:
            return False

    def quad1(self):
        for i in range(0, 301):
            for j in range(0, 201):
                if (j - 185 - (self.r + self.c) <= 0) and (5 * j + 7 * i - 5 * (290 + (self.r + self.c)) <= 0) and \
                        (5 * j - 6 * i - 5 * (30 - (self.r + self.c)) >= 0) and (
                        5 * j + 6 * i - 5 * (210 - (self.r + self.c)) >= 0) and \
                        (5 * j + 7 * i - 5 * (220 - (self.r + self.c)) >= 0):
                    if not self.showObstacle:
                        self.obstaclespace.append([i, j])
                    else:
                        self.animationImage[j, i] = np.array([255, 255, 255])



    def check_quad1(self,i,j):
        if (j - 185 - (self.r + self.c) <= 0) and (5 * j + 7 * i - 5 * (290 + (self.r + self.c)) <= 0) and \
                (5 * j - 6 * i - 5 * (30 - (self.r + self.c)) >= 0) and (
                5 * j + 6 * i - 5 * (210 - (self.r + self.c)) >= 0) and \
                (5 * j + 7 * i - 5 * (220 - (self.r + self.c)) >= 0):
            return True
        else:
            return False





    def quad2(self):
        for i in range(0, 301):
            for j in range(0, 201):
                if (j <= 13 * i - 140 + (self.r+self.c)) and (j - i - 100 + (self.r+self.c) >= 0) and \
                        (5 * j + 7 * i - 5 * 220 <= 0):
                    #obstacle_space.append([x, y])
                    if not self.showObstacle:
                        self.obstaclespace.append([i, j])
                    else:
                        self.animationImage[j,i] = np.array([255,255,255])
        return

    def check_quad2(self,i,j):


        if (j <= 13 * i - 140 + (self.r + self.c)) and (j - i - 100 + (self.r + self.c) >= 0) and \
            (5 * j + 7 * i - 5 * 220 <= 0):
            return True
        else:
            return False


    def quad3(self):
            for i in range(0, 301):
                for j in range(0, 201):
                    if (5 * j - 3 * i + 5 * (95 - (self.r + self.c)) <= 0) and (5 * j + 3 * i - 5 * (175 + self.r + self.c) <= 0) and \
                            (5 * j - 3 * i + 5 * (125 + self.r + self.c) >= 0) and (5 * j + 3 * i - 5 * (145 - self.r + self.c) >= 0):
                        if not self.showObstacle:
                            self.obstaclespace.append([i, j])
                        else:
                            self.animationImage[j,i] = np.array([255,255,255])
            return

    def check_quad3(self,i,j):

        if (5 * j - 3 * i + 5 * (95 - (self.r + self.c)) <= 0) and (5 * j + 3 * i - 5 * (175 + self.r + self.c) <= 0) and \
                (5 * j - 3 * i + 5 * (125 + self.r + self.c) >= 0) and (5 * j + 3 * i - 5 * (145 - self.r + self.c) >= 0):
            return True
        else:
            return False




    def quad4(self):
        for i in range(0, 301):
            for j in range(0, 201):
                if (5 * j - 9 * i - 5 * (13 + self.r + self.c) <= 0) and (65 * j + 37 * i - 5 * 1247 - 65 * (self.r + self.c) <= 0) and \
                        (5 * j - 9 * i + 5 * (141 + self.r + self.c) >= 0) and (65 * j + 37 *i - 5 * 1093 + 65 * (self.r + self.c) >= 0):
                    if not self.showObstacle:
                        self.obstaclespace.append([i, j])
                    else:
                        self.animationImage[j,i] = np.array([255,255,255])
        return

    def check_quad4(self,i,j):

        if (5 * j - 9 * i - 5 * (13 + self.r + self.c) <= 0) and (65 * j + 37 * i - 5 * 1247 - 65 * (self.r + self.c) <= 0) and \
                (5 * j - 9 * i + 5 * (141 + self.r + self.c) >= 0) and (65 * j + 37 *i - 5 * 1093 + 65 * (self.r + self.c) >= 0):
            return True
        else:
            return False


    def border(self):
        for i in range(0, 300):
            for j in range(0, 0 + self.r + self.c):
                if not self.showObstacle:
                    self.obstaclespace.append([i, j])
                else:
                    self.animationImage[j,i] = np.array([255,255,255])
        for i in range(0, 300):
            for j in range(200 - self.r - self.c, 200):
                if not self.showObstacle:
                    self.obstaclespace.append([i, j])
                else:
                    self.animationImage[j,i] = np.array([255,255,255])
        for i in range(0, 0 + self.r + self.c):
            for j in range(0, 200):
                if not self.showObstacle:
                    self.obstaclespace.append([i, j])
                else:
                    self.animationImage[j,i] = np.array([255,255,255])
        for i in range(300 - self.r - self.c, 300):
            for j in range(0, 200):
                if not self.showObstacle:
                    self.obstaclespace.append([i, j])
                else:
                    self.animationImage[j,i] = np.array([255,255,255])
        pass
    def check_border(self,i,j):
        total = self.r +self.c
        if 0 <= i < total or 300-total<i<=300 or 0<=j<total or 200-total<j<=200:
            return True
        else:
            return False

    def showMap(self, ax):
        # plt.imshow(self.map, cmap="gray")

        obstaclespace = np.array(self.obstaclespace)
        self.x_obs = [col[0] for col in self.obstaclespace]
        self.y_obs = [col[1] for col in self.obstaclespace]

        ax.scatter(self.x_obs, self.y_obs, c='r')
        #plt.axis([0, 300, 0, 200])
        #plt.show()

    def checkallobstacle(self,i,j):
        if self.check_circle((225,200-50),25,i,j):
            return True
        elif self.check_ellipse((150,200-100),20,40,i,j):
            return True
        elif self.check_quad1(i,j):
            return True
        elif self.check_quad2(i,j):
            return True
        elif self.check_quad3(i, j):
            return True
        elif self.check_quad4(i, j):
            return True
        elif self.check_border(i, j):
            return True
        else:
            return False

    def checkFeasibility(self, node):
        h, w = node[0], node[1]
        if h >= self.H or w >= self.W or h < 0 or w < 0:
            return False
        ##elif [h, w] in self.obstaclespace:
        #    return False
        #else:
         #   return True
        elif self.checkallobstacle(w,h):
            return False
        else:
            return True



    def intersection(self, node1, node2, line, range1, range2):
        x, y = node1[0], node1[1]
        u, v = node2[0], node2[2]
        a1 = v - y
        b1 = u - x
        c1 = a1*x + b1*u
        a2, b2, c2 = line[0], line[1], line[2]
        A = np.array([[a1, b1], [a2, b2]])
        B = np.array([c1, c2])
        C = np.linalg.solve(A, B)
        p, q = C[0], C[1]
        if range1[0] < p < range1[1] and range2[0] < q < range2[1]:
            return False
        else:
            return True

  #  def checkVisited(self, node):
   #     if self.explored[node[0], node[1]] == 1:
   #         return False
   #     else:
   #         return True

    def checkVisited(self,node):
        if node[0] % 1 > self.dist_threshold / 2:
            i = int(math.ceil(node[0]) / self.dist_threshold)               #uppervalue
        else:
            i = int(math.floor(node[0]) / self.dist_threshold)

        if node[1] % 1 > self.dist_threshold / 2:                           #lower value
            j = int(math.ceil(node[1]) / self.dist_threshold)
        else:
            j = int(math.floor(node[1]) / self.dist_threshold)
        i = 200 if i > 200 else i
        j = 300 if j > 300 else j
        m = node[1]
        ###for K, changed with 30 degrees.
        if m >= 360:
            m = m % 360
        if 15 < m <= 45 or -345 <= m < -315:
            k = 1
        elif 45 < m <=75 or -315 <= m <-285:
            k =2
        elif 75 < m <= 105 or -285 <= m < -255:
            k = 3
        elif 105 < m <= 135 or -255 <= m < -225:
            k = 4
        elif 135 < m <= 165 or -225 <= m < -195:
            k = 5
        elif 165 < m <= 195 or -195 <= m < -165:
            k = 6
        elif 195 < m <= 225 or -165 <= m < -135:
            k = 7
        elif 225 < m <= 255 or -135 <= m < -105:
            k = 8
        elif 255 < m <= 285 or -105 <= m < -75:
            k = 9
        elif 285 < m <= 315 or -75 <= m < -45:
            k = 10
        elif 315 < m <= 345 or -45 <= m < -15:
            k = 11
        elif 345 < m < 360 or -360 < m < -345 or -15 <= m <=15:
            k = 0
        print(i,j,k)
        if self.explored[i][j][k] == 1:
            return False
        else:
            return True
        #self.visited_matrix[i][j][k] = 1
        #return self.visited_matrix


    def addParent(self, node, parentNode, cost):
        if node[0] % 1 > self.dist_threshold / 2:
            i = int(math.ceil(node[0]) / self.dist_threshold)               #uppervalue
        else:
            i = int(math.floor(node[0]) / self.dist_threshold)

        if node[1] % 1 > self.dist_threshold / 2:                           #lower value
            j = int(math.ceil(node[1]) / self.dist_threshold)
        else:
            j = int(math.floor(node[1]) / self.dist_threshold)

        i = 200 if i > 200 else i
        j = 300 if j > 300 else j
        m = node[1]
        ###for K, changed with 30 degrees.
        if m >= 360:
            m = m % 360
        if 15 < m <= 45 or -345 <= m < -315:
            k = 1
        elif 45 < m <=75 or -315 <= m <-285:
            k =2
        elif 75 < m <= 105 or -285 <= m < -255:
            k = 3
        elif 105 < m <= 135 or -255 <= m < -225:
            k = 4
        elif 135 < m <= 165 or -225 <= m < -195:
            k = 5
        elif 165 < m <= 195 or -195 <= m < -165:
            k = 6
        elif 195 < m <= 225 or -165 <= m < -135:
            k = 7
        elif 225 < m <= 255 or -135 <= m < -105:
            k = 8
        elif 255 < m <= 285 or -105 <= m < -75:
            k = 9
        elif 285 < m <= 315 or -75 <= m < -45:
            k = 10
        elif 315 < m <= 345 or -45 <= m < -15:
            k = 11
        elif 345 < m < 360 or -360 < m < -345 or -15 <= m <=15:
            k = 0

        #self.parentData[i,j,k,:3] = np.array(parentNode)
        self.parentData[i, j, k, 0] = parentNode[0]
        self.parentData[i, j, k, 1] = parentNode[1]
        print("node2",parentNode)
        self.parentData[i, j, k, 2] = parentNode[2]
        self.parentData[i, j, k, 3] = cost
        #pass

    def getParent(self, node):
        if node[0] % 1 > self.dist_threshold / 2:
            i = int(math.ceil(node[0]) / self.dist_threshold)               #uppervalue
        else:
            i = int(math.floor(node[0]) / self.dist_threshold)

        if node[1] % 1 > self.dist_threshold / 2:                           #lower value
            j = int(math.ceil(node[1]) / self.dist_threshold)
        else:
            j = int(math.floor(node[1]) / self.dist_threshold)

        i = 200 if i > 200 else i
        j = 300 if j > 300 else j

        m = node[1]
        ###for K, changed with 30 degrees.
        if m >= 360:
            m = m % 360
        if 15 < m <= 45 or -345 <= m < -315:
            k = 1
        elif 45 < m <= 75 or -315 <= m < -285:
            k = 2
        elif 75 < m <= 105 or -285 <= m < -255:
            k = 3
        elif 105 < m <= 135 or -255 <= m < -225:
            k = 4
        elif 135 < m <= 165 or -225 <= m < -195:
            k = 5
        elif 165 < m <= 195 or -195 <= m < -165:
            k = 6
        elif 195 < m <= 225 or -165 <= m < -135:
            k = 7
        elif 225 < m <= 255 or -135 <= m < -105:
            k = 8
        elif 255 < m <= 285 or -105 <= m < -75:
            k = 9
        elif 285 < m <= 315 or -75 <= m < -45:
            k = 10
        elif 315 < m <= 345 or -45 <= m < -15:
            k = 11
        elif 345 < m < 360 or -360 < m < -345 or -15 <= m <= 15:
            k = 0

        return tuple([self.parentData[i,j,k,0], self.parentData[i,j,k,1], self.parentData[i,j,k,2]])

    def getCost(self, node):
        if node[0] % 1 > self.dist_threshold / 2:
            i = int(math.ceil(node[0]) / self.dist_threshold)  # uppervalue
        else:
            i = int(math.floor(node[0]) / self.dist_threshold)

        if node[1] % 1 > self.dist_threshold / 2:  # lower value
            j = int(math.ceil(node[1]) / self.dist_threshold)
        else:
            j = int(math.floor(node[1]) / self.dist_threshold)

        i = 200 if i > 200 else i
        j = 300 if j > 300 else j
        m = node[1]
        ###for K, changed with 30 degrees.
        if m >= 360:
            m = m % 360
        if 15 < m <= 45 or -345 <= m < -315:
            k = 1
        elif 45 < m <= 75 or -315 <= m < -285:
            k = 2
        elif 75 < m <= 105 or -285 <= m < -255:
            k = 3
        elif 105 < m <= 135 or -255 <= m < -225:
            k = 4
        elif 135 < m <= 165 or -225 <= m < -195:
            k = 5
        elif 165 < m <= 195 or -195 <= m < -165:
            k = 6
        elif 195 < m <= 225 or -165 <= m < -135:
            k = 7
        elif 225 < m <= 255 or -135 <= m < -105:
            k = 8
        elif 255 < m <= 285 or -105 <= m < -75:
            k = 9
        elif 285 < m <= 315 or -75 <= m < -45:
            k = 10
        elif 315 < m <= 345 or -45 <= m < -15:
            k = 11
        elif 345 < m < 360 or -360 < m < -345 or -15 <= m <= 15:
            k = 0

        return self.parentData[i,j,k,3]


    def addExplored(self, node):
        if node[0] % 1 > self.dist_threshold / 2:
            i = int(math.ceil(node[0]) / self.dist_threshold)  # uppervalue
        else:
            i = int(math.floor(node[0]) / self.dist_threshold)

        if node[1] % 1 > self.dist_threshold / 2:  # lower value
            j = int(math.ceil(node[1]) / self.dist_threshold)
        else:
            j = int(math.floor(node[1]) / self.dist_threshold)

        i = 200 if i > 200 else i
        j = 300 if j > 300 else j
        m = node[1]
        ###for K, changed with 30 degrees.
        if m >= 360:
            m = m % 360
        if 15 < m <= 45 or -345 <= m < -315:
            k = 1
        elif 45 < m <= 75 or -315 <= m < -285:
            k = 2
        elif 75 < m <= 105 or -285 <= m < -255:
            k = 3
        elif 105 < m <= 135 or -255 <= m < -225:
            k = 4
        elif 135 < m <= 165 or -225 <= m < -195:
            k = 5
        elif 165 < m <= 195 or -195 <= m < -165:
            k = 6
        elif 195 < m <= 225 or -165 <= m < -135:
            k = 7
        elif 225 < m <= 255 or -135 <= m < -105:
            k = 8
        elif 255 < m <= 285 or -105 <= m < -75:
            k = 9
        elif 285 < m <= 315 or -75 <= m < -45:
            k = 10
        elif 315 < m <= 345 or -45 <= m < -15:
            k = 11
        elif 345 < m < 360 or -360 < m < -345 or -15 <= m <= 15:
            k = 0
        print("aaaa",i,j,k)
        self.explored[i][j][k] = 1



    def path(self, d):
        # for d in data:

        self.animationImage[int(d[0]), int(d[1]), :] = np.array([0, 255, 0])
        # print("showing final")
        # plt.imshow(self.animationImage)
        # plt.show()
        return



