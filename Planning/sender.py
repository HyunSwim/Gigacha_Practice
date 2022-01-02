import rospy
from geometry_msgs.msg import Point

class Sender:
    def __init__(self):
        rospy.init_node('Sender', anonymous = false)
        self.pub = rospy.Publisher('/point', Point, queue_size = 1)
        self.msg = Point()

    def run(self):
        inin = input("Input new point: ")
        self.msg.x = float(inin)
        self.pub.publish(self.msg)

if __name__ == "__main__":
    ss = Sender()
    while not rospy_is_shutdown():
        ss.run()