import urllib.request
import cv2 as cv
import numpy
import os

def store_imgs(url):
    image_urls = urllib.request.urlopen(url).read().decode()
    pic_num = 1
    for i in image_urls.split('\n'):
        try:
            print(pic_num,i)
##            edit the path according where you want to save the images
            urllib.request.urlretrieve(i,str(pic_num)+'.jpg')
            pic_num += 1
        except Exception as e:
            print(e)
    
if __name__ == '__main__':
##    url of the page that contains the urls of images
    url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    store_imgs(url)
