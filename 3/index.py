from core.ext import analysisImage
from core.file import walkFolder, makeDir, copyFile
import time


def append(map, key, imageInfo):
  tempList = map.get(key)
  if not tempList:
    tempList = []
    map[key] = tempList
  tempList.append(imageInfo)


def move(map, parentPath):
  for key, value in map.items():
    folder = parentPath + key
    makeDir(folder)
    for (datetime, address, file) in value:
      sections = file.split('/')
      copyFile(file, folder + '/' + sections[-1])


dateMap = {}
addressMap = {}
fileList = walkFolder('./example-ext')
for file in fileList:
  print('处理图片： ' + file)
  (imageTime, address) = analysisImage(file)
  if imageTime and address:
    datetime = time.strptime(str(imageTime), "%Y:%m:%d %H:%M:%S")
    imageInfo = (datetime, address, file)

    append(dateMap, time.strftime("%Y-%m-%d", datetime), imageInfo)
    append(addressMap, address.replace(' ', '').replace(',', '-'), imageInfo)

move(dateMap, './result/date/')
move(addressMap, './result/address/')
