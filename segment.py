import functions as func
import numpy as np

class segment:
	def __init__(self, theta, l, d, alpha):
		self.theta = theta # only used for the intial theta, combined with user input to get angle.
		self.l = l
		self.d = d
		self.alpha = alpha
		self.angle = theta
		self.rotZ = func.rotateZ(self.angle)
		self.transX = func.translateX(self.l)
		self.transZ = func.translateZ(self.d)
		self.rotX = func.rotateX(self.alpha)

	def turn(self, theta):
		self.angle = self.theta + theta
		self.rotZ = func.rotateZ(self.angle)

	def matrix(self):
		matrix = np.dot(self.rotZ,self.transX)
		matrix = np.dot(matrix,self.transZ)
		matrix = np.dot(matrix,self.rotX)
		return matrix
