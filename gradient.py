# use idk.py's randomcolor function to get 2 random colors and create a gradient image with them
def main():
    from PIL import Image, ImageDraw, ImageFont
    from idk import randomcolor
    import os
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='Create a gradient image')
    parser.add_argument('-o', '--output', help='output image file name', required=True)
    parser.add_argument('-s', '--size', help='image size', required=True)
    parser.add_argument('-f', '--font', help='font file', required=True)
    parser.add_argument('-t', '--text', help='text to display', required=True)
    args = parser.parse_args()
    size = args.size.split('x')
    size = (1920, 1080)
    font = ImageFont.truetype(args.font, size[0] // 10)
    text = args.text
    image = Image.new('RGB', size, 'black')
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, (255, 255, 255), font=font)
    colors = randomcolor.RandomColor().generate(2)
    for i in range(size[0]):
        for j in range(size[1]):
            color = colors[0]
            if i < size[0] // 2:
                color = colors[1]
            image.putpixel((i, j), color)
    image.save(args.output)

# run main
if __name__ == '__main__':
    main()