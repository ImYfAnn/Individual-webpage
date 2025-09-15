from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def create_resume_pdf():
    """Create a professional PDF resume"""
    
    # Create PDF document with better margins
    doc = SimpleDocTemplate("Madiha-Chaudhary-Resume.pdf", pagesize=A4,
                          rightMargin=1.5*cm, leftMargin=1.5*cm,
                          topMargin=2*cm, bottomMargin=1.5*cm)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        spaceAfter=15,
        spaceBefore=0,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1a365d'),
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=20,
        spaceBefore=5,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#4a5568'),
        fontName='Helvetica'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=13,
        spaceAfter=8,
        spaceBefore=16,
        textColor=colors.HexColor('#2d3748'),
        fontName='Helvetica-Bold',
        borderWidth=0,
        borderColor=colors.HexColor('#e2e8f0'),
        borderPadding=5,
        backColor=colors.HexColor('#f7fafc')
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=9.5,
        spaceAfter=4,
        spaceBefore=2,
        alignment=TA_JUSTIFY,
        fontName='Helvetica',
        leading=12
    )
    
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=10.5,
        spaceAfter=2,
        spaceBefore=8,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#2d3748')
    )
    
    company_style = ParagraphStyle(
        'Company',
        parent=styles['Normal'],
        fontSize=9.5,
        spaceAfter=1,
        spaceBefore=1,
        fontName='Helvetica-Oblique',
        textColor=colors.HexColor('#4a5568')
    )
    
    duration_style = ParagraphStyle(
        'Duration',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=4,
        spaceBefore=1,
        fontName='Helvetica',
        textColor=colors.HexColor('#718096'),
        alignment=TA_RIGHT
    )
    
    # Build content
    story = []
    
    # Title
    story.append(Paragraph("MADIHA CHAUDHARY", title_style))
    
    # Contact info with better formatting
    contact_lines = [
        "📞 +91 9157496970  |  📧 madihakhalid786@hotmail.com",
        "📍 Valsad, Gujarat, India  |  Nationality: Indian",
        "🌐 LinkedIn: www.linkedin.com/in/madiha-chaudhary-81146a231"
    ]
    
    for line in contact_lines:
        story.append(Paragraph(line, subtitle_style))
    
    story.append(Spacer(1, 15))
    
    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
    summary_text = """
    Seasoned Customer Support Specialist with over 10 years of experience across B2B and B2C domains. 
    Proven expertise in phone, chat, and email support, conflict resolution, and customer satisfaction. 
    Adept at using CRM tools and driving process improvements. Seeking a Senior Customer Care Support 
    role to leverage my background in global support operations, content writing, and team collaboration.
    """
    story.append(Paragraph(summary_text, normal_style))
    story.append(Spacer(1, 8))
    
    # Key Skills
    story.append(Paragraph("KEY SKILLS", heading_style))
    skills_data = [
        ['Customer Support (Voice, Chat, Email)', 'CRM Tools: Zendesk, Salesforce, Freshdesk'],
        ['Conflict Resolution & Escalation Handling', 'SLA & KPI Management'],
        ['Inside Sales & Business Development', 'Content Writing & Research'],
        ['WebRTC | Live Streaming (Basic)', 'AI Tools (learning actively)'],
        ['Languages: English, Hindi', '']
    ]
    
    skills_table = Table(skills_data, colWidths=[3.2*inch, 3.2*inch])
    skills_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2d3748')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 8))
    
    # Professional Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))
    
    # Revolut
    story.append(Paragraph("Customer Support Specialist (Phone & Chat)", job_title_style))
    
    # Create a table for company and duration
    company_duration_table = Table([
        ["Revolut", "Dec 2023 to May 2025"]
    ], colWidths=[4.5*inch, 2*inch])
    company_duration_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Oblique'),
        ('FONTSIZE', (0, 0), (0, 0), 9.5),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#4a5568')),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (0, 1), 9),
        ('TEXTCOLOR', (0, 1), (0, 1), colors.HexColor('#718096')),
        ('ALIGN', (0, 1), (0, 1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2)
    ]))
    story.append(company_duration_table)
    
    revolut_duties = """
    • Delivered tier-1 and tier-2 phone support for global banking customers<br/>
    • Resolved account and transaction issues, contributing to >90% customer satisfaction score<br/>
    • Handled chat tickets during internal rotation<br/>
    • Adapted quickly to graveyard shifts and rapid changes in workflow<br/>
    • Tools used: Internal CRM, ticketing systems
    """
    story.append(Paragraph(revolut_duties, normal_style))
    story.append(Spacer(1, 6))
    
    # PrintYo
    story.append(Paragraph("Inside Sales & Customer Service Executive", job_title_style))
    
    company_duration_table2 = Table([
        ["PrintYo Australia (Logicsofts Webtech Pvt Ltd)", "Aug 2022 to Jul 2023"]
    ], colWidths=[4.5*inch, 2*inch])
    company_duration_table2.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Oblique'),
        ('FONTSIZE', (0, 0), (0, 0), 9.5),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#4a5568')),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (0, 1), 9),
        ('TEXTCOLOR', (0, 1), (0, 1), colors.HexColor('#718096')),
        ('ALIGN', (0, 1), (0, 1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2)
    ]))
    story.append(company_duration_table2)
    
    printyo_duties = """
    • Managed full-cycle customer support via email, chat, and phone<br/>
    • Collaborated with business teams for custom printing solutions<br/>
    • Handled B2B and B2C orders, complaints, and escalations<br/>
    • Improved customer response time by 30%
    """
    story.append(Paragraph(printyo_duties, normal_style))
    story.append(Spacer(1, 6))
    
    # Content Writer
    story.append(Paragraph("Content Writer (Full-time)", job_title_style))
    
    company_duration_table3 = Table([
        ["Tsocio Digisol / CD Tech", "May 2021 to Feb 2022"]
    ], colWidths=[4.5*inch, 2*inch])
    company_duration_table3.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Oblique'),
        ('FONTSIZE', (0, 0), (0, 0), 9.5),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#4a5568')),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (0, 1), 9),
        ('TEXTCOLOR', (0, 1), (0, 1), colors.HexColor('#718096')),
        ('ALIGN', (0, 1), (0, 1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2)
    ]))
    story.append(company_duration_table3)
    
    content_duties = """
    • Wrote SEO-optimized content for digital businesses and live streaming platforms<br/>
    • Contributed to blogs, product descriptions, and client documentation
    """
    story.append(Paragraph(content_duties, normal_style))
    story.append(Spacer(1, 6))
    
    # E-commerce Business Owner
    story.append(Paragraph("E-commerce Business Owner", job_title_style))
    
    company_duration_table4 = Table([
        ["Self-Employed", "Jan 2013 to Oct 2020"]
    ], colWidths=[4.5*inch, 2*inch])
    company_duration_table4.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Oblique'),
        ('FONTSIZE', (0, 0), (0, 0), 9.5),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#4a5568')),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (0, 1), 9),
        ('TEXTCOLOR', (0, 1), (0, 1), colors.HexColor('#718096')),
        ('ALIGN', (0, 1), (0, 1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2)
    ]))
    story.append(company_duration_table4)
    
    ecommerce_duties = """
    • Launched and managed travel products store on Amazon and eBay India<br/>
    • Handled customer service, logistics, marketing, and inventory independently
    """
    story.append(Paragraph(ecommerce_duties, normal_style))
    story.append(Spacer(1, 6))
    
    # Other positions
    story.append(Paragraph("Sr. Business Executive", job_title_style))
    other_company_table1 = Table([
        ["Serco", "Oct 2012 to Apr 2013"]
    ], colWidths=[4.5*inch, 2*inch])
    other_company_table1.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Oblique'),
        ('FONTSIZE', (0, 0), (0, 0), 9.5),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#4a5568')),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (0, 1), 9),
        ('TEXTCOLOR', (0, 1), (0, 1), colors.HexColor('#718096')),
        ('ALIGN', (0, 1), (0, 1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2)
    ]))
    story.append(other_company_table1)
    story.append(Paragraph("• Managed customer accounts and upselling for telecom clients", normal_style))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Customer Relations Advisor", job_title_style))
    other_company_table2 = Table([
        ["3 Global Services", "Jun 2009 to Jan 2011"]
    ], colWidths=[4.5*inch, 2*inch])
    other_company_table2.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Oblique'),
        ('FONTSIZE', (0, 0), (0, 0), 9.5),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#4a5568')),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (0, 1), 9),
        ('TEXTCOLOR', (0, 1), (0, 1), colors.HexColor('#718096')),
        ('ALIGN', (0, 1), (0, 1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2)
    ]))
    story.append(other_company_table2)
    other_duties1 = """
    • Provided support for Vodafone & 3 Prepay Australia customers<br/>
    • Delivered solutions in high-volume call environments
    """
    story.append(Paragraph(other_duties1, normal_style))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("Communication Coach / Inside Sales Rep", job_title_style))
    other_company_table3 = Table([
        ["Stream Global Services / Infowavz", "Mar 2004 to Mar 2009"]
    ], colWidths=[4.5*inch, 2*inch])
    other_company_table3.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Oblique'),
        ('FONTSIZE', (0, 0), (0, 0), 9.5),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#4a5568')),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (0, 1), 9),
        ('TEXTCOLOR', (0, 1), (0, 1), colors.HexColor('#718096')),
        ('ALIGN', (0, 1), (0, 1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2)
    ]))
    story.append(other_company_table3)
    other_duties2 = """
    • Supported clients like Invacare, Dish Network, and Primus Canada<br/>
    • Promoted to Communication Coach for HPNA-6J Technical Process
    """
    story.append(Paragraph(other_duties2, normal_style))
    story.append(Spacer(1, 8))
    
    # Education
    story.append(Paragraph("EDUCATION", heading_style))
    education_table = Table([
        ["BA in English (Hons)", "2003 to 2006"],
        ["Modern Institute of Engineering & Management", ""]
    ], colWidths=[4.5*inch, 2*inch])
    education_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 10.5),
        ('TEXTCOLOR', (0, 0), (0, 0), colors.HexColor('#2d3748')),
        ('FONTNAME', (0, 1), (0, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (0, 1), 9),
        ('TEXTCOLOR', (0, 1), (0, 1), colors.HexColor('#718096')),
        ('ALIGN', (0, 1), (0, 1), 'RIGHT'),
        ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Oblique'),
        ('FONTSIZE', (1, 0), (1, 0), 9.5),
        ('TEXTCOLOR', (1, 0), (1, 0), colors.HexColor('#4a5568')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2)
    ]))
    story.append(education_table)
    story.append(Spacer(1, 8))
    
    # References
    story.append(Paragraph("REFERENCES", heading_style))
    references_data = [
        ['Vijay, PrintYo', 'vijay@logicsofts.com', '+91 88267 11327'],
        ['Riddhi, PrintYo', 'riddhi@printyo.net.au', '+91 82005 67666'],
        ['Kartikey, Revolut', '', '+91 70076 12632'],
        ['Dilon, Revolut', '', '+91 88927 40090']
    ]
    
    references_table = Table(references_data, colWidths=[2*inch, 2.5*inch, 2*inch])
    references_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f8fafc')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2d3748')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold')
    ]))
    story.append(references_table)
    
    # Build PDF
    doc.build(story)
    print("PDF created successfully: Madiha-Chaudhary-Resume.pdf")

if __name__ == "__main__":
    create_resume_pdf()
