# What You Will Learn :
# OOP
# Modules
# Instructions :
# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.
import time
import requests

# solution1
URL = 'https://www.google.ru/?client=safari'
loading_time = requests.get(URL).elapsed.total_seconds()
print(loading_time)



# solution2
def loading_time(url):
    start = time.time()
    f = requests.get(url)
    end = time.time()
    print(end - start)

loading_time('https://www.google.ru/?client=safari')