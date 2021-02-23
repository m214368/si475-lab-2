import functions as fun
from math import atan2
import arm


def reverse(x,y,z,psi,phi,theta):
	#calculate T
	T = fun.T(x,y,z,psi,phi,theta)
	#calculate angle 1
	angleA = atan2(-T[0,1],T[1,1])
	#calculate angle 2
	one = (T[0,3]-.012-.126*T[0,0])/(T[1,1]*.196)
	two = (T[2,3]-.077-.126*T[2,0])/(.196)
	angleB = atan2(one,two)
	#calculate angle 3
	angleC = atan2(T[1,0],T[0,0])-angleB

	print(angleA,angleB,angleC)
	test = arm.arm1()  
	test.move(angleA,angleB,angleC)
	test.pose()
#
#
#