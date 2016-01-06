import os
'''检测dbbean释放'''
global option1,option2,array1,array2
#checkDir = {'InitBaseDBBean.jsp':'baseDbbean.cleanUp()','InitDBBean.jsp':'dbbean.cleanUp()','othersInitBaseDBBean.jsp':'othersBaseDbbean.cleanUp()','XZSPDBBean.jsp':'dbbean.CleanUp()'}
option1 = 'XZSPDBBean.jsp'
array1 = []
option2 = 'dbbean.cleanUp()'
array2 = []
def endWith(filePath):
	return os.path.splitext(filePath)[1]

def getFileList(path,suffix):
    fileList = []
    for root,dirs,files in os.walk(path):
        for file in files:
            fileName = os.path.join(root,file)
            if endWith(fileName) == suffix:
                fileList.append(fileName)
    return fileList
def readFile(filePath):
    file_object = open(filePath)
    for line in file_object:
        if line.find(option1) >0:
            array1.append(filePath)
            break

def getResultFile():
    result = []
    for f in array1:
        flag = False
        file_object = open(f)
        for line in file_object:
            if line.find(option2) >0:
                flag = True
                break
        if not flag:
            result.append(f)

    return result




if __name__ == '__main__':
    path = 'F:\zwdtSjgl\zwdtSjgl'
    suffix = '.jsp'
    fileList = getFileList(path,suffix)
    temp = []
    for f in fileList:
        readFile(f)
    temp = getResultFile()
    logfile = file('XZSPDBBean_unclearup.txt','w+')
    for f1 in temp:
        logfile.writelines(f1)
        logfile.write("\n")
    logfile.close()

 