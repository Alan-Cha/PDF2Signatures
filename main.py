# importing required modules
import PyPDF2

# given the number of pages in a booklet, return an array with the appropriate
# order
#
# NOTE: the numbers of pages must be divisable by 4 because each page will be
# divided into 4 pages
def pageOrder(numOfPages):
    # used to flip the order of pages depending on the side of the sheet
    flipSide = False

    # checking numOfPages
    if (not isinstance(numOfPages, int)) or numOfPages % 4 != 0 or numOfPages <= 0:
        raise ValueError('Incorrect number of pages per booklet')

    order = []

    for current in range(int(numOfPages / 2)):
        if flipSide:
            order.append(current)
            order.append((numOfPages - 1) - current)
        else:
            order.append((numOfPages - 1) - current)
            order.append(current)

        flipSide = not flipSide

    return order

# creating a pdf file object
# TODO: Get input and output file locations from arguments
pdfFileObj = open('Chinese Lion Dancing Explained.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

print(pageOrder(8))

# # creating a page object
# pageObj = pdfReader.getPage(0)
#
# # extracting text from page
# print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
