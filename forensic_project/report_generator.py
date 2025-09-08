from fpdf import FPDF

def create_pdf_report(ips, creds, commands):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Forensic Analysis Report", ln=True, align="C")
    
    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.cell(0, 10, "Top Attacker IPs:", ln=True)
    for ip in ips[:10]:
        pdf.cell(0, 8, str(ip), ln=True)
    
    pdf.ln(5)
    pdf.cell(0, 10, "Top Failed Credentials:", ln=True)
    for cred in creds[:10]:
        pdf.cell(0, 8, f"{cred[0]}:{cred[1]}", ln=True)
    
    pdf.ln(5)
    pdf.cell(0, 10, "Top Commands:", ln=True)
    for cmd in commands[:10]:
        pdf.cell(0, 8, cmd, ln=True)
    
    # Add graphs
    for img in ["top_ips.png", "top_credentials.png", "top_commands.png", "attack_by_hour.png"]:
        pdf.add_page()
        pdf.image(img, x=15, y=30, w=180)  # Adjust size as needed
    
    pdf.output("forensic_report.pdf")
