import os

print(os.getcwd())
os.chdir("C:\\Users\\C5327170\\OneDrive - SAP SE\\Desktop\\notebook\\Python\\IO")
print(os.getcwd())
if(os.path.isdir("txt")):
    pass
else:
    os.mkdir("txt")
os.chdir("txt")
print(os.getcwd())

qq = open("qq.txt", "a+")
content1 = qq.read(10)
print(content1)
qq.write( "UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-46: character maps to <undefined>\n" )
content2 = qq.read(20)
print(content2)
qq.close()