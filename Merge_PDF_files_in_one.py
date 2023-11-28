from pypdf import PdfMerger

pdfs = ['1.pdf', '2.pdf', '3.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("Kishor_dhakal_documents.pdf")
merger.close()