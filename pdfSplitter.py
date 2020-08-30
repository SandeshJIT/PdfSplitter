from PyPDF2 import PdfFileWriter,PdfFileReader
def cropper(start,end,file):
    inputPdf=PdfFileReader(open(file,"rb"))
    outputPdf=PdfFileWriter()
    ostream = open(file.split(".")[0]+"cropped"+".pdf","wb")
    start=start-1
    end=end-1
    while start<=end:
        outputPdf.addPage(inputPdf.getPage(start))
        outputPdf.write(ostream)
        start+=1
    ostream.close()
