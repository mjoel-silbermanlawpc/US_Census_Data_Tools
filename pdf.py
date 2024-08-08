from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
import matplotlib.pyplot as plt




def create_pdf(df, filename):

    cc = df.iloc[0,-2]
    cc_title = df.iloc[0,-1]
    cc_with_title = str(cc) + " - " + cc_title
    female_percent = df.iloc[0, 4]
    black_percent = df.iloc[0, 12]
    hispanic_percent = df.iloc[0, 6]
    asian_percent = df.iloc[0, 18]
    am_indian_percent = df.iloc[0, 21]
    pac_hawaiian_percent = df.iloc[0, 22]
    two_or_more_percent = df.iloc[0, 24]
    white_percent = df.iloc[0, 9]
    minority_percent = black_percent + hispanic_percent + asian_percent + am_indian_percent + two_or_more_percent


    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setLineWidth(1)
    c.setStrokeColorRGB(0, 0, 0)
    border_padding = 0.4
    c.rect(border_padding * inch, border_padding * inch, width - 2*border_padding * inch, height - 2*border_padding * inch)

    # Set title and subtitle
    title = "Some Business Name - 8/7/2024"
    c.setFont("Helvetica", 11)
    title_width = c.stringWidth(title, "Helvetica", 11)
    c.drawString((width - title_width) / 2.0, 10.25 * inch, title)

    title = "Availability Analysis"
    c.setFont("Helvetica-Bold", 16)
    title_width = c.stringWidth(title, "Helvetica-Bold", 16)
    c.drawString((width - title_width) / 2.0, 9.9 * inch, title)


    c.setFont("Helvetica", 13)
    cc_with_title_width = c.stringWidth(cc_with_title, "Helvetica", 13)
    c.drawString((width - cc_with_title_width) / 2.0, 9.55 * inch, cc_with_title)

    title = str(df.iloc[0,2])
    c.setFont("Helvetica", 9)
    title_width = c.stringWidth(title, "Helvetica", 9)
    c.drawString((width - title_width) / 2.0, 5 * inch, title)


    c.setLineWidth(1)
    c.line(1 * inch, 9.3 * inch, 7.5 * inch, 9.3 * inch)

    # Example percentages


    # Table data
    table_data = [
        ["", "Females", "Minorities", "Black", "Hispanic", "Asian", "Am. Indian", "Pac / Hawaiian", "Two or More"],
        ["Census Area", f"{female_percent:.1f}%", f"{minority_percent:.1f}%", f"{black_percent:.1f}%",
         f"{hispanic_percent:.1f}%", f"{asian_percent:.1f}%", f"{am_indian_percent:.1f}%",f"{two_or_more_percent:.1f}%", f"{pac_hawaiian_percent:.1f}%"],
        ["Actual", 37.5, 35.9, 14.5, 12.3, 8.0, 0.0, 0.0, 1.1]
    ]

    # Create the table
    col_widths = [1.3 * inch, 0.75 * inch, 0.6 * inch, 0.6 * inch, 0.6 * inch, 0.6 * inch, 0.75 * inch, 1 * inch, 1 * inch]
    table = Table(table_data, colWidths=col_widths)

    # Add style to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor("#003366")),  # Dark blue background for header
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # White text for header
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center horizontally
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),  # Center vertically
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),  # Set font size for the header
        ('ROWHEIGHT', (0, 0), (-1, 0), 25)  # Set height of the top row
    ])

    table.setStyle(style)

    # Find a suitable position to place the table
    table.wrapOn(c, width, height)
    table.drawOn(c, .62 * inch, 8 * inch)

    sizes = [white_percent, black_percent, hispanic_percent, asian_percent, am_indian_percent,
             two_or_more_percent]

    # Define the labels
    labels = ['White', 'Black', 'Hispanic', 'Asian', 'American Indian', 'Two or More']
    colors2 = ['#004c99', '#0066cc', '#0080ff', '#3399ff', '#66b2ff', '#99ccff', '#cce5ff']

    plt.figure(figsize=(10, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=180, colors=colors2)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig('pie_chart.png')  # Save the pie chart as an image
    plt.close()

    # Draw the saved pie chart image into the PDF
    c.drawImage('pie_chart.png',1.3 * inch, .75* inch, width=6 * inch, height=4 * inch)




    img_width = 1666*.9
    img_height = 741*.9
    aspect = img_height / img_width
    display_width = 2 * inch
    display_height = display_width * aspect
    x = (width - display_width) / 2.0
    y = -3 # Adjust y-coordinate to position it at 5 inches height
    c.drawImage("SilbermanLogo.png", x, y, width=display_width, height=display_height)


    # Finalize and save the PDF
    c.showPage()
    c.save()


