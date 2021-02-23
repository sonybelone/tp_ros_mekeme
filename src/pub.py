#!/usr/bin/env python
# license removed for brevity
import math
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped 
from move_pose.msg import GeoStamped

def talker():
	pub =rospy.Publisher("chatter", PoseStamped, queue_size=10)
	rospy.init_node("talker",anonymous=True)
	rate = rospy.Rate(15) #15hz
	Carre=PoseStamped()
	print(Carre)
	c = 0
	d = 0
	Carre.pose.position.y = 0;
	Carre.pose.position.x = 0;
	
	while not rospy.is_shutdown():
		
		if(Carre.pose.position.y == 0 && Carre.pose.position.x ==0):
			
		while(Carre.pose.position.y != 10):
			Carre.pose.position.y = c
			c= c + 1
			pub.publish(Carre)
			rate.sleep()
		while(Carre.pose.position.x != 10):
			Carre.pose.position.x = d
			d= d + 1
			pub.publish(Carre)
			rate.sleep()

		elif(Carre.pose.position.x == 10 && Carre.pose.position.y ==10):
			
		while(Carre.pose.position.y != 10):
			Carre.pose.position.y = c
			c= c + 1
			pub.publish(Carre)
			rate.sleep()
		while(Carre.pose.position.x != 10):
			Carre.pose.position.x = d
			d= d + 1
			pub.publish(Carre)
			rate.sleep()



		pub.publish(Carre) 

		rate.sleep()
if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
