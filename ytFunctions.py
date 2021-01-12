from pytube import YouTube

link = "https://www.youtube.com/watch?v=u2ExIOHzXO0&ab_channel=watchvines"

yt = YouTube(link)
print(yt.title)

stream = yt.streams.first()
stream.download('/Users/louis/Desktop')
print('Done')