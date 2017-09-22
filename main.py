#!/usr/bin/env python2.7
import gym
import reacher.Reacher
import numpy as np
import cv2
import math
import scipy as sp


class MainReacher():
    def __init__(self):
        self.env = gym.make('ReacherMy-v0')
        self.env.reset()

    def detect_blue(self,image):
        #In this method you can focus on detecting the blue circle
        return

    def detect_green(self,image):
        #In this method you should focus on detecting the green circle
        return

    def detect_red(self,image):
        #In this method you should focus on detecting the red circle
        return

    def detect_target(self,image):
        #Detect the target circle (Colour: [200,200,200])
        return

    def detect_joint_angles(self,image):
        #Calculate the relevant joint angles from the image
        return

    def detect_ee(self,image):
        #Detect the end effector location
        return

    def FK(self,joint_angles):
        #Forward Kinematics to calculate end effector location
        #Each link is 1m long and 0.2m wide
        return

    def coordinate_convert(self,pixels):
        #Converts pixels into metres
        return np.array([(pixels[0]-self.env.viewerSize)/self.env.resolution,(pixels[0]-self.env.viewerSize)/self.env.resolution])

    def go(self):
        #The robot has several simulated modes:
        #These modes are listed in the following format:
        #Identifier (control mode) : Description : Input structure into step function

        #POS : A joint space position control mode that allows you to set the desired joint angles and will position the robot to these angles : env.step((np.zeros(3),np.zeros(3), desired joint angles, np.zeros(3)))
        #POS-IMG : Same control as POS, however you must provide the current joint angles and velocities : env.step((estimated joint angles, estimated joint velocities, desired joint angles, np.zeros(3)))
        #VEL : A joint space velocity control, the inputs require the joint angle error and joint velocities : env.step((joint angle error (velocity), estimated joint velocities, np.zeros(3), np.zeros(3)))
        #TORQUE : Provides direct access to the torque control on the robot : env.step((np.zeros(3),np.zeros(3),np.zeros(3),desired joint torques))
        self.env.controlMode="POS"
        #Run 100000 iterations
        for _ in range(100000):
            #self.env.render returns and rgb_array containing the image of the robot
            rgb_array = self.env.render()
            jointAngles = np.array([0.9,0,-1.5])
            self.env.step((np.zeros(3),np.zeros(3),jointAngles, np.zeros(3)))
            #The step method will send the control input to the robot, the parameters are as follows: (Current Joint Angles/Error, Current Joint Velocities, Desired Joint Angles, Torque input) 

#main method
def main():
    reach = MainReacher()
    reach.go()

if __name__ == "__main__":
    main()
