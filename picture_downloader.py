#!python3
#imgur.py-Scrape photos from imgur website

def imgur():
    global imgurName,imgurFullLink,imgurFoldersName,imgurNumber,imgurFilesName,imgurImageName

    imgurName=input("The name of the picture's that you want to download pls:\n")
    imgurNumber=input('\nHow many images do you want to download?\n\n(if you want all dont type anything)\n')
    imgurFoldersName=input('\nWhat you want the name of the folder (which will contain the pic you want to download):\n')
    imgurFilesName=input('\nPls give us a name to rename the pictures:\n')

    try:#put try here just to make sure that the program won't crash if the folder is already exists
        os.makedirs(f'C:\\Users\\Administrator\\Desktop\\pic_downloader\\imgur\\{imgurFoldersName}')#create a new folder on desktop

    except FileExistsError:
        pass

    url=f'https://imgur.com/search?q={imgurName}'
    res=requests.get(url)#send requests
    res.raise_for_status()
    picSoup=bs(res.text,'html.parser')
    imgHtml=picSoup.select('img')#Want to download an img

    if imgurNumber:

        for i in range(int(imgurNumber)):
                photoLink=imgHtml[i].get('src')#Get the link
                imgurFullLink=f'https:'+photoLink#Get the full link
                res=requests.get(imgurFullLink)#Send request to the photo link

                print(f'\n\nDownloading {imgurFullLink}')
                imgurImageFile=open(os.path.join(r'C:\Users\Administrator\Desktop\pic_downloader\imgur',os.path.basename(imgurFullLink)),'wb')
                imgurImageName=os.path.join(r'C:\Users\Administrator\Desktop\pic_downloader\imgur',os.path.basename(imgurFullLink))

                for chunk in res.iter_content(100000):
                        imgurImageFile.write(chunk)
                imgurImageFile.close()
                rename()
    if not imgurNumber:
        for i in range(len(imgHtml)):
            photoLink=imgHtml[i].get('src')#Get the link
            imgurFullLink=f'https:'+photoLink
            res=requests.get(imgurFullLink)
            res.raise_for_status()

            print(f'\n\nDownloading {imgurFullLink}')
            imgurImageFile=open(os.path.join(r'C:\Users\Administrator\Desktop\pic_downloader\imgur',os.path.basename(imgurFullLink)),'wb')
            imgurImageName=os.path.join(r'C:\Users\Administrator\Desktop\pic_downloader\imgur',os.path.basename(imgurFullLink))

            for chunk in res.iter_content(100000):
                imgurImageFile.write(chunk)
            imgurImageFile.close()
            rename()




def rename():
    renamePath=r'C:\Users\Administrator\Desktop\pic_downloader\imgur'
    global x
    x=1


    imgurFullPath=path(imgurImageName)#get image full path
    imgurFileType=imgurFullPath.suffix#get the file extension
    imgurFileNewname=path(f'C:\\Users\\Administrator\\Desktop\\pic_downloader\\imgur\\{imgurFoldersName}')/f'{imgurFilesName}{x}{imgurFileType}'

    while os.path.exists(imgurFileNewname):#if file name already exsits (like if the user downloaded the pic before)
        x+=1#add 1 to x until it be bigger than the last file name
        try:
            imgurFileNewname=path(f'C:\\Users\\Administrator\\Desktop\\pic_downloader\\imgur\\{imgurFoldersName}')/f'{imgurFilesName}{x}{imgurFileType}'#trying to create a new file name that is not used before by adding 1to x value


        except:
            pass
        if not os.path.exists(imgurFileNewname):#if it found a new name then it will exit the loop
            break

    print(f'\n\nRenameing  C:\\Users\\Administrator\\Desktop\\pic_downloader\\imgur\\{os.path.basename(imgurFullLink)} to {imgurFileNewname}\n\n')
    os.rename(f'C:\\Users\\Administrator\\Desktop\\pic_downloader\\imgur\\{os.path.basename(imgurFullLink)}',imgurFileNewname)

    x+=1
    
    
imgur()
