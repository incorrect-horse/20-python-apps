from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="letter")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv", sep=",")

for index, row in df.iterrows():
    pdf.add_page()

    #header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)

    #make lines
    line_count = 0
    while line_count < 250:
        pdf.line(10, 21 + line_count, 200, 21 + line_count)
        line_count += 10
#    for i in range(20, 280, 10):
#        pdf.line(10, i, 200, i)

    #footer
    pdf.ln(245)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        #make lines
        line_count = 0
        while line_count < 250:
            pdf.line(10, 21 + line_count, 200, 21 + line_count)
            line_count += 10

        #footer
        pdf.ln(257)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
