# https: // google-images-download.readthedocs.io/en/latest/arguments.html
# importing google_images_download module
import subprocess
import time
from google_images_download import google_images_download
# creating object
response = google_images_download.googleimagesdownload()

search_queries = ["bottle"]
ip_addrs = ["138.199.58.87"]

limit = 100


def downloadimages(query):
    arguments = {
        "keywords": query,
        "format": "jpg",
        "limit": limit,
        "print_urls": True,
        # "size": "medium",
        # "aspect_ratio": "panoramic",
        "chromedriver": "./chromedriver.exe",
        "output_directory": "./",
        "image_directory": "./image.png",
        # "prefix": "000",
        # "specific_site": "wikipedia.org",
        # "proxy": ""
    }
    try:
        # for ip in ip_addrs:
        # arguments["proxy"] = ip
        response.download(arguments)

    # Handling File NotFound Error
    except FileNotFoundError:
        arguments["aspect_ratio"] = ""

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            pass


def getImages():
    for query in search_queries:
        downloadimages(query)


# Driver Code
# while True:
#     getImages()
#     subprocess.call(['sh', './image.png/adjFilename.sh'])
#     time.sleep(1)

getImages()
