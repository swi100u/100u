import os
import sys
sys.path.insert(0, '/usr/local/lib/python3.9/site-packages')

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT, TA_LEFT

pdf_path = "/projects/sandbox/100u/Wniosek_ponowne_rozpatrzenie_SKO_FINAL.pdf"

# Rejestracja czcionki Noto Sans
noto_regular = "/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf"
noto_italic = "/usr/share/fonts/google-noto-vf/NotoSans-Italic[wght].ttf"

pdfmetrics.registerFont(TTFont('NotoSans', noto_regular))
pdfmetrics.registerFont(TTFont('NotoSans-Italic', noto_italic))

FONT_REGULAR = 'NotoSans'
FONT_ITALIC = 'NotoSans-Italic'

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=A4,
    leftMargin=54,
    rightMargin=54,
    topMargin=50,
    bottomMargin=50
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('CustomTitle', parent=styles['Title'], fontName=FONT_REGULAR, fontSize=13, leading=17, alignment=TA_CENTER, spaceAfter=6)
heading_style = ParagraphStyle('CustomHeading', parent=styles['Normal'], fontName=FONT_REGULAR, fontSize=11, leading=15, alignment=TA_LEFT, spaceBefore=14, spaceAfter=6)
normal_style = ParagraphStyle('CustomNormal', parent=styles['Normal'], fontName=FONT_REGULAR, fontSize=10.5, leading=14.5, alignment=TA_JUSTIFY, spaceAfter=4)
left_style = ParagraphStyle('CustomLeft', parent=styles['Normal'], fontName=FONT_REGULAR, fontSize=10.5, leading=14.5, alignment=TA_LEFT, spaceAfter=4)

story = []

# NAGLOWEK
story.append(Paragraph("Samorz\u0105dowe Kolegium Odwo\u0142awcze w Katowicach", left_style))
story.append(Paragraph("ul. D\u0105browskiego 23", left_style))
story.append(Paragraph("40-032 Katowice", left_style))
story.append(Spacer(1, 12))
story.append(Paragraph("Sygn. akt: SKO.K/41.3/983/2026/7988/LZ", left_style))
story.append(Spacer(1, 12))
story.append(Paragraph("Wnioskodawca: Tomasz \u015awiestowski", left_style))
story.append(Spacer(1, 20))

story.append(Paragraph("<b>WNIOSEK O PONOWNE ROZPATRZENIE SPRAWY</b>", title_style))
story.append(Spacer(1, 16))

# Podstawa prawna
story.append(Paragraph(
    "Dzia\u0142aj\u0105c na podstawie art. 127 \u00a7 3 k.p.a. w zw. z art. 144 k.p.a., wnosz\u0119 o ponowne rozpatrzenie sprawy "
    "zako\u0144czonej postanowieniem Samorz\u0105dowego Kolegium Odwo\u0142awczego w Katowicach z dnia 5 czerwca 2026 r., "
    "sygn. SKO.K/41.3/983/2026/7988/LZ, odmawiaj\u0105cym wszcz\u0119cia post\u0119powania w sprawie stwierdzenia niewa\u017cno\u015bci "
    "decyzji Prezydenta Miasta Ruda \u015al\u0105ska z dnia 21 grudnia 2023 r., nr SK.5430.7.16.2023.BW.", normal_style))
story.append(Spacer(1, 10))

story.append(Paragraph("<b>Wnosz\u0119 o:</b>", normal_style))
story.append(Spacer(1, 4))
story.append(Paragraph("1. Uchylenie zaskar\u017conego postanowienia w ca\u0142o\u015bci.", normal_style))
story.append(Paragraph("2. Wszcz\u0119cie post\u0119powania w sprawie stwierdzenia niewa\u017cno\u015bci decyzji z dnia 21 grudnia 2023 r.", normal_style))
story.append(Paragraph("3. Przeprowadzenie post\u0119powania wyja\u015bniaj\u0105cego w zakresie okoliczno\u015bci podniesionych w niniejszym wniosku.", normal_style))
story.append(Paragraph(
    "4. Zwr\u00f3cenie si\u0119 do Prokuratury Rejonowej w Rudzie \u015al\u0105skiej o przekazanie opinii s\u0105dowo-psychiatrycznej, "
    "na kt\u00f3r\u0105 powo\u0142ywa\u0142 si\u0119 organ przy wydaniu decyzji z dnia 21 grudnia 2023 r., celem ustalenia, "
    "czy dokument ten w og\u00f3le istnieje w formie mog\u0105cej stanowi\u0107 podstaw\u0119 rozstrzygni\u0119cia administracyjnego.", normal_style))
