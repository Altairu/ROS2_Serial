# serial_send_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

import serial

class SerialSendNode(Node):
    def __init__(self):
        super().__init__('serial_send_node')

        self.ser = serial.Serial("/dev/ttyACM0", baudrate=9600)
        self.subscription = self.create_subscription(
            Int32MultiArray, 'received_data', self.listener_callback, 10)  # 送信するデータをsubscribeするトピック

    def listener_callback(self, msg):
        # 受け取ったデータをそのままROS 2ノード上でpublish
        self.get_logger().info(f"Received and Sent Back: {msg.data}")

        # Int32MultiArrayをバイト配列に変換してシリアル通信で送信
        send_data = bytes(msg.data)
        self.ser.write(send_data)
        self.get_logger().info(f"Sent Back: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    serial_send_node = SerialSendNode()
    rclpy.spin(serial_send_node)
    serial_send_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
