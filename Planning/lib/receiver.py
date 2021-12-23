import rospy
from geometry_msgs.msg import Point

class Recevier:
    def __init__(self, data):
        self.data = data
        rospy.Subscriber('/point', Point, self.pointCallback)

    def pointCallback(self, msg):
        self.data.next_point = msg.x
        print(f"Msg recevived: {msg.x}")