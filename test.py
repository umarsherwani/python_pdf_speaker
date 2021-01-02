import pyttsx3
import PyPDF2

#just place the pdf file name and location of file (location must be at same location where your program Run) 
# don't forget the mode i.e 'rb' when you open file 
book = open('cybercrimeciteseerx.pdf','rb')
pdfreader =PyPDF2.PdfFileReader(book)

# Give you the number of pages
pages = pdfreader.numPages
print(pages)

# always use init for intialize the pyttsx3
speaker = pyttsx3.init()
for _ in range(0,pages):
    #get page  always takes argument
    page = pdfreader.getPage(0)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()