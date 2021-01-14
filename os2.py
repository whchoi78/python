import os.path

#해당 폴더가 존재하는지 확인 
print(os.path.exists("C:/리눅스/가상머신"))

#디렉터리인지 아닌지 확인
print(os.path.isdir("C:/리눅스/가상머신"))

#파일인지 아닌지 확인
print(os.path.isfile("C:/리눅스/DNS"))

#해당 경로의 하위 디렉터리와 파일의 이름을 나타내줌
for dirName, subDirList, fnames in os.walk("C:/리눅스/"):
    #print(dirName)
    #print(subDirList)
    #print(fnames)
    for fname in fnames:
        print(os.path.join(dirName, fname))