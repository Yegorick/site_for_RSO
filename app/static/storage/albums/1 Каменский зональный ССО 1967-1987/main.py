import zipfile

file_z = zipfile.ZipFile('D:\\Projects\\Site\\app\\static\\storage\\albums\\1 Каменский зональный ССО 1967-1987\\1 Каменский зональный ССО 1967-1987.zip', 'r')

file_z.printdir()

file_z.close()
