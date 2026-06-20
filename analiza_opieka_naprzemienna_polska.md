# Analiza danych polskich w kontekście badań nad opieką naprzemienną i przemocą partnerską

---

## Executive summary

- Cel: Zrekonstruować i ocenić polskie dane (GUS, Ministerstwo Sprawiedliwości) dotyczące orzeczeń o wykonywaniu władzy rodzicielskiej (2018–2024) oraz ocenić, czy można na ich podstawie testować hipotezę znaną z Fernández‑Kranz et al. (2021) o wpływie shared custody na przemoc partnerską.
- Główne obserwacje: W zrekonstruowanych danych rośnie udział orzeczeń o wspólnej władzy rodzicielskiej (z 57,8% w 2018 r. do ~67,6% w 2024 r.). Uwaga: termin "wspólna władza" w polskim prawie nie równa się automatycznie fizycznej pieczy naprzemiennej.
- Główne ograniczenia: brak jednorodnej reformy ustawowej (brak naturalnego eksperymentu), niepewność co do operacjonalizacji "opieki naprzemiennej" w dostępnych statystykach oraz brak jawnych, powiązanych danych policyjnych/zdrowotnych na poziomie lokalnym.
- Rekomendacja badawcza (krótko): uzyskać dane panelowe na poziomie okręgów sądowych i powiatów, powiązać orzeczenia z danymi policji/Niebieskiej Karty/zdrowia i zaprojektować quasi‑eksperyment (różnice w praktyce sądowej, zmiany składu sędziowskiego, pilotaż regionu).

---

## 1. Co pokazuje tabela — skrót wyników opisowych

Dane z GUS i Ministerstwa Sprawiedliwości dotyczą orzeczeń sądowych o wykonywaniu władzy rodzicielskiej po rozwodzie w Polsce w latach 2018–2024. Poniżej znajduje się zrekonstruowana tabela (źródła: GUS, MS — patrz sekcja Źródła). 

Uwaga krytyczna: W pliku oryginalnym występuje niezgodność numeryczna między opisem trendu a wartościami w tabeli (wartość 2023 dla "Razem matce i ojcu" wydaje się być wyższa niż w 2024 r., mimo że tekst podaje monotoniczny wzrost 2018→2024). Proszę zweryfikować oryginalne pliki GUS/MS i poprawić, jeśli to konieczne — zobacz sekcję Data & Methods.

### Kluczowe trendy (skrót)
- Wspólna władza: 57,8% (2018) → ~67,6% (2024) (trend wzrostowy w zrekonstruowanych danych).
- Wyłączna przy matce: spadek w liczbach bezwzględnych i udziałach.
- Wyłączna przy ojcu: stabilnie niskie wartości.

### Zrekonstruowane dane (2018–2024)
| Rok | Matce | Ojcu | Razem matce i ojcu | Oddzielnie matce i ojcu | Rodzinie zastępczej | Placówce wychowawczej | Inne | Razem |
|-----:|------:|-----:|-------------------:|------------------------:|--------------------:|-----------------------:|-----:|------:|
| 2018 | 13 360 | 1 270 | 21 020 | 290 | 230 | 90 | 70 | 36 330 |
| 2019 | 12 150 | 1 150 | 22 820 | 270 | 220 | 80 | 70 | 36 760 |
| 2020 | 10 780 | 1 110 | 23 140 | 250 | 210 | 70 | 60 | 35 620 |
| 2021 | 9 920  | 1 020 | 24 860 | 240 | 200 | 70 | 60 | 36 370 |
| 2022 | 8 940  | 960   | 25 680 | 230 | 190 | 60 | 60 | 36 120 |
| 2023 | 8 020  | 920   | 27 120 | 220 | 180 | 60 | 50 | 36 570 |
| 2024 | 9 950  | 1 090 | 24 260 | 240 | 200 | 70 | 60 | 35 870 |

Data validation note: The 2023 value for "Razem matce i ojcu" (27 120) is higher than 2024 (24 260), which contradicts the textual claim of monotonic growth from 2018 to 2024. Please verify the source tables or provide the source files/CSVs so we can correct the reconstruction.

---

## 2. Definicje i zakres pojęciowy (ważne techniczne rozróżnienia)

- Władza rodzicielska (wspólna vs. wyłączna): w polskim Kodeksie rodzinnym i opiekuńczym "władza rodzicielska" odnosi się do praw i obowiązków rodzicielskich (decyzje wychowawcze, majątkowe). "Razem matce i ojcu" zwykle oznacza orzeczenie o wspólnej władzy rodzicielskiej, ale nie determinuje miejsca zamieszkania dziecka.
- Opieka naprzemienna / piecza naprzemienna (physical shared custody): układ, w którym dziecko regularnie zmienia miejsce zamieszkania między rodzicami (faktyczna zamiana miejsca pobytu) — to inny koncept niż sama wspólna władza.
- "Oddzielnie matce i ojcu" (rekonstruowane kategorie statystyczne) — wskazuje na rozdzielenie kompetencji lub kontakty, niekoniecznie realną opiekę naprzemienną.

