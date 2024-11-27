import os

try:
    os.rename('donkeyfile.txt','donkeyfilerenamed.txt')

    os.rename('donkeyfilerenamed.txt','donkeyfile.txt')
except Exception as e:
    print(f"An error ocurred. {e}")
