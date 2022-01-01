from lib.receiver import Receiver
from lib.spliner import Spliner
from lib.data import Data
import rospy
from std_msgs.msg import String

class Master:
    def __init__(self):
        rospy.init_node('Master', anonymous=False)
        self.data = Data()
        self.receiver = Receiver(self.data)
        self.spliner = Spliner(self.data)
    
    def run(self):
        self.spliner.run()

if __name__ == "__main__":
    mm = Master()
    while not rospy_is_shutdown():
        mm.run()