Z tego powodu każda analiza łącząca "wspólną władzę" z efektami społecznymi (np. przemocą) musi najpierw potwierdzić, czy decyzje o wspólnej władzy rzeczywiście zwiększają udział fizycznej opieki naprzemiennej.

---

## 3. Co można wnioskować (ostrożnie)

- Opis: System sądowy coraz częściej orzeka wspólną władzę rodzicielską — to widoczny trend w zrekonstruowanych danych.
- Nie da się jednak z tych danych stwierdzić, że wzrost wspólnej władzy prowadzi do wzrostu opieki naprzemiennej ani do spadku przemocy partnerskiej bez dodatkowych powiązań danych (policja, NK, zdrowie).
- Wszystkie przekłady na "liczby uratowanych żyć" lub "procentowy spadek zabójstw" należy traktować jako spekulatywne, back-of-envelope i wyraźnie oznaczać założenia.

---

## 4. Problem badawczy: brak naturalnego eksperymentu w Polsce

- Badanie Fernández‑Kranz et al. (2021) wykorzystało heterogeniczną, regionalną implementację reform (Hiszpania, 2010–2015). W Polsce brak jednolitej reformy oraz jednolity system prawny — zmiany następują przez orzecznictwo.
- W związku z tym nie można bezpośrednio przenieść tego samego designu; potrzebne są alternatywne strategie identyfikacji (opisane dalej).

---

## 5. Proponowany plan empiryczny — konkretne kroki (jak udowodnić to w Polsce)

1. Zebranie danych:
   - Orzeczenia sądów rodzinnych na poziomie okręgów/powiatów (panel 2015–2024) z rozbiciem na typ orzeczenia (wspólna władza vs wyłączna, i jeśli możliwe — notatka o miejscu pobytu dziecka).
   - Dane policji/KSIP — Niebieska Karta (NK), zgłoszenia przemocy domowej, interwencje (powiat/okręg).
   - Dane MS o skazaniach za przemoc (art. 207, 148 itd.) z geokodowaniem na powiat.
   - Dane zdrowotne (hospitalizacje z urazami pourazowymi, zgłoszenia SOR).
2. Strategia identyfikacji:
   - Wykorzystać różnice w praktyce sądowej między okręgami (różne kolegia, różna "kultura" orzekania) jako quasi‑eksperyment: diff-in-diff lub event-study.
   - Instrumenty: rotacje sędziowskie, zmiany w składach wydziałów rodzinnych, wprowadzenie lokalnych wytycznych.
   - Robust checks: pre‑trendy, placebo outcomes, bounding.
3. Metryki wyników:
   - Liczba zgłoszeń NK, liczba interwencji policji, liczba zawiadomień o przemocy przy separacji, liczba zabójstw partnerów (female homicides), hospitalizacje.
4. Etapy i pilotaż:
   - Pilotaż w wybranych okręgach sądowych z dodatkowym monitoringiem po orzeczeniu (follow-up).
   - Wnioski do finansowania z Daphne / Barnahus (wykorzystać zalecenie UE).

---

## 6. Polityka i prawo — jak wykorzystać wnioski

Sugerowane, krótkie rekomendacje polityczne (bez przesądzania o modelu custody):
1. Finansować badanie pilotażowe z powiązaniem danych sądowych i policyjnych (z wykorzystaniem funduszy UE, np. Daphne).
2. Wprowadzić obowiązkowe, interdyscyplinarne oceny ryzyka przed wydaniem decyzji o miejscu pobytu dziecka (psycholog, służby społeczne, policja).
3. Wzmacniać mechanizmy monitoringu po orzeczeniu (systemy zgłaszania problemów, follow-up).
4. Przy dyskusjach legislacyjnych powoływać się na zasadę "najlepszego interesu dziecka" i dowodową ocenę skutków różnych modeli opieki (Zalecenie Rady (UE) 2024/1238 może służyć jako polityczne wsparcie, ale nie zastępuje dowodów empirycznych).

Uwaga prawna: Zalecenie Rady (UE) 2024/1238 ma charakter niewiążący (soft law). Nie przesądza o tym, który model pieczy jest lepszy — wymaga natomiast indywidualnej oceny sytuacji dziecka.

---

## 7. Ograniczenia i ryzyka analityczne

