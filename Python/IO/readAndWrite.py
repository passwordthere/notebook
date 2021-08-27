import os
from typing import final

def readAndWrite():
    print( os.getcwd() )
    os.chdir( "C:\\Users\\C5327170\\OneDrive - SAP SE\\Desktop\\notebook\\Python\\IO\\txt" )
    print( os.getcwd() )
    filename = input()

    qq = open( filename, "r+" )
    content1 = qq.read()
    print( content1 )
    qq.write( "UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-46: character maps to <undefined>\n" )
    content2 = qq.read()
    print( content2 )
    qq.close()

try:
    readAndWrite()
except IOError:
    print("文件不存在")
finally:
    readAndWrite()