story.append(Spacer(1, 14))

story.append(Paragraph("<b>UZASADNIENIE</b>", title_style))
story.append(Spacer(1, 10))

# I
story.append(Paragraph("<b>I. Brak to\u017csamo\u015bci sprawy \u2014 nowa okoliczno\u015b\u0107 faktyczna</b>", heading_style))
story.append(Paragraph(
    "Kolegium odm\u00f3wi\u0142o wszcz\u0119cia post\u0119powania, powo\u0142uj\u0105c si\u0119 na to\u017csamo\u015b\u0107 sprawy z poprzednim post\u0119powaniem "
    "niewa\u017cno\u015bciowym zako\u0144czonym decyzj\u0105 SKO z dnia 18 kwietnia 2025 r. Stanowisko to jest b\u0142\u0119dne.", normal_style))
story.append(Paragraph(
    "Obecny wniosek opiera si\u0119 na okoliczno\u015bci, kt\u00f3ra ujawni\u0142a si\u0119 dopiero po zako\u0144czeniu poprzedniego post\u0119powania "
    "\u2014 w toku post\u0119powania prowadzonego przez Prezydenta Miasta Ruda \u015al\u0105ska pod sygn. SK.5430.4.86.2026.BW.", normal_style))
story.append(Paragraph(
    "W tym post\u0119powaniu organ I instancji podj\u0105\u0142 czynno\u015bci zmierzaj\u0105ce do pozyskania opinii s\u0105dowo-psychiatrycznej, "
    "na kt\u00f3r\u0105 powo\u0142ywa\u0142a si\u0119 Prokuratura Rejonowa w Rudzie \u015al\u0105skiej. Prokuratura odm\u00f3wi\u0142a udost\u0119pnienia tej opinii. "
    "Organ sam potwierdzi\u0142 w decyzji z dnia 4 marca 2026 r., \u017ce nie dysponuje tym dokumentem.", normal_style))
story.append(Paragraph("Jest to okoliczno\u015b\u0107 nowa i samodzielna. Dopiero obecnie sta\u0142o si\u0119 niebudz\u0105ce w\u0105tpliwo\u015bci, \u017ce:", normal_style))
story.append(Paragraph("\u2014 organ nie posiada\u0142 opinii s\u0105dowo-psychiatrycznej ani w 2023 r., ani w \u017cadnym p\u00f3\u017aniejszym momencie,", normal_style))
story.append(Paragraph("\u2014 nie jest mo\u017cliwe jej pozyskanie nawet obecnie,", normal_style))
story.append(Paragraph(
    "\u2014 decyzja z dnia 21 grudnia 2023 r. zosta\u0142a wydana bez jakiegokolwiek dowodu potwierdzaj\u0105cego "
    "istnienie przes\u0142anek z art. 99 ustawy o kieruj\u0105cych pojazdami.", normal_style))

# II
story.append(Paragraph("<b>II. Organ zastosowa\u0142 niew\u0142a\u015bciwy re\u017cim prawny \u2014 pomylenie art. 99 z art. 102 u.k.p.</b>", heading_style))
story.append(Paragraph(
    "Z tre\u015bci uzasadnienia decyzji z dnia 21 grudnia 2023 r. wynika, \u017ce organ potraktowa\u0142 wniosek Prokuratury "
    "jako wi\u0105\u017c\u0105cy i stwierdzi\u0142, \u017ce \u201enie mo\u017ce odst\u0105pi\u0107 od prowadzonego post\u0119powania\u201d.", normal_style))
story.append(Paragraph(
    "Jest to podej\u015bcie w\u0142a\u015bciwe dla art. 102 ustawy o kieruj\u0105cych pojazdami, w kt\u00f3rym organ jest w znacznym "
    "stopniu zwi\u0105zany ustaleniami Policji lub s\u0105du. Tymczasem art. 99 ust. 1 pkt 2, na kt\u00f3ry organ si\u0119 powo\u0142a\u0142, "
    "wymaga od organu samodzielnego ustalenia istnienia \u201euzasadnionych i powa\u017cnych zastrze\u017ce\u0144 co do stanu zdrowia\u201d kierowcy. "
    "Organ nie jest w tym trybie zwi\u0105zany stanowiskiem \u017cadnego podmiotu zewn\u0119trznego.", normal_style))