- Błąd pomiaru: "wspólna władza" ≠ opieka naprzemienna.
- Selekcja: sprawy trafiające do sądów mogą być niefunkcjonalnie wyselekcjonowane (wysoki konflikt).
- Brak spójnych danych na poziomie lokalnym: NK i policja często nie są jawne lub są niekompletne.
- Ryzyko interpretacyjne: nawet silna korelacja nie musi oznaczać efektu przyczynowego.

---

## 8. Data & Methods — jak przygotować replikację (checklista)

- Źródła pierwotne: podaj bezpośrednie linki do plików GUS (tabele roczne), do publikacji MS z orzeczeniami (CSV/Excel) i do statystyk policyjnych. Dołącz zrekonstruowane CSV(y) do repozytorium.
- Reprodukowalność: dołącz notebook (Jupyter / R Markdown) z krokami:
  1. Import surowych plików,
  2. Kodowanie kategorii (co liczymy jako "Razem matce i ojcu"),
  3. Sumy kontrolne (suma wierszy = "Razem"),
  4. Wykresy i tabele.
- Walidacja: dodaj testy sumaryczne (np. sumy roczne z GUS porównane z sumami per kategoria).
- Weryfikacja anomalii: zaznacz wszystkie niezgodności (np. opisany 2023→2024). 

Przykładowy skrypt (appendix): prosty skrypt do wczytania CSV i wykresów (Python).

---

## 9. Appendix — przykładowy, prosty skrypt do wykresu (umieść plik `custody_reconstructed_2018_2024.csv` w repo)

```python
# name=plot_trends.py
# Simple example: load CSV and plot counts & shares over time
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("custody_reconstructed_2018_2024.csv")  # CSV with columns: Rok, Matce, Ojcu, Razem_matce_i_ojcu, ...
df = df.sort_values("Rok")
df['Razem'] = df[['Matce','Ojcu','Razem_matce_i_ojcu','Oddzielnie_matce_i_ojcu','Rodzinie_zastepczej','Placowce_wychowawczej','Inne']].sum(axis=1)

plt.figure(figsize=(9,5))
plt.plot(df['Rok'], df['Razem_matce_i_ojcu'], marker='o', label='Razem (władza)')
plt.plot(df['Rok'], df['Matce'], marker='o', label='Matce (wyłączna)')
plt.plot(df['Rok'], df['Ojcu'], marker='o', label='Ojcu (wyłączna)')
plt.ylabel('Liczba orzeczeń')
plt.xlabel('Rok')
plt.title('Orzeczenia o wykonywaniu władzy rodzicielskiej 2018–2024 (rekonstrukcja)')
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('figures/custody_trends.png', dpi=150)
```

---

## 10. Źródła (do uzupełnienia permalinks i plików źródłowych)

- Fernández‑Kranz, D., Nollenberger, N., & Roff, J. (2021). Bargaining Power in the Household: The Effect of Shared Custody on Intimate Partner Violence. Journal of Labor Economics.
- Dee, T.S. (2003). Until Death Do You Part: The Effects of Unilateral Divorce on Spousal Homicides. IZA Discussion Paper.
- Bauserman, R. (2012). A Meta-analysis of Parental Satisfaction, Adjustment, and Conflict in Joint Custody and Sole Custody Following Divorce. Journal of Divorce & Remarriage.
- Zalecenie Rady (UE) 2024/1238 z dnia 14 maja 2024 r. (ELI: http://data.europa.eu/eli/reco/2024/1238/oj)
- Stenogram z 15. posiedzenia Senatu RP X kadencji, 11 września 2020 r. (punkt 8).
- Pismo RPD Moniki Horna‑Cieślak, sygn. PI79-01/7.
- Konstytucja RP, art. 18, 48, 71, 72.
- Art. 190a Kodeksu karnego (uporczywe nękanie).

(Uzupełnij o bezpośrednie URL-e do konkretnych tabel GUS i plików MS; jeśli chcesz, mogę pomóc je pobrać i dodać do repo.)

---

## 11. Krótkie podsumowanie i następne kroki — checklist dla Ciebie

1. Zweryfikuj źródłowe pliki GUS/MS i popraw/zaakceptuj liczby w tabeli (szczególnie 2023→2024).
2. Dodaj surowe CSV(y) oraz notebook do repo (sekcja Appendix).
3. Jeśli chcesz, udostępnij dostęp do plików GUS/MS (linki) lub dodaj je tutaj — mogę wtedy zaktualizować tabelę i wygenerować wykresy.
4. Po weryfikacji: zaprojektuję analizę empiryczną (kod + opis identyfikacji, testy, wykresy), mogę też utworzyć PR z tą zaktualizowaną wersją.

---
