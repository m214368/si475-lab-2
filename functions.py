import numpy as np
from math import cos,sin

def rotate(theta):
    return np.array([[cos(theta),-1*sin(theta),0],
                     [sin(theta),cos(theta),0],
                     [0,0,1]])

def translate(x,y):
    return np.array([[1,0,x],
                     [0,1,y],
                     [0,0,1]])

def rotateX(theta):
    return np.array([[1,0,0,0],
                     [0,cos(theta),-1*sin(theta),0],
                     [0,sin(theta),cos(theta),0],
                     [0,0,0,1]])

def rotateZ(theta):
    return np.array([[cos(theta),-1*sin(theta),0,0],
                     [sin(theta),cos(theta),0,0],
                     [0,0,1,0],
                     [0,0,0,1]])

def translateX(x):
    return np.array([[1,0,0,x],
                     [0,1,0,0],
                     [0,0,1,0],
                     [0,0,0,1]])

def translateZ(z):
    return np.array([[1,0,0,0],
                     [0,1,0,0],
                     [0,0,1,z],
                     [0,0,0,1]])

def T(x,y,z,psi,phi,theta):
    return np.array([[cos(theta)*cos(phi),-sin(theta)*cos(psi)+cos(theta)*sin(phi)*sin(psi),sin(theta)*sin(psi)+cos(theta)*sin(phi)*cos(psi),x],
                     [sin(theta)*cos(phi),cos(theta)*cos(psi)+sin(theta)*sin(phi)*sin(psi),-cos(theta)*sin(psi)+sin(theta)*sin(phi)*cos(psi),y],
                     [-sin(phi),cos(phi)*sin(psi),cos(theta)*cos(psi),z],
                     [0,0,0,1]])