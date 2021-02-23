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

	print('\nCalculated Angles\n')
	print(angleA,angleB,angleC)
	test = arm.arm1()  
	test.move(angleA,angleB,angleC)
	print('\nMoving to the calculated angles\n')
	test.pose()

def testCase(angleA,angleB,angleC):
	print('~~~~~~~~~~~start~~~~~~~~~~~~~~~')
	print("Generating test case with angles:"+str(angleA)+" "+str(angleB)+" "+str(angleC))
	test.move(angleA,angleB,angleC)
	print("Test case generated, testing")
	x,y,z,psi,phi,theta = test.pose()
	reverse(x,y,z,psi,phi,theta)
	print('~~~~~~~~~~~end~~~~~~~~~~~~~~~~~')

testCase(0.5,0.5,0.5)
testCase(0,0,0)
testCase(0,-.7,0)
testCase(.7,0,0)
testCase(0,0,.7)
testCase(200,200,200)

