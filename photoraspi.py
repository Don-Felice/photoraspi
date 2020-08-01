# -*- coding: utf-8 -*-
# FSegerer 20200801

# external imports
from picamera import PiCamera
import argparse

# project intern imports
from photoraspi.utils_cam import livetime, shootseries


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("num_imgs", type=int,
                        help="number of images to be taken")
    parser.add_argument("interval", type=int,
                        help="interval between images")
    parser.add_argument("dest_dir", type=str,
                        help="destination directory for image output")
    parser.add_argument("-a", "--alpha", type=int, default=60,
                        help="transparency of preview mode")
    args = parser.parse_args()

    camera = PiCamera()
    print("Take your time to adjust the camera, you don't wanna mess this up!!")
    livetime(camera, alpha=args.alpha)
    shootseries(camera, args.num_imgs, args.interval, args.dest_dir)
