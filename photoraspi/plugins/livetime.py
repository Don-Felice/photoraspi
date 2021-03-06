# -*- coding: utf-8 -*-


# external imports
from picamera import PiCamera

# project intern imports
from photoraspi.utils_cam import livetime
from photoraspi.photoraspi_plugin import PhotoraspiPlugin


class LiveTime(PhotoraspiPlugin):
    """
    Live stream to display
    """

    @staticmethod
    def init_parser(parser):
        """
        Adding arguments to an argparse parser. Needed for all photoraspi_plugins.
        """
        parser.add_argument("-a", "--alpha", type=int, default=60,
                            help="transparency of preview mode")

    def __init__(self, args):
        self.camera = PiCamera()
        super().__init__(args)

    def run(self):
        print("Take your time to adjust the camera, you don't wanna mess this up!!")
        livetime(self.camera, alpha=self.alpha)
