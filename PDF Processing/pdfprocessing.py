import PyPDF2
import re
# with open('dummy.pdf', 'rb') as file: # rb is for read bytes as to read the pdf we have to read in bytes
#     reader = PyPDF2.PdfFileReader(file)
#     page  = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)

textArr= []
reader = PyPDF2.PdfFileReader("w17.pdf")
total_pg = reader.getNumPages()
for i in range(0, total_pg):
    page = reader.pages[i]
    
    text = page.extractText()
    writer = PyPDF2.PdfFileWriter()
    textArr.append(text)

# Define the regular expression pattern to match the word "EITHER"
pattern1 = r'\bEITHER\d\b'

# Use the split() method of the re module to split the text string
substrings = re.split(pattern1, textArr[0])[1:]
# print(substrings)

pattern = r'\([A-Z]\)([^.]+)'


# Use the findall() method of the re module to find all matches
matches = re.findall(pattern,  textArr[0])

# Print the array of substrings
print(matches)