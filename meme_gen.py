'''
Small script to make a meme generator. This means introduce text in a image
Author: Lenin G Falconi
Date> 27/03/19
'''

import cv2
import argparse
import os
import sys
import re
import numpy as np

# Display Message

def writeMessage(image, text_message):
    height, width, dim = np.shape(image)
    print(width, height, dim)
    font_position_x, font_position_y = 10,30
    font_type = cv2.FONT_HERSHEY_PLAIN
    font_scale = 1
    font_color = (255,255,255)
    lineType = 2
    thickness = 2
    i_out = cv2.putText(image, text_message,
                (font_position_x, font_position_y),
                font_type,
                font_scale,
                font_color,
                thickness,
                lineType)
    size = cv2.getTextSize(text_message,
                font_type,
                font_scale,
                thickness)
    print(size)
    return i_out


def stampText(image, text, line):
    # https://stackoverflow.com/questions/27647424/opencv-puttext-new-line-character/27647540
    # https://www.programcreek.com/python/example/89323/cv2.getTextSize

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.55
    margin = 5
    thickness = 2
    color = (255, 0, 0)

    size = cv2.getTextSize(text, font, font_scale, thickness)
    # print(size)
    text_width = size[0][0]
    text_height = size[0][1]
    line_height = text_height + size[1] + margin

    x = image.shape[1] - margin - text_width
    y = margin + size[0][1] + line * line_height

    cv2.putText(image, text, (x, y), font, font_scale, color, thickness)
    # cv2.putText(img, line, (50, y), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    # img_out = cv2.putText(image, text, (x, y), font, font_scale, color, thickness)

    # return img_out


def main():
    # The argparse part:
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    ap.add_argument("-t", "--text", required=True, help="Text to put in image. Lines separated with")

    args = vars(ap.parse_args())

    print("Welcome to Meme Generator with OpenCV")
    print("email: enteatenea@gmail.com")
    print(args)

    # img = cv2.imread('pacoMonc.jpg')
    img = cv2.imread(args["image"])
    print('image size is ', img.shape)
    # meme = writeMessage(img, 'HelloPaco')
    # text = 'Bueno compatriotas, \n Ahora a prerpararse para el 2020 \n para continuar en mi oficio de \n dividir votos.'
    text = args["text"]

    # Regex cleaning string input
    regex = r"(\\n)"
    subst = "\n"
    result = re.sub(regex, subst, text, 0, re.MULTILINE)
    # print(result)

    for i, line in enumerate(result.split("\n")):
        stampText(img, line, i)
    # stampText(img, 'Bueno compatriotas, \n Ahora a prerpararse para el 2020 \n para continuar en mi oficio de \n dividir votos.', 0)
    # stampText(img, 'Ahora a preparase para el 2020', 1)
    # stampText(img, 'para continuar en mi oficio de', 2)
    # stampText(img, 'dividir los votos', 3)
    cv2.imwrite('meme.jpg', img)
    cv2.imshow('Memme', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


# References:
# https://www.pyimagesearch.com/2014/06/02/opencv-load-image/