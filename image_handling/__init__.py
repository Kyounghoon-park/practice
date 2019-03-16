from image_handling.service import ImageService

if __name__ == '__main__':
    image = ImageService('lena.jpg', 'gray')
    image.changeColor()

