# -*- coding: utf-8 -*-


# external imports
from picamera import PiCamera
import argparse

# project intern imports
from photoraspi.utils_cam import livetime, shootseries


class MultiShot:
    """ Take multiple pictures in a given interval
    """

    @staticmethod
    def init_parser(parser):
        parser.add_argument("num_imgs", type=int,
                            help="number of images to be taken")
        parser.add_argument("interval", type=int,
                            help="interval between images")
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
        shootseries(camera, args.num_imgs, args.interval, args.dest_dir)