story.append(Paragraph(
    "W decyzji organ nie analizuje, czy zastrze\u017cenia s\u0105 \u201euzasadnione\u201d ani czy s\u0105 \u201epowa\u017cne\u201d. Stwierdza jedynie: "
    "\u201euzna\u0107 nale\u017cy, \u017ce zachodz\u0105 uzasadnione i powa\u017cne zastrze\u017cenia\u201d \u2014 bez jakiejkolwiek argumentacji. "
    "Jest to konkluzja bez rozumowania, typowa dla decyzji zwi\u0105zanej.", normal_style))
story.append(Paragraph(
    "Organ formalnie powo\u0142ywa\u0142 si\u0119 na art. 99, lecz faktycznie zachowa\u0142 si\u0119 tak, jakby dzia\u0142a\u0142 w trybie art. 102 "
    "\u2014 bez pe\u0142nego post\u0119powania dowodowego, bez samodzielnej oceny przes\u0142anek i z przekonaniem, "
    "\u017ce jest zwi\u0105zany stanowiskiem Prokuratury.", normal_style))

# III
story.append(Paragraph("<b>III. Zastosowanie art. 182 k.p.a. \u2014 b\u0142\u0119dna kwalifikacja \u017c\u0105dania Prokuratury</b>", heading_style))
story.append(Paragraph(
    "Z zawiadomienia o wszcz\u0119ciu post\u0119powania z dnia 10 listopada 2023 r. (pismo nr SK.5430.4.593.2023.BW) wynika, "
    "\u017ce organ wszcz\u0105\u0142 post\u0119powanie na podstawie \u201ewniosku Prokuratora Rejonowego w Rudzie \u015al\u0105skiej sygn. akt "
    "4096-0.Pa.36.2022 o wszcz\u0119cie post\u0119powania administracyjnego na podstawie art. 182 k.p.a.\u201d", normal_style))
story.append(Paragraph(
    "Art. 182 k.p.a. przyznaje prokuratorowi prawo \u017c\u0105dania wszcz\u0119cia post\u0119powania administracyjnego. "
    "\u017b\u0105danie takie obliguje organ do wszcz\u0119cia post\u0119powania, jednak nie przes\u0105dza o tre\u015bci rozstrzygni\u0119cia. "
    "Organ jest zobowi\u0105zany wszcz\u0105\u0107 post\u0119powanie, ale musi samodzielnie przeprowadzi\u0107 post\u0119powanie dowodowe "
    "i samodzielnie oceni\u0107, czy zachodz\u0105 przes\u0142anki materialnoprawne do wydania decyzji.", normal_style))
story.append(Paragraph(
    "Tymczasem organ potraktowa\u0142 \u017c\u0105danie Prokuratury nie tylko jako podstaw\u0119 wszcz\u0119cia post\u0119powania "
    "(co by\u0142o prawid\u0142owe), lecz r\u00f3wnie\u017c jako materialnoprawna podstaw\u0119 rozstrzygni\u0119cia (co by\u0142o niedopuszczalne). "
    "Organ przyj\u0105\u0142 twierdzenia Prokuratury za w\u0142asne ustalenia faktyczne bez jakiejkolwiek weryfikacji.", normal_style))
story.append(Paragraph(
    "Organ b\u0142\u0119dnie uto\u017csami\u0142 obowi\u0105zek wszcz\u0119cia post\u0119powania na \u017c\u0105danie prokuratora z obowi\u0105zkiem "
    "wydania decyzji zgodnej z tym \u017c\u0105daniem. S\u0105 to dwie odr\u0119bne kwestie prawne.", normal_style))

# IV
story.append(Paragraph("<b>IV. Opinia z postepowania karnego o innym przedmiocie (art. 190a k.k.)</b>", heading_style))
story.append(Paragraph(
    "Z zawiadomienia o wszcz\u0119ciu post\u0119powania wynika, \u017ce opinia s\u0105dowo-psychiatryczna zosta\u0142a sporz\u0105dzona "
    "w toku post\u0119powania karnego prowadzonego przez Prokuratur\u0119 Rejonow\u0105 w Rudzie \u015al\u0105skiej "
    "\u201eo czyn z art. 190a kk\u201d (uporczywe n\u0119kanie/stalking).", normal_style))
story.append(Paragraph(
    "Opinia ta mia\u0142a na celu ocen\u0119 poczytalnosci podejrzanego w kontek\u015bcie zarzucanego mu czynu. "
    "Nie by\u0142a sporz\u0105dzona w celu oceny zdolno\u015bci do kierowania pojazdami. Nie odnosi\u0142a si\u0119 do kwestii "
    "przeciwwskaza\u0144 zdrowotnych do prowadzenia pojazd\u00f3w mechanicznych.", normal_style))
