import functions as fun
from math import atan2
import arm

test = arm.arm1()  

def reverse(x,y,z,psi,phi,theta):
	#calculate T
	T = fun.T(x,y,z,psi,phi,-theta)#negate theta b/c arm design
	#calculate angle 1
	angleA = atan2(-T[0,1],T[1,1])
	#calculate angle 2
	one = (T[0,3]-.012-.126*T[0,0])/(T[1,1]*.196)
	two = (T[2,3]-.077-.126*T[2,0])/(.196)
	angleB = atan2(one,two) - .853
	#calculate angle 3
	angleC = phi-angleB

	print('angles')
	print(angleA,angleB,angleC)
	test = arm.arm1()  
	test.move(angleA,angleB,angleC)
	print('test')
	test.pose()

def testCase(angleA,angleB,angleC):
	print(str(angleA)+" "+str(angleB)+" "+str(angleC))
	test.move(angleA,angleB,angleC)
	x,y,z,psi,phi,theta = test.pose()
	print(reverse(x,y,z,psi,phi,theta))

testCase(0.5,0.5,0.5)


