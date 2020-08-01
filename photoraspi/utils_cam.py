from picamera import PiCamera
from time import sleep
from pathlib import Path

def timestamp():
    localtime = time.localtime(time.time())
    timestamp = f'{localtime.tm_year}{localtime.tm_mon:02d}{localtime.tm_mday:02d}' + \
                f'-{localtime.tm_hour:02d}{localtime.tm_min:02d}{localtime.tm_sec:02d}' #(localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec)
    return timestamp

def livetime(timer, alpha=255):
    camera = PiCamera()
    camera.start_preview(alpha=alpha)
    sleep(timer)
    camera.stop_preview()

def shootseries(num_imgs, interval, path_output):
    if isinstance(path_output, str):
        path_output = Path(path_output)

    for i in range(num_imgs):
        camera.capture(path_output / 'image%s.jpg' % i)
        sleep(interval)