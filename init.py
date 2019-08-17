import zipfile

from zipfile import ZipFile
zf = ZipFile('./data.zip', 'r')
zf.extractall('./')
zf.close()

zf = ZipFile('chest_xray.zip', 'r')
zf.extractall('./')
zf.close()