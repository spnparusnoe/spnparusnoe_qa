import PyPDF2

class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pdf_data = self._read_pdf()

    def _read_pdf(self):
        pdf_data = {}
        with open(self.file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                text = page.extract_text()  # extracting the text
                if text:  # checking of the exctracting
                    pdf_data[f'Page_{i + 1}'] = text
                else:
                    pdf_data[f'Page_{i + 1}'] = ""
        return pdf_data

    def get_data(self):
        return self.pdf_data

class PDFComparator:
    def __init__(self, ethalon_pdf_reader):
        self.ethalon_data = ethalon_pdf_reader.get_data()

    def compare_with(self, test_pdf_reader):
        test_data = test_pdf_reader.get_data()

        if len(test_data) != len(self.ethalon_data):
            print("incongruity: the number of pages doesn't match")
            return False

        for page, ethalon_text in self.ethalon_data.items():
            test_text = test_data.get(page, "")
            if test_text != ethalon_text:
                print(f"incongruity on {page}")
                return False

        print("PDF is match to ethalon")
        return True

# reading the file
ethalon_path = "C:\\Users\\spnpa\\Desktop\\pythonProject\\ERP_for_US\\test_task.pdf"  #change to ur local path
ethalon_pdf_reader = PDFReader(ethalon_path)

# creating of the object of the comparation
comparator = PDFComparator(ethalon_pdf_reader)

# creating testing file and comparation
test_file_path = "C:\\Users\\spnpa\\Desktop\\pythonProject\\ERP_for_US\\test_task.pdf"  #change to ur local path
test_pdf_reader = PDFReader(test_file_path)

# comparaion
is_match = comparator.compare_with(test_pdf_reader)
