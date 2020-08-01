# -*- coding: utf-8 -*-
# FSegerer 20200801

from picamera import PiCamera
import time
from pathlib import Path


def gettimestamp():
    localtime = time.localtime(time.time())
    timestamp = f'{localtime.tm_year}{localtime.tm_mon:02d}{localtime.tm_mday:02d}' + \
                f'-{localtime.tm_hour:02d}{localtime.tm_min:02d}{localtime.tm_sec:02d}'
    return timestamp


def livetime(camera, timer=None, alpha=255):
    try:
        camera.start_preview(alpha=alpha)
        if timer:
            time.sleep(timer)
        else:
            input("Press enter to continue...")
        camera.stop_preview()
    finally:
        camera.stop_preview()


def shootseries(camera, num_imgs, interval, path_output):
    if isinstance(path_output, str):
        path_output = Path(path_output)

    timestamp_initial = gettimestamp()
    path_output = path_output / f'Series_starting_{timestamp_initial}'

    path_output.mkdir(parents=True, exist_ok=True)
    print('---------------------')
    print(f'Will start to take beautiful pictures and save them in \"{str(path_output)}\"')
    print(f'Whole series will roughly take {interval*(num_imgs-1)/60:5.2f} minutes')
    for i in range(num_imgs):
        timestamp = gettimestamp()
        img_name = f'RasPic_{timestamp}.jpg'
        camera.capture(str(path_output / img_name))
        print(f'capturing image {i} out of {num_imgs}: {img_name}')
        time.sleep(interval)
    print(f'Awesome series captured and saved in \"{str(path_output)}\"')
    print('---------------------')
