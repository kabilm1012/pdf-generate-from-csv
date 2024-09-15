from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

# Page Break shouldn't take place automatically
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)
    pdf.set_line_width(0.5)
    pdf.line(x1=10, y1=20, x2=200, y2=20)

    # Add lines with 10mm space
    for y in range(30, 298, 10):
        pdf.set_line_width(0.1)
        pdf.line(10, y, 200, y)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R", ln=1)

    for i in range(row['Pages'] - 1):
        pdf.add_page()

        # Add lines with 10mm space
        for y in range(20, 298, 10):
            pdf.set_line_width(0.1)
            pdf.line(10, y, 200, y)

        # Set the footer
        pdf.ln(265+12)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R", ln=1)

pdf.output('output.pdf')
