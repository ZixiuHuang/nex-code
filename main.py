
from image_enhancement import imageEnhancement
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-image_enhancement', action="store_true", help='run image enhancement.')
parser.add_argument('-resize', type=int, default=100, help='image resize.')
parser.add_argument('-colmap', action="store_true", help='run colmap.')
parser.add_argument('-nex', action="store_true", help='run nex.')
args = parser.parse_args()





imageEnhancement(args)