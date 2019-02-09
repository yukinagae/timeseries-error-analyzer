from distutils.core import setup

REQUIREMENTS = [
    'numpy',
    'sklearn',
    # test
    'pytest',
]

setup(
    name='tserror',
    version='0.1dev-1',
    author='Yuki Nagae',
    author_email='yuki.nagae1130@gmail.com',
    install_requires=REQUIREMENTS,
    packages=['tserror'],
    license='MIT',
    description='A tiny python package analyzes time series prediction errors',
)