story.append(Paragraph(
    "Nawet gdyby organ pozyska\u0142 t\u0119 opini\u0119, nie mog\u0142aby ona stanowi\u0107 samodzielnej podstawy do ustalenia "
    "\u201euzasadnionych i powa\u017cnych zastrze\u017ce\u0144 co do stanu zdrowia\u201d w rozumieniu art. 99 ust. 1 pkt 2 "
    "ustawy o kieruj\u0105cych pojazdami, poniewa\u017c:", normal_style))
story.append(Paragraph("\u2014 zosta\u0142a sporz\u0105dzona na potrzeby oceny poczytalno\u015bci w sprawie karnej, a nie zdolno\u015bci do kierowania pojazdami,", normal_style))
story.append(Paragraph("\u2014 dotyczy\u0142a zupe\u0142nie innego przedmiotu (odpowiedzialno\u015b\u0107 karna za n\u0119kanie),", normal_style))
story.append(Paragraph("\u2014 bieg\u0142y psychiatra nie bada\u0142 osoby pod k\u0105tem zdolno\u015bci psychofizycznych wymaganych od kierowcy.", normal_style))
story.append(Paragraph(
    "Bezkrytyczne przeniesienie twierdze\u0144 Prokuratury z post\u0119powania karnego o czyn z art. 190a k.k. "
    "do post\u0119powania administracyjnego o uprawnienia kierowcy stanowi ra\u017c\u0105ce naruszenie zasady prawdy "
    "obiektywnej (art. 7 k.p.a.) oraz zasady swobodnej oceny dowod\u00f3w (art. 80 k.p.a.).", normal_style))

# V
story.append(Paragraph("<b>V. Organ nie przeprowadzi\u0142 post\u0119powania dowodowego</b>", heading_style))
story.append(Paragraph(
    "Organ powo\u0142ywa\u0142 si\u0119 na tre\u015b\u0107 opinii s\u0105dowo-psychiatrycznej, stwierdzaj\u0105c \u017ce \u201ejak wynika z opinii "
    "s\u0105dowo-psychiatrycznej Pan Tomasz \u015awiestowski jest uzale\u017cniony od narkotyk\u00f3w i dopalaczy\u201d. Jednocze\u015bnie:", normal_style))
story.append(Paragraph("\u2014 opinia ta nigdy nie zosta\u0142a w\u0142\u0105czona do akt administracyjnych sprawy,", normal_style))
story.append(Paragraph("\u2014 organ nie podj\u0105\u0142 czynno\u015bci zmierzaj\u0105cych do jej pozyskania przed wydaniem decyzji,", normal_style))
story.append(Paragraph("\u2014 organ nie dokona\u0142 samodzielnej oceny tego dokumentu,", normal_style))
story.append(Paragraph("\u2014 strona nie mia\u0142a mo\u017cliwo\u015bci zapoznania si\u0119 z tym dowodem (naruszenie art. 10 \u00a7 1 k.p.a.).", normal_style))

# VI
story.append(Paragraph("<b>VI. Organ nie by\u0142 zwi\u0105zany stanowiskiem Prokuratury</b>", heading_style))
story.append(Paragraph(
    "Art. 99 ust. 1 pkt 2 ustawy o kieruj\u0105cych pojazdami wymaga samodzielnego ustalenia przez organ "
    "istnienia \u201euzasadnionych i powa\u017cnych zastrze\u017ce\u0144 co do stanu zdrowia\u201d kierowcy. Przepis ten nie przewiduje "
    "zwi\u0105zania organu stanowiskiem Policji, Prokuratury ani \u017cadnego innego podmiotu zewn\u0119trznego.", normal_style))

# VII
story.append(Paragraph("<b>VII. Obalenie domniemania prawid\u0142owo\u015bci (art. 76 \u00a7 3 k.p.a.)</b>", heading_style))
story.append(Paragraph(
    "Zgodnie z art. 76 \u00a7 3 k.p.a. domniemanie prawdziwo\u015bci dokumentu urz\u0119dowego mo\u017ce zosta\u0107 obalone "
    "dowodem przeciwnym. Dowodem przeciwnym jest fakt, \u017ce organ nie posiada opinii, Prokuratura odm\u00f3wi\u0142a "
    "jej udost\u0119pnienia, a brak jest mo\u017cliwo\u015bci weryfikacji twierdze\u0144 zawartych w pi\u015bmie inicjuj\u0105cym post\u0119powanie.", normal_style))

