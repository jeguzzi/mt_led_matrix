#!/usr/bin/env python

import max7219.led as led
from max7219 import font
import rospy
from mt_led_matrix.msg import Buffer
from std_msgs.msg import String, UInt8

# See https://max7219.readthedocs.io/en/0.2.3/max7219.html#max7219.led.device.brightness


class LedMatrix(object):
    """docstring for LedMatrix."""

    def __init__(self):
        super(LedMatrix, self).__init__()
        rospy.init_node('led_matrix')
        self.delay = rospy.get_param('~delay', 0.1)
        try:
            self.font = getattr(font,
                                '{0}_FONT'.format(rospy.get_param('~font', 'DEFAULT').upper()))
        except:
            self.font = None
        self.device = led.matrix(cascaded=2)
        self.device.orientation(270, redraw=False)
        rospy.Subscriber('~text', String, self.update_text, queue_size=1)
        rospy.Subscriber('~brightness', UInt8, self.update_brightness, queue_size=1)
        rospy.Subscriber('~buffer', Buffer, self.update_buffer, queue_size=1)
        rospy.on_shutdown(self.on_shutdown)
        rospy.spin()

    def update_text(self, msg):
        self.device.show_message(msg.data, delay=self.delay, font=self.font)

    def update_brightness(self, msg):
        value = min(msg.data, 15)
        self.device.brightness(value)

    def update_buffer(self, msg):
        for i, v in enumerate(msg.data):
            self.device._buffer[i] = ord(v)
        self.device.flush()

    def on_shutdown(self):
        self.device.clear()

if __name__ == '__main__':
    LedMatrix()
