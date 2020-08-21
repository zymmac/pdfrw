import re

with open ('metadata.opf', encoding="utf8") as myfile:  # Open lorem.txt for reading text.
    contents = myfile.read()
patternTitle = re.compile(r'(?<=>).+(?=</dc:title)')
PatternAuthor = re.compile(r'(?<=>).+(?=</dc:creator)')

title = patternTitle.search(contents)
author = PatternAuthor.search(contents)

print(title)
print(author)
