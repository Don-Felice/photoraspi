# -*- coding: utf-8 -*-


# external imports
from picamera import PiCamera
import argparse

# project intern imports
from photoraspi.utils_cam import livetime


class LiveTime:
    """ Live stream to display
    """

    @staticmethod
    def init_parser(parser):
        parser.add_argument("-a", "--alpha", type=int, default=60,
                            help="transparency of preview mode")

    @staticmethod
    def run(args):
        camera = PiCamera()
        print("Take your time to adjust the camera, you don't wanna mess this up!!")
        livetime(camera, alpha=args.alpha)


