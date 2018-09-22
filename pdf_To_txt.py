import PyPDF2

pdf_name = 'ansible-essential-7-4.pdf'
pdfObj = open(pdf_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfObj)

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    text = pageObj.extractText()
f = open("1password.txt" , "w")
f.write(text)