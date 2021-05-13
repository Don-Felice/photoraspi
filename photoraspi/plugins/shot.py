# -*- coding: utf-8 -*-


# external imports
from picamera import PiCamera
import argparse

# project intern imports
from photoraspi.utils_cam import livetime, singleshot


class Shot:
    """ Take a single picture
    """

    @staticmethod
    def init_parser(parser):
        parser.add_argument("dest_dir", type=str,
                            help="destination directory for image output")
        parser.add_argument("-a", "--alpha", type=int, default=60,
                            help="transparency of preview mode")
        parser.add_argument("-q", "--quick", action='store_true', default=False,
                            help="Skip camera adjustment before shot.")

    @staticmethod
    def run(args):
        camera = PiCamera()
        if not args.quick:
            print("Take your time to adjust the camera, you don't wanna mess this up!!")
            livetime(camera, alpha=args.alpha)
        singleshot(camera, args.dest_dir)


