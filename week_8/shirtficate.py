from fpdf import FPDF

pdf = FPDF()
s = input('Enter name: ')
pdf.add_page()
pdf.image('shirtificate.png')
pdf.set_font('Arial',size=40,style='B')
pdf.text(50,100,(s+' took CS50'))
pdf.set_xy(0,0)
pdf.output('shirtificate.pdf')