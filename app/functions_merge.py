from PyPDF2 import PdfWriter

merger = PdfWriter()


def local(loc):
    return 0


def merge(a1,a2):
    arquivo1 = open(a1,"rb")
    arquivo2 = open(a2,"rb")

    merger.append(fileobj=arquivo1, pages=(0, 1))
    merger.merge(position=2, fileobj=arquivo2, pages=(0, 1))

    output = open("arquivo_junto.pdf", "wb")
    merger.write(output)
    merger.close()
    output.close()
