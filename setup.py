from setuptools import setup


setup(
    name='photoraspi',
    version='0.1.0',
    author='Felix Segerer',
    packages=['photoraspi'],
    license='LICENSE',
    description='Photography tools using the raspberry pi',
    entry_points={
        'console_scripts': [
            'photoraspi = photoraspi.__main__:main',
        ],
        'photoraspi_plugins': [
            'shot = photoraspi.plugins.shot:Shot',
            'mshot = photoraspi.plugins.multishot:MultiShot',
            'lt = photoraspi.plugins.livetime:LiveTime',
        ],
     }
)
