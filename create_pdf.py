from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("sample.pdf", pagesize=letter)

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(50, 750, "Tamil Nadu Electricity Policy 2024")

# Content
c.setFont("Helvetica", 12)
y = 700
content = """
1. RENEWABLE ENERGY TARGETS
Tamil Nadu aims to generate 50% renewable energy by 2025.
Solar projects receive 40% subsidy from government.
Wind energy capacity will increase by 2000 MW.

2. FARMER BENEFITS
Farmers get free electricity for 8 hours daily.
Solar pump subsidies available for all registered farmers.
Training programs for sustainable agriculture provided.

3. INDUSTRIAL SUPPORT
Industries get 20% discount on bulk electricity purchase.
Energy efficient units get additional 5% rebate.
Setup costs for solar installation supported.

4. CONTACT INFORMATION
Website: https://tangedco.gov.in
Email: info@tangedco.gov.in
Phone: +91-44-2536-1234
"""

for line in content.split('\n'):
    if line.strip():
        c.drawString(50, y, line)
        y -= 20

c.save()
print("✅ PDF created: sample.pdf")