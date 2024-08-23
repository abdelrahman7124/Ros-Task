#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import random

class UltrasonicPublisher(Node):
    def __init__(self):
        super().__init__('ultrasonic_publisher')
        self.publisher_ = self.create_publisher(Twist, 'ultrasonic_data', 10)
        self.timer = self.create_timer(1, self.timer_callback)
    
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = random.uniform(0.0, 100.0)
        formated=format(msg.linear.x,".2f")
        self.publisher_.publish(msg)
        self.get_logger().info(f'Sending: {formated}')

def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
