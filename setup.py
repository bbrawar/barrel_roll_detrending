from setuptools import setup, find_packages

setup(
    name='brc',
    version='0.1.0',
    description='Barrel-Roll Curve (BRC) computation for time-series data',
    author='Bhuvnesh Brawar',
    author_email='bbrawar@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