# VIII
story.append(Paragraph("<b>VIII. Potwierdzenie braku dowodu w p\u00f3\u017aniejszym post\u0119powaniu</b>", heading_style))
story.append(Paragraph(
    "W decyzji z dnia 4 marca 2026 r. organ I instancji sam przyzna\u0142, i\u017c wyst\u0119powa\u0142 do Prokuratury "
    "o udost\u0119pnienie opinii psychiatrycznej i jej nie otrzyma\u0142. Jest to przyznanie, \u017ce organ wiedzia\u0142 "
    "o konieczno\u015bci weryfikacji tego dowodu, podj\u0105\u0142 pr\u00f3b\u0119 jego pozyskania, nie by\u0142 w stanie go uzyska\u0107, "
    "a mimo to utrzymywa\u0142 w mocy skutki prawne decyzji z 2023 r.", normal_style))

# IX
story.append(Paragraph("<b>IX. Ra\u017c\u0105ce naruszenie prawa (art. 156 \u00a7 1 pkt 2 k.p.a.)</b>", heading_style))
story.append(Paragraph("Nie jest to wadliwa ocena dowod\u00f3w, lecz:", normal_style))
story.append(Paragraph("\u2014 ca\u0142kowity brak dowodu, na podstawie kt\u00f3rego organ podj\u0105\u0142 rozstrzygni\u0119cie,", normal_style))
story.append(Paragraph("\u2014 zastosowanie niew\u0142a\u015bciwego re\u017cimu prawnego (art. 102 zamiast art. 99),", normal_style))
story.append(Paragraph("\u2014 b\u0142\u0119dne uto\u017csamienie art. 182 k.p.a. z podstaw\u0105 materialn\u0105 rozstrzygni\u0119cia,", normal_style))
story.append(Paragraph("\u2014 bezkrytyczne przeniesienie ustale\u0144 z post\u0119powania karnego o art. 190a k.k.,", normal_style))
story.append(Paragraph("\u2014 pozbawienie strony prawa do udzia\u0142u w post\u0119powaniu dowodowym (art. 10 \u00a7 1 k.p.a.),", normal_style))
story.append(Paragraph("\u2014 ingerencja w prawo do swobodnego przemieszczania si\u0119 bez materialnej podstawy.", normal_style))

# X
story.append(Paragraph("<b>X. Podsumowanie</b>", heading_style))
story.append(Paragraph("Nie zachodzi to\u017csamo\u015b\u0107 sprawy uzasadniaj\u0105ca art. 61a \u00a7 1 k.p.a., poniewa\u017c:", normal_style))
story.append(Paragraph("1. Now\u0105 okoliczno\u015bci\u0105 jest ujawniony brak opinii s\u0105dowo-psychiatrycznej.", normal_style))
story.append(Paragraph("2. Okoliczno\u015b\u0107 ta ujawni\u0142a si\u0119 dopiero w post\u0119powaniu pod sygn. SK.5430.4.86.2026.BW.", normal_style))
story.append(Paragraph("3. Obecnie dysponuj\u0119 potwierdzeniem organu, \u017ce dow\u00f3d nie istnieje i nie mo\u017ce zosta\u0107 pozyskany.", normal_style))
story.append(Paragraph("4. Organ zastosowa\u0142 niew\u0142a\u015bciwy re\u017cim prawny (art. 102 zamiast art. 99).", normal_style))
story.append(Paragraph("5. Organ b\u0142\u0119dnie uto\u017csami\u0142 art. 182 k.p.a. z podstaw\u0105 materialn\u0105 decyzji.", normal_style))
story.append(Paragraph(
    "6. Opinia z post\u0119powania karnego o art. 190a k.k. nie mog\u0142a stanowi\u0107 podstawy zastosowania art. 99 u.k.p.", normal_style))
story.append(Spacer(1, 6))
story.append(Paragraph("Wobec powy\u017cszego wnosz\u0119 jak na wst\u0119pie.", normal_style))

story.append(Spacer(1, 30))
story.append(Paragraph("Tomasz \u015awiestowski", normal_style))
story.append(Paragraph("[podpis]", normal_style))

doc.build(story)
print(f"PDF wygenerowany: {pdf_path}")
print(f"Rozmiar: {os.path.getsize(pdf_path)} bajtow")
