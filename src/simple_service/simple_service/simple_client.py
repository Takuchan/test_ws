import sys
from turtlesim.srv import Spawn
import rclpy
from rclpy.node import Node

class SimpleClient(Node):
    def __init__(self):
        super().__init__('simple_client')
        self.cli = self.create_client(Spawn,'spawn')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available . waiting again...')
        self.req = Spawn.Request()

    def send_request(self):
        self.req.x           = float(sys.argv[1])     #  亀の位置x座標
        self.req.y           = float(sys.argv[2])     #  亀の位置y座標
        self.req.theta   = float(sys.argv[3])    #  亀の向き[rad]        
        self.req.name  = str(sys.argv[4])        #  亀の名前
        self.future         = self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    simple_client=SimpleClient()
    simple_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(simple_client)
        if simple_client.future.done():
            try:
                response = simple_client.future.result() # サーバーから非同期的に送られてきたレスポンス
            except Exception as e:                                         #  エラー時の処理
                simple_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:  #  エラーでないときは、端末にレスポンスである亀の名前を表示する
                simple_client.get_logger().info('Response:name=%s' % response.name)
            break
    simple_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()