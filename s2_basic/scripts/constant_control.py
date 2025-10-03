import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class constant_control(Node):
    def _init_(self) -> None:
        super()._init_("constant_control")

        self.control_msg = ("sending constant control")

        self.control_pub = self.create_publisher(String, "/constant_control", 10)

        self.control_timer = self.create_timer(0.2, self.control_callback)

        self.motor_sub = self.create_subscription(Bool,"/constant/control", self.control_callback, 10 )

    def control_callback(self) -> None:

        msg = String()
        msg.data = self.control_msg

        self.control_pub.publish(msg)

if _name_ == "_main_":
    rclpy.init()
    node = control_class()
    rclpy.spin(node)
    rclpy.shutdown()
    