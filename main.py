from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    i = 1

    while i < row['Pages']:
        pdf.add_page()
        i = i + 1

pdf.output('output.pdf')
