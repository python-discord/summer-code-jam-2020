from django.shortcuts import render
from django.http import HttpResponse
from .utils.asciiImage import asciiImage
# Create your views here.


def main(request):
    imageFile = "media/test.jpeg"
    inst = asciiImage(imageFile)
    textImage = inst.convertImageToAscii(100, 0.4, False)
    res = "<div>"
    res += "<p style = 'font-family: \"Courier New\"' >"
    for i in textImage:
        res += i + "<br>"
    res += "</div>"
    return HttpResponse(res)
