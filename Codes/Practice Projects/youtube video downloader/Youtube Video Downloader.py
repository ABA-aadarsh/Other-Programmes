from pytube import YouTube
link=input("Enter youtube video link: ")
# link="https://youtu.be/EAYlckSaviI"
try:
    intype=int(input("Enter :\n1 for Video\n2 for Audio\n::"))
    data=YouTube(link)
    if intype==1:
        x=data.streams
        streamlist=[]
        for i in x:
            if "progressive=\"True\"" in str(i):
                if "video/mp4" in str(i):
                    streamlist.append(i)
        for z,i in enumerate(streamlist):
            index=str(i).find("res")
            print(f"Num:{z}\t\t",str(i)[index:index+10])
        strm=int(input("\nEnter Num: "))
        print("Wait. Downloading.....")
        streamlist[strm].download()

    elif intype==2:
        x=data.streams.filter(only_audio=True)
        for z,i in enumerate(x):
            index1=str(i).find("mime_type")
            index2=str(i).find("abr=\"")
            print(f"Num: {z}",str(i)[index1:index1+22],str(i)[index2:index2+13])
        strm=int(input("Enter Num: "))
        print("Wait. Downloading......")
        x[strm].download()
    print("Downloaded Successfully")
    temp=input("")
except:
    print("Error occured. Check the link and input.")
