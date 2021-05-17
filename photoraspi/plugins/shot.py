# -*- coding: utf-8 -*-


# external imports
from picamera import PiCamera


# project intern imports
from photoraspi.utils_cam import livetime, singleshot


class Shot:
    """
    Take a single picture
    """

    @staticmethod
    def init_parser(parser):
        """
        Adding arguments to an argparse parser. Needed for all photoraspi_plugins.
        """
        parser.add_argument("dest_dir", type=str,
                            help="destination directory for image output")
        parser.add_argument("-a", "--alpha", type=int, default=60,
                            help="transparency of preview mode")
        parser.add_argument("-q", "--quick", action='store_true', default=False,
                            help="Skip camera adjustment before shot.")

    def __init__(self, args):
        self.camera = PiCamera()
        for arg in vars(args):
            setattr(self, arg, getattr(args, arg))

    def run(self):
        if not self.quick:
            print("Take your time to adjust the camera, you don't wanna mess this up!!")
            livetime(self.camera, alpha=self.alpha)
        singleshot(self.camera, self.dest_dir)
