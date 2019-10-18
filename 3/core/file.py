from os import listdir, makedirs
from os.path import isfile, join, exists
import shutil


def walkFolder(examplePath):
  return [
      join(examplePath, f)
      for f in listdir(examplePath)
      if isfile(join(examplePath, f))
  ]


def copyFile(origin, dest):
  shutil.copy(origin, dest)


def makeDir(path):
  if not exists(path):
    makedirs(path)
