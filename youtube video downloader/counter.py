import os

count = -1
directory2 = os.getcwd() + "\Downloads"
downloads = os.listdir(directory2)

for i in downloads:
    count += 1