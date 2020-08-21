import os
rootdir = 'C:/Users/ZymmAc/Calibre Library'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.pdf'):
            pdf = os.path.join(subdir, file)
            folder = subdir
            meta = os.path.join(subdir, "metadata.opf")
            print(pdf)
            print(folder)
            print(meta)
