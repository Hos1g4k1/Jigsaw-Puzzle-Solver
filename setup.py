from setuptools import setup

setup(
    name="jigsaw",
    version="1.0",
    author="Milos Milakovic Lazar Celikovic",
    description="Jigsaw puzzle solver using genetic algorithm",
    license="MIT",
    url="",
    packages=[
        "jigsaw"
    ],
    install_requires=[
        "numpy",
        "matplotlib",
        "opencv-python"
    ],
    scripts=[
        "bin/create_puzzle",
        "bin/jigsaw"
    ]
)
