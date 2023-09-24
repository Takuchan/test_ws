import rclpy
from turtlesim.srv import Spawn
from rclpy.node import Node


class SimpleService(Node):
    def __init__(self):
        super().__init__('simple_server')
        self.srv = self.create_service(Spawn,'spawn',self.spawn_callback)
    
    def spawn_callback(self,request,response):
        if request.name == '':
            response.name = 'kame'
        else:
            response.name = request.name
        
        self.get_logger().info('Request:x=%f, y=%f, theta=%f, name=%s\nResponse:name=%s' % (request.x, request.y, request.theta, request.name, response.name))

        return response
def main(args=None):
    rclpy.init(args=args)
    simple_service = SimpleService()
    rclpy.spin(simple_service)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
