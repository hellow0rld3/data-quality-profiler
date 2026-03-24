# Data Quality Profiler & Cleaner 🧹

Prosta, ale skuteczna aplikacja webowa do automatycznego profilowania, oceny i czyszczenia brudnych zestawów danych (plików CSV). Projekt wykorzystuje metody statystyczne oraz modele uczenia maszynowego (ML) do przygotowywania surowych danych pod dalsze analizy.


[Link do strony](https://data-profiler-cszczepanek.streamlit.app/)

## Główny cel projektu
Automatyzacja najbardziej powtarzalnej części pracy Data Scientist – czyszczenia danych, przy zachowaniu maksymalnej ilości użytecznych informacji.

## Funkcjonalności

* **Data Quality Score:** Automatyczna ocena jakości wgranego pliku (0-100%) kalkulowana na podstawie odsetka pustych komórek oraz zduplikowanych wierszy.
* **Smart Imputation:** Inteligentne uzupełnianie braków w kolumnach numerycznych. Algorytm w locie analizuje odchylenie standardowe i średnią danej kolumny, aby zadecydować, czy użyć do imputacji średniej (dla danych stabilnych) czy mediany (dla danych z dużym rozrzutem).
* **Detekcja Anomalii (ML):** Wbudowany model **Isolation Forest** (wraz z automatyczną standaryzacją `StandardScaler`), który w sposób nienadzorowany przeszukuje wymiary numeryczne i flaguje wartości odstające w nowej kolumnie `outlier_IF`.
* **Architektura Mikroserwisów:** Pełne oddzielenie logiki obliczeniowej (REST API) od interfejsu użytkownika.

## Technologie i Architektura

Aplikacja składa się z dwóch niezależnych modułów komunikujących się przez protokół HTTP:

**Back-end (Silnik API):** FastAPI, Uvicorn, Pandas, Scikit-learn.
* Hostowany w chmurze **Render**.


**Front-end (Interfejs):** Streamlit, Requests.
* Hostowany na **Streamlit Community Cloud**.



## Uruchomienie lokalne

Aby uruchomić projekt na własnym komputerze, sklonuj to repozytorium i zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt
```

Następnie uruchom oba serwery w dwóch osobnych oknach terminala:

## Terminal 1 (Uruchomienie API)

```bash
uvicorn app.main:app --reload
```

API będzie dostępne pod adresem http://localhost:8000 (Swagger UI pod /docs).

## Terminal 2 (Uruchomienie Interfejsu)

```bash
streamlit run app/frontend.py
```

Interfejs otworzy się automatycznie w przeglądarce pod adresem: http://localhost:8501 .

