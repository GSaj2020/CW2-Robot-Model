#!/usr/bin/env python

import rospy  
#Jointstates package contains the states of our robot's joints etc vel,pos,effect
from sensor_msgs.msg import JointState 
# Header- to publish a message 
from std_msgs.msg import Header


def talker():
# initialise class publisher - instance to publish in the topic; the message between the publisher and subscriber
    
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)

    rospy.init_node('lin_joint_state_publisher')
    rate = rospy.Rate(10) # 10hz

####### Joint 1:
    joint_1 = JointState()# creating an instance
    joint_1.header = Header() # creating a header
    joint_1.header.stamp = rospy.Time.now() # a header file contains the time.stamp which tells you when the message was published to ensure the subscriber takes the most recent message from 						      publisher(talker)

    while not rospy.is_shutdown(): # user input
	####### Joint 1:
	joint_1.name = ['base_link_link_1', 'my_first_link1_link_2','link2_link_3','link3_link_4']
	print "User input for joint 1:"
	coordinates = raw_input()
	new_coord = float(coordinates)

	####### Joint 2:
	print "User input for joint 2:"
	coordinates1 = raw_input()
	new_coord1 = float(coordinates1)

	while new_coord1 < -1.571 or new_coord1 > 1.571:
		print"Error, beyond joint limit, must be between 0.5 and -0.5. Please enter again:" 
		coordinates1 = raw_input()
		new_coord1 = float(coordinates1)

	
	####### Joint 3
	print "User input for joint 3:"
	coordinates2 = raw_input()
	new_coord2 = float(coordinates2)

	while new_coord2 < -1.571 or new_coord2 > 1.5751:
		print"Error, beyond joint limit, must be between 1 and -1. Please enter again:" 
		coordinates2 = raw_input()
		new_coord2 = float(coordinates2)

	####### Joint 4
	print "User input for joint 4:"
	coordinates3 = raw_input()
	new_coord3 = float(coordinates3)

	while new_coord3 < -1.571 or new_coord3 > 1.571:
		print"Error, beyond joint limit, must be between 1 and -1. Please enter again:" 
		coordinates3 = raw_input()
		new_coord3= float(coordinates3)


	joint_1.position = [new_coord, new_coord1, new_coord2, new_coord3]
	joint_1.header.stamp =rospy.Time.now()
	pub.publish(joint_1)

	rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
