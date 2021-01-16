import re
import sys

def GetText(path):
    if(path == 'test'):
        path = "test.txt"
    dataString = ""
    if('.' not in path or path.split('.')[-1] != "txt"):
        print("File should have txt extension, press Enter to exit")
        sys.exit()
    try:
        file = open(path)
        data = file.readlines()
        dataString = '\n'.join(data)
    except:
        input("Unable to load the file, press Enter to exit")
        sys.exit()
    return dataString

def GetKey(data, exKey):

    mKey = re.search(exKey, data)
    key =""
    try:
        key = mKey.group('key')
    except:
        input("Unable to find key, key should be written as 'key: ...', press Enter to exit")
        sys.exit()
    return key

def GetOccurences(data, key):
    start = 0
    stop = len(key)
    output = []
    while(stop <= len(data)):
        isCorrect = CheckValue(data[start:stop], key, len(key)-1)
        if(isCorrect):
            output.append((start,stop-1))
        stop += 1
        start += 1
    return output

def CheckValue(input, key, stop):
    while(stop >= 0):
        if(input[stop] == key[stop]):
            return CheckValue(input[:-1], key[:-1], stop-1)
        return False
    return True 

def ExportData(path, occurences):
    if(path == 'test'):
        path = "output.txt"
    if('.' not in path or path.split('.')[-1] != "txt"):
        print("File should have txt extension, press Enter to exit")
        sys.exit()
    try:
        file = open(path, "w")
        file.write("Indexes of the occurrence of a given string (from: to), counted from zero:\n")
        file.write(str(occurences))
        file.write("\nNumber of appearances:\n")
        file.write(str(len(occurences)))
        file.close()
    except:
        input("Unable to write to file, press Enter to exit")

path = input("Enter the path to the text file, type 'test' to use the test file ")


data = GetText(path)
print("File content:\n" + data)
exKey = 'key:\s*(?P<key>.*)'
key = GetKey(data, exKey)
print("Recognized key:\n" + key)
data = re.sub(exKey, "", data).strip()
occurences = GetOccurences(data, key)

output = input("Enter the output path, type test to use test path ")
ExportData(output, occurences)

