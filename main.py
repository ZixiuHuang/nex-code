
from image_enhancement import imageEnhancement
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-image_dir', type=str, default="./images/", help='directory to the images')
parser.add_argument('-resize', type=int, default=100, help='resize images to x% of original size')
args = parser.parse_args()

imageEnhancement(args)