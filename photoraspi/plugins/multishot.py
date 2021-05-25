# -*- coding: utf-8 -*-


# external imports
from picamera import PiCamera

# project intern imports
from photoraspi.utils_cam import livetime, shootseries
from photoraspi.photoraspi_plugin import PhotoraspiPlugin


class MultiShot(PhotoraspiPlugin):
    """
    Take multiple pictures in a given interval
    """

    @staticmethod
    def init_parser(parser):
        """
        Adding arguments to an argparse parser. Needed for all photoraspi_plugins.
        """
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

    def __init__(self, args):
        self.camera = PiCamera()
        super().__init__(args)

    def run(self):
        camera = PiCamera()
        if not self.quick:
            print("Take your time to adjust the camera, you don't wanna mess this up!!")
            livetime(camera, alpha=self.alpha)
        shootseries(self.camera, self.num_imgs, self.interval, self.dest_dir)
