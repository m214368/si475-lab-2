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

	print('angles')
	print(angleA,angleB,angleC)
	test = arm.arm1()  
	test.move(angleA,angleB,angleC)
	print('test')
	test.pose()

print("one")
#(.2,-.5,-.4)

#('x = ', 0.19241939581316006)
#('y = ', 0.036572822131738902)
#('z = ', 0.29600097135780656)
#('roll  =', -1.295849689882289e-17)
#('pitch =', -0.6000000000000001)
#('yaw   =', 0.19999999999999998)
reverse(.192,.036,.296,0,-.6,.2)

print("two")
#(0,0,0)

#('x = ', 0.28471563338320116)
#('y = ', -7.8377395145430601e-18)
#('z = ', 0.20500000000000002)
#('roll  =', 0.0)
#('pitch =', -0.0)
#('yaw   =', -1.5407439555097887e-33)
reverse(.285,0,.2,0,0,0)

print("three")
#(.5,.5,.5)

#('x = ', 0.14996623417522889)
#('y = ', 0.075371297244299015)
#('z = ', -0.051586657275799155)
#('roll  =', -8.043990182777856e-16)
#('pitch =', 1.5)
#('yaw   =', 0.5000000000000013)
reverse(.15,.075,-.052)

#print("four")
#myarm.move(0,0,.7)

#print("five")
#myarm.move(0,.7,0)

#print("six")
#myarm.move(.7,0,0)

