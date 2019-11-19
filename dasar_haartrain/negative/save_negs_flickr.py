import flickrapi as flickr
##import urllib
import xml.etree.ElementTree as ET
import cv2 as cv
import urllib
key = ''
secret = ''

flickr = flickr.FlickrAPI(api_key = key, secret = secret,)

def search(tags):
    count = 1
    
    photos =flickr.walk(tags = tags,tag_mode='all',per_page = 5000, extras='url_c')
    
    for photo in photos:
        try:
##                print('photo',photo.keys())
                pic_id=photo.get('id')
                
                sizes=flickr.photos.getSizes(photo_id=pic_id)[0]
##                    print(ET.dump(sizes))
                size=sizes.find("./size[@label='Large']")
                url=size.get('source')
##                    print('small source:',url)

                urllib.request.urlretrieve(url,pic_id +".jpg")
                print(count,'pic saved')
                count += 1
                
        except Exception as e:
                print(e)
    cv.waitKey(0)

if __name__ == '__main__':
    urls = search('happy')
