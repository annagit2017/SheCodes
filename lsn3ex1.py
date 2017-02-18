import random
import urllib.request

random_name = random.randrange (1, 1000) # Create new variable and assign it randomised numerical param

#At this stage use 'print (random_name)' to print out randomised number and confirm random function works as expected

image_name = str(random_name) + '.png' # We combine numerical value and string, therefore it is required to convert integer to string by using str()

# At this stage use 'print (image_name)' to confirm you create image name correctly

url = 'https://goo.gl/QRNysq'

urllib.request.urlretrieve(url, image_name)
