#!python3
#Scrape_the_web.py scrape what ever you want

import requests,os
from bs4 import BeautifulSoup as bs
from pathlib import Path as path
import pyinputplus as pypi


def manga():
    user=input("\nGive us the link of the manga you want(from this website (https://manganelo.com)):\n")#Link for manga
    while True:
        if not user.startswith('https://chap.manganelo.com'):
            makeSure=input('\nMake sure you get the link from this website(https://manganelo.com)or make sure if you choosed the manga you want:\n')
            if makeSure.startswith('https://chap.manganelo.com'):
                user=makeSure
                break
        else:
            break


    while True:
        try:
            chStart=int(input('\nFrom which chapter do you want to start?:\n'))#need this to go the ordered chapter of the manga

        except:
            print('Enter a number')
            continue
        if chStart:
            break
        if not chStart:
            break
    ch=chStart
    try:
        chEnd=int(input(f"\nYou want to download from chapter{chStart} to? or if you want to download all after don't type anything:\n"))
    except ValueError:
        chEnd=False
        pass
    folderName=input('\nGive us a name to the manga folder you want to download:\n')


    try:
        os.makedirs(f'C:\\Users\\Administrator\\Desktop\\manga\\{folderName}')#The folder which will contain the manga files and chapters folders
    except:
        pass
    link=user+f'/chapter-{chStart}'#create the link which request will go for
    if not chEnd:#If user did't choose an end chapter
        while True:#This allow us to go for another chapter
                res=requests.get(link)
                res.raise_for_status()
                soup=bs(res.text,'html.parser')

                imgElem=soup.select('body > div.body-site > div.container-chapter-reader > img')#Get the css selector for the manga image

                for i in range(len(imgElem)):#Page loop
                    src=imgElem[i].get('src')
                    fullLink=src
                    res=requests.get(fullLink)
                    try:
                        os.makedirs(f'C:\\Users\\Administrator\\Desktop\\manga\\{folderName}\\chapter{str(ch)}')#create the chapter file
                    except:
                        pass
                    animeFile=open(os.path.join(f'C:\\Users\\Administrator\\Desktop\\manga\\{folderName}\\chapter{str(ch)}',os.path.basename(fullLink)),'wb')#file name

                    print(f'Downloading  {fullLink}')
                    for chunk in res.iter_content(100000):#File download
                        animeFile.write(chunk)
                    animeFile.close()
                print(f'Chapter{ch} Is Done')
                nextElem=soup.select('body > div.body-site > div:nth-child(4) > div.panel-navigation > div > a.navi-change-chapter-btn-next.a-h')#Get the css selector for the next button
                try:
                    href=nextElem[0].get('href')#Link for the next chapter
                except IndexError:
                    print(f'Its seems like there is no Chapter {ch+1} or {ch+1}')
                    break

                previous_link=link
                link=href
                checkerLink=os.path.dirname(link)
                checkerPrev=os.path.dirname(previous_link)
                chStart+=1#This is needed to name chapters
                if checkerLink!=checkerPrev:
                    break
        print('Thanks for using this app')
    if chEnd:#if user choose an end chapter
        fullRange=chEnd-chStart
        for i in range(fullRange+1):
            res=requests.get(link)
            res.raise_for_status()
            soup=bs(res.text,'html.parser')

            imgElem=soup.select('body > div.body-site > div.container-chapter-reader > img')#Get the css selector for the manga image

            for i in range(len(imgElem)):#Page loop
                src=imgElem[i].get('src')
                fullLink=src
                res=requests.get(fullLink)
                try:
                    os.makedirs(f'C:\\Users\\Administrator\\Desktop\\manga\\{folderName}\\chapter{str(ch)}')#create the chapter file
                except:
                    pass
                animeFile=open(os.path.join(f'C:\\Users\\Administrator\\Desktop\\manga\\{folderName}\\chapter{str(ch)}',os.path.basename(fullLink)),'wb')#file name

                print(f'Downloading  {fullLink}')
                for chunk in res.iter_content(100000):#File download
                    animeFile.write(chunk)
                animeFile.close()
            print(f'Chapter{ch} Is Done')
            nextElem=soup.select('body > div.body-site > div:nth-child(4) > div.panel-navigation > div > a.navi-change-chapter-btn-next.a-h')#Get the css selector for the next button
            try:
                href=nextElem[0].get('href')#Link for the next chapter
            except IndexError:
                print(f'Its seems like there is no Chapter {ch} or {ch+1}')
                break


            previous_link=link
            link=href
            checkerLink=os.path.dirname(link)
            checkerPrev=os.path.dirname(previous_link)
            ch+=1#This is needed to name chapters
            if checkerLink!=checkerPrev:
                break

        print('Thanks for using this app')





manga()
