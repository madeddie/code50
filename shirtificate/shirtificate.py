from fpdf import FPDF

def main():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.cell(w=0,h=0,text="CS50 Shirtificate",align='C')
    pdf.image("shirtificate.png", x=0, y=20)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
