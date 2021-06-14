from pytube import YouTube

# where to save
SAVE_PATH = "G:\\Videos\\"  # to_do

# link of the video to be downloaded
link = ["https://www.youtube.com/watch?v=tDb3FncQvJM",
        "https://www.youtube.com/watch?v=7OX6ISEFDHA&ab_channel=Infraction-NoCopyrightMusicInfraction-NoCopyrightMusicVerified"
        ]

for i in link:
    try:
        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(i)
        print(yt.title)
    except:
        # to handle exception
        print("Connection Error")



    print("********************Download video*************************")
    # get all the stream resolution for the
    for stream in yt.streams:
        print(stream)

    # set stream resolution
    my_video = yt.streams.get_highest_resolution()

    # or
    # my_video = my_video.streams.first()

    # Download video
    #my_video.download()


    try:
        # downloading the video
        my_video.download(SAVE_PATH)
    except:
        print("Some Error!")
print('Task Completed!')








