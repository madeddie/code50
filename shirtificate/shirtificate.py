from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.cell(w=0,h=0,text="CS50 Shirtificate",align="C")
    pdf.image("shirtificate.png", x=10, y=20, w=pdf.epw)
    pdf.set_text_color(255)
    pdf.cell(w=-180,h=150,text=f"{name} took CS50",align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
