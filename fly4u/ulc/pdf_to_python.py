# -*- coding: utf-8 -*-
import PyPDF2
from django.contrib.admin.utils import flatten

# list of trafficed cities from polish airports whith IATA codes. Data of ULC.
# most...[1] - volume of passengers in 2019, most...[2] - volume of passengers in 2018
most_trafficed_cities = [['Londyn', 3631821, 3471676, "LCY", "LHR", "LGW", "LTN", "STN", "SEN"],
                               ['Frankfurt', 1248325, 1271942, "FRA"],
                               ['Oslo', 1176673, 1063840, "OSL"], ['Monachium', 902552, 835166, "MUC"],
                               ['Kijów', 864607, 543247, "IEV", "KBP"], ['Paryż', 762917, 757066, "CDG", "ORY", "BVA"],
                               ['Amsterdam', 726950, 618157, "AMS"], ['Sztokholm', 704603, 747343, "ARN", "BMA", "VST", "NYO"],
                               ['Bruksela', 628976, 618787, "BRU", "CRL"], ['Mediolan', 616536, 591644, "MXP", "LIN", "BGY"],
                               ['Dublin', 596900, 590486, "DUB"],  ['Eindhoven', 580927, 500249, "EIN"],
                               ['Tel Aviv', 520823, 568768, "TLV"], ['Kopenhaga', 506334, 450051, "CPH"],
                               ['Rzym', 489098, 439234, "FCO", "CIA"], ['Barcelona', 436253, 480710, "BCN", "GRO", "REU"],
                               ['Wiedeń', 416203, 261039, "VIE"], ['Dortmund', 392947, 387420, "DTM"],
                               ['Lwów', 352455, 224744, "LWO"], ['Liverpool', 333469, 350263, "LPL"],
                               ['Zurych', 326621, 291417, "ZRH"], ['Ateny', 319748, 299465, "ATH"],
                               ['Bristol', 317141, 294363, "BRS"], ['Manchester', 297617, 261464, "MAN"],
                               ['Helsinki', 297135, 197683, "HEL"]]

most_trafficed_cities_flat = flatten(most_trafficed_cities)

# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfpage import PDFPage
# from io import BytesIO
#
# def pdf_to_text(path):
#     manager = PDFResourceManager()
#     retstr = BytesIO()
#     layout = LAParams(all_texts=True)
#
#     device = TextConverter(manager, retstr, laparams=layout)
#
#     filepath = open(path, 'rb')
#     interpreter = PDFPageInterpreter(manager, device)
#
#     for page in PDFPage.get_pages(filepath, check_extractable=True):
#         interpreter.process_page(page)
#
#     tekst = retstr.getvalue()
#
#     filepath.close()
#     device.close()
#     retstr.close()
#
# #     return tekst
#
#
# if __name__ == "__main__":
#     text = pdf_to_text("/home/revorete/PycharmProjects/travel4u_project/fly4u/ulc/wg_metropolii_regularne_kw32019.pdf")
#     print(text)
def to_python_cities():
    pdf_file = open('wg_metropolii_regularne_kw32019.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf_file)

    # pobieram tylko DRUGĄ stronę z dokumentu
    pageObj = pdfReader.getPage(1)
    text = pageObj.extractText()
    polskie_znaki = ("Kijów", "Paryż", "Wiedeń", "Lwów")
    text = text[37:].split('\n')
    # wycinam tylko potrzebne dane z STR
    list = [text[i:i + 7] for i in range(0, len(text), 7)]
    list = list[:-2]
    k = 0

    new_list = []

    for l in list:
        # dodaję miasta z polskimi znakami, zaimportowane jako null
        if l[0] == '':
            l[0] = polskie_znaki[k]
            k += 1

        # nowa lista tylko z danymi interesującymi plus zmiana wartości na integer
        l[2] = int(l[2].replace(" ", ""))
        l[5] = int(l[5].replace(" ", ""))
        new_list.append([l[0], l[2], l[5]])

    # [print(l) for l in new_list]
    print(new_list)

    pdf_file.close()


if __name__ == "__main__":
    to_python_cities()