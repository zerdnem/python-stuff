import os

def clean_filenames():
    fileList = os.listdir(os.curdir)
    for item in fileList:
  newName = item.replace(' ', '_').lstrip('1234567890').lower().translate(None, '+=)(*&^%$#@!')
  os.rename(item, newName)

    for item in fileList:
  if os.path.isdir(item):
    os.chdir(item)
    clean_filenames()
    os.chdir('../')

myPath = raw_input('Enter path to begin cleaning: ')
os.chdir(myPath)
clean_filenames()

