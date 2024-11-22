import argparse
from startrail import StarTrail
import os
import glob

def main():
    parser = argparse.ArgumentParser(description="Generate star trail images or videos")
    parser.add_argument('-i', '--input', required=True, help="Input image folder path")
    parser.add_argument('-o', '--output', required=True, help="Output file path or folder path")
    parser.add_argument('-d', '--decay', type=float, default=1.0, help="Decay value, range from 0 to 1, default is 1.0")
    parser.add_argument('-m', '--mode', choices=['image', 'video', 'frame'], required=True, help="Output mode: image, video, or frame")

    args = parser.parse_args()

    if args.decay < 0 or args.decay > 1:
        print("Decay value should be a decimal between 0 and 1")
        return

    # Get all image files in the input folder
    input_files = glob.glob(os.path.join(args.input, '*'))
    input_files = [f for f in input_files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

    if not input_files:
        print("No supported image files found in the input folder")
        return

    if args.mode == 'image':
        if not args.output.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            print("Output file format not supported, only .jpg, .jpeg, .png, .bmp are supported")
            return
    elif args.mode == 'video':
        if not args.output.lower().endswith('.mp4'):
            print("Output file format not supported, only .mp4 is supported")
            return
    elif args.mode == 'frame':
        if not os.path.isdir(args.output):
            os.makedirs(args.output, exist_ok=True)

    star_trail = StarTrail(input_files, args.output, args.decay)

    if args.mode == 'image':
        star_trail.image()
    elif args.mode == 'video':
        star_trail.video()
    elif args.mode == 'frame':
        star_trail.frame()

    print("Processing completed")

if __name__ == "__main__":
    main() 