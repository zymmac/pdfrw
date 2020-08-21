import sys
import os
import re
from pdfrw import PdfReader, PdfWriter


rootdir = 'C:/Users/ZymmAc/Desktop/BibliotecaCalibre'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.pdf'):
            pdf = os.path.join(subdir, file)
            folder = subdir
            meta = os.path.join(subdir, "metadata.opf")
            print("Pdf File: " + pdf + "\n \n Folder: " + folder + "\n \n Meta: " + meta + "\n \n")

            with open (meta, encoding="utf8") as myfile:
                contents = myfile.read()
            patternTitle = re.compile(r'(?<=>).+(?=</dc:title)')
            PatternAuthor = re.compile(r'(?<=>).+(?=</dc:creator)')

            title = patternTitle.search(contents).group(0)
            author = PatternAuthor.search(contents).group(0)

            inpfn = pdf
            outfn = 'new.' + os.path.basename(inpfn)

            trailer = PdfReader(inpfn)
            trailer.Info.Title = title
            trailer.Info.Author = author
            PdfWriter(outfn, trailer=trailer).write()
