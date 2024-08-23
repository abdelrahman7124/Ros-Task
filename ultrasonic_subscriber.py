#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class UltrasonicSubscriber(Node):
    def __init__(self):
        super().__init__('ultrasonic_subscriber')
        self.sub = self.create_subscription(Twist,'ultrasonic_data',self.timer_callback,10)

    def timer_callback(self, msg):
        reading = msg.linear.x
        formated=format(reading,".2f")
        self.get_logger().info(f'Received : {formated}')
        if reading < 50.0:
            self.get_logger().info("Object detected.")
        else:
            self.get_logger().info("Clear path.")

def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
