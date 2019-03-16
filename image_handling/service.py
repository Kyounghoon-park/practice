import cv2
import matplotlib.image as plt


class ImageService:
    def __init__(self, fname, color_name):
        self.fname = fname
        self.color_name = color_name

    def changeColor(self):
        result = ''
        if self.color_name == 'original':
            result = cv2.imread(self.fname, cv2.IMREAD_COLOR)
        elif self.color_name == 'gray':
            result = cv2.imread(self.fname, cv2.IMREAD_GRAYSCALE)
        #cv2.imshow('result', result)
        #cv2.waitKey(0)

        plt.imsave('change_result.jpg', result)
