from fpdf import FPDF

def main():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.text(50, 50, "CS50 Shirtificate")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
