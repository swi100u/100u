from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
import os

# Register DejaVu fonts (full Polish character support)
pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', '/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf'))

pdf_path = "/projects/sandbox/Odpowiedz_Wojewoda_USC.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                        leftMargin=60, rightMargin=60,
                        topMargin=50, bottomMargin=50)

# Styles
titleStyle = ParagraphStyle(
    'Title',
    fontName='DejaVuSans-Bold',
    fontSize=13,
    leading=17,
    alignment=TA_CENTER,
    spaceAfter=12,
)
normalStyle = ParagraphStyle(
    'Normal',
    fontName='DejaVuSans',
    fontSize=10,
    leading=14,
    alignment=TA_JUSTIFY,
)
addressStyle = ParagraphStyle(
    'Address',
    fontName='DejaVuSans',
    fontSize=10,
    leading=14,
    alignment=TA_LEFT,
)

story = []

# Tytuł
story.append(Paragraph("Odpowiedź na pismo znak NPII.4100.176.2025<br/>i wniosek o działania nadzorcze", titleStyle))
story.append(Spacer(1, 16))

# Adresat
story.append(Paragraph(
    "Śląski Urząd Wojewódzki w Katowicach<br/>"
    "Wydział Nadzoru Prawnego<br/>"
    "za pośrednictwem Ministerstwa Sprawiedliwości",
    addressStyle
))
story.append(Spacer(1, 16))

# Treść pisma
content = (
    "Zapoznałem się z pismem z dnia 28 sierpnia 2025 r. (znak: NPII.4100.176.2025). "
    "Przyjmuję do wiadomości, że organ nadzoru działa z urzędu, "
    "jednak nie mogę podzielić stanowiska, jakoby nadzór nad obsadą stanowisk kierowniczych "
    "w USC ograniczał się wyłącznie do oceny formalnych kryteriów art. 8 ust. 1 pkt 2 ustawy "
    "– Prawo o aktach stanu cywilnego.<br/><br/>"

    "W polskim systemie prawnym wielokrotnie podkreślono, że nieskazitelna opinia oraz "
    "rękojmia prawidłowego wykonywania obowiązków są warunkami sine qua non dla pełnienia "
    "funkcji zaufania publicznego "
    "(notariusz: art. 11 ustawy Prawo o notariacie, sędzia: art. 61 § 1 PUS, adwokat: "
    "art. 65 Prawo o adwokaturze, radca prawny: art. 24 ust. 1 ustawy o radcach prawnych).<br/><br/>"

    "NSA w wyroku z 29 maja 2025 r., sygn. II GSK 2468/21, jednoznacznie stwierdził, "
    "że zatarcie skazania nie niweczy konieczności badania rękojmi – bo rękojmia to cecha "
    "osobista, związana z charakterem, etyką i wiarygodnością, a nie wyłącznie formalnym "
    "statusem prawnym.<br/><br/>"

    "Osoba pełniąca funkcję zastępcy kierownika USC, która przyznała się do podrobienia "
    "podpisów obywatela na dokumentach urzędowych, nie może być oceniana wyłącznie pod kątem "
    "braku prawomocnego skazania. Brak reakcji ze strony organów nadzoru tworzy sytuację, "
    "w której obywatel nie ma gwarancji, że czynności dokonuje osoba dająca rękojmię "
    "zaufania publicznego.<br/><br/>"

    "<b>Analogiczne przykłady:</b><br/>"
    "• Sprawa Anety Karpiuk – nagłośniona w mediach, pokazująca, że formalny brak skazania "
    "nie eliminuje społecznych i etycznych wątpliwości.<br/>"
    "• Sprawa notariusza (NSA II GSK 2468/21) – mimo zatarcia skazania, rękojmia została "
    "oceniona negatywnie.<br/>"
    "• Przypadki nauczycieli (art. 75 ust. 2a i art. 85o Karty Nauczyciela) – brak zgłoszenia "
    "naruszenia przez dyrektora nie uchyla odpowiedzialności.<br/><br/>"

    "<b>Wnoszę o:</b><br/>"
    "1. Pełną weryfikację rękojmi i nieskazitelnej opinii osób pełniących funkcje kierownicze "
    "w USC.<br/>"
    "2. Wyjaśnienie skutków prawnych czynności dokonanych przez osobę, której nieskazitelność "
    "i rękojmia są podważone.<br/>"
    "3. Przekazanie sprawy do rozstrzygnięcia Naczelnego Sądu Administracyjnego, aby ustalić "
    "zakres obowiązków organów nadzoru w ocenie legalności obsady stanowisk w USC."
)

story.append(Paragraph(content, normalStyle))
story.append(Spacer(1, 24))

# Podpis
story.append(Paragraph("Z poważaniem,<br/>Tomasz Świestowski", addressStyle))

# Zapis dokumentu
doc.build(story)

print(f"PDF wygenerowany: {pdf_path}")
print(f"Rozmiar: {os.path.getsize(pdf_path)} bajtów")
