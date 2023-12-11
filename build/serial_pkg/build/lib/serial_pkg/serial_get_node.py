# serial_get_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

import serial

class SerialGetNode(Node):
    def __init__(self):
        super().__init__('serial_get_node')

        self.ser = serial.Serial("/dev/ttyACM0", baudrate=9600)
        self.publisher = self.create_publisher(
            Int32MultiArray, 'received_data', 10)  # 受け取ったデータをpublishするトピック
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        if self.ser.in_waiting >= 32:
            # シリアルから32バイトデータを読み取り、Int32MultiArrayに変換
            received_data = Int32MultiArray()
            received_data.data = list(self.ser.read(32))

            # 受信したデータをそのままROS 2ノード上でpublish
            self.publisher.publish(received_data)
            self.get_logger().info(f"Received and Published: {received_data.data}")

def main(args=None):
    rclpy.init(args=args)
    serial_get_node = SerialGetNode()
    rclpy.spin(serial_get_node)
    serial_get_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
