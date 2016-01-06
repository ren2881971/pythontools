import os
'''检索目录下文件 并替换内容'''
global findStr
findStr='zwdt.jl.gov.cn'
global replaceStr
replaceStr= 'www2.jl.gov.cn'
def getFileList(path):
    fileList = []
    for root,dirs,files in os.walk(path):
        for file in files:
            fileName = os.path.join(root,file)
            fileList.append(fileName)
    return fileList

def replaceFiles(filepath):
    file_object = open(filepath)
    for line in file_object:
        if line.find(findStr)>0:
            line.replace(findStr,replaceStr,3)


if __name__ == '__main__':
    path='F:\zwdtSjgl\zwdtSjgl'
    fileList = getFileList(path)
    for filepath in fileList:
        replaceFiles(filepath)
    

