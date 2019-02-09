from distutils.core import setup


setup(
    name='tserror',
    version='0.1dev-1',
    author='Yuki Nagae',
    author_email='yuki.nagae1130@gmail.com',
    install_requires=[
        'numpy',
        'scikit-learn'
    ],
    tests_require=['pytest'],
    packages=['tserror'],
    license='MIT',
    description='A tiny python package analyzes time series prediction errors',
)
