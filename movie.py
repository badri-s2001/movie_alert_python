from bs4 import BeautifulSoup
import requests
import time
import os

condition = True
count = 0 
while condition == True:
    r = requests.get('https://in.bookmyshow.com/buytickets/master-chennai/movie-chen-ET00110368-MT/20210113')
    print("Refresh: "+str(count)+" Code: "+str(r.status_code))
    count = count+1
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a'):
        name = link.find('strong')
        if name!=None and 'Luxe Cinemas: Chennai' in name.text:
            print("Found")
            os.startfile('song.mp3')
            condition = False
            break
    time.sleep( 20 )