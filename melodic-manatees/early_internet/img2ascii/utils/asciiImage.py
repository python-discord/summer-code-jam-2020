#
# This code is under MIT licence, you can find the complete file here: https://github.com/electronut/pp
#

from PIL import Image


class asciiImage():
    def __init__(self, image):
        self.gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~()i!lI;:,\"^`'. "
        # 10 levels of gray
        self.gscale2 = '@%#*+=-:. '

        self.image = Image.open(image).convert('L')
        self.w = self.image.size[0]
        self.h = self.image.size[1]

    def getAverageL(self, loadedImage, x, y):
        avg = 0
        for c in range(x):
            for r in range(y):
                avg += loadedImage[c, r]
        return avg / (x * y)

    def convertImageToAscii(self, cols, scale, moreLevels):
        w = self.w / cols
        h = w / scale

        rows = int(self.h / h)
        if cols > self.w or rows > self.h:
            cols = self.w
            rows = self.h

        aimg = []
        # generate list of dimensions
        for j in range(rows):
            y1 = int(j*h)
            y2 = int((j+1)*h)

            # correct last tile
            if j == rows-1:
                y2 = self.h

            # append an empty string
            aimg.append("")

            for i in range(cols):

                # crop image to tile
                x1 = int(i*w)
                x2 = int((i+1)*w)

                # correct last tile
                if i == cols-1:
                    x2 = self.w
                # crop image to extract tile
                img = self.image.crop((x1, y1, x2, y2))

                # get average luminance
                avg = int(self.getAverageL(
                    img.load(), img.size[0], img.size[1]))

                # look up ascii char
                if moreLevels:
                    gsval = self.gscale1[int((avg*69)/255)]
                else:
                    gsval = self.gscale2[int((avg*9)/255)]

                # append ascii char to string
                aimg[j] += gsval

        # return txt image
        return aimg


if __name__ == "__main__":
    imageFile = "/Users/elee/Desktop/test.jpeg"
    inst = asciiImage(imageFile)
    print(inst.convertImageToAscii(100, 1, True))
