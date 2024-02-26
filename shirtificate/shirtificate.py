from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(20)

def main():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
