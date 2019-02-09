from distutils.core import setup

REQUIREMENTS = [
    "numpy",
    "sklearn",
]

setup(
    name='ts-error',
    version='0.1dev',
    author='Yuki Nagae',
    author_email='yuki.nagae1130@gmail.com',
    install_requires=REQUIREMENTS,
    packages=['ts-error'],
    license='MIT',
    description='A tiny python package analyzes time series prediction errors',
    long_description=open('README.md').read(),
)
