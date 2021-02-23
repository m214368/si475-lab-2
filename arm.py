from arm_controller import ArmController
import numpy as np
import segment as s
from math import acos, atan2, sqrt, cos

class arm(object):
	def __init__(self, segs):
		self.segments = segs

	def move(self,angles):
		for i in range(len(self.segments)):
			self.segments[i].turn(angles[i])

	def matrix(self):
		matrix = np.eye(4)
		for i in range(len(self.segments)):
			matrix = np.dot(matrix,self.segments[i].matrix())
		return matrix

class arm1(arm):
	def __init__(self):
		self.ac=ArmController()
		seg = list()
		seg.append(s.segment(0,.012,0,0))
		seg.append(s.segment(0,0,.077,(np.pi/2)))
		seg.append(s.segment((np.pi/2)-acos(.128/.13),.130,0,0))
		seg.append(s.segment(acos(.128/.13)-(np.pi/2),.124,0,0))
		seg.append(s.segment(0,.126,0,-(np.pi/2)))
		self.segments = seg
		super(arm1,self).__init__(seg)

	def move(self,u1,u2,u4):
		print('moving to '+str(u1)+','+str(u2)+','+str(u4))
		super(arm1,self).move([0,u1,-u2,0,-u4])
		self.ac.set_joints([u1,u2,0,u4])


	def pose(self):
		T = self.matrix()
		x=T[0,3]
		y=T[1,3]
		z=T[2,3]
		print("x = ",x)
		print("y = ",y)
		print("z = ",z)
		phi = atan2(-T[2,0],sqrt(T[0,0]*T[0,0]+T[1,0]*T[1,0]))
		theta = -atan2(T[1,0]/cos(phi),T[0,0]/cos(phi))
		psi = atan2(T[2,1]/cos(phi),T[2,2]/cos(phi))
		print("roll  =", psi)
		print("pitch =", phi)
		print("yaw   =", theta)
		print(self.ac.get_pose())
		return(x,y,z,psi,phi,theta)
