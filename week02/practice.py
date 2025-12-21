song1 = 150
song2 = 210
song3 = input("Enter the duration of song 3 in seconds: ")

song3_int = float(song3)

playlist = song1 + song2 + song3_int
print(f"Total playlist duration in seconds: {playlist}")