Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.

Program po uruchomieniu wyświetla informację o dostępnych komendach:

    saldo
    sprzedaż
    zakup
    konto
    lista
    magazyn
    przegląd
    koniec

Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:

    saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
    sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
    zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
    konto - Program wyświetla stan konta.
    lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
    magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
    przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
    koniec - Aplikacja kończy działanie.

Dodatkowe wymagania:

    Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
    Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
    Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
    Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.

Używanie programu:

$ python magazyn.py opcje parametry < in.txt

Przypadki użycia w pliku dla vscode: launch.json

jak poniżej zostało przetestowane:
- [x] "args": ["saldo", "-1000", "podatek", "<", "in.txt"]
- [x] "args": ["zakup", "jetson", "40000", "5", "<", "in.txt"]
- [x] "args": ["sprzedaż", "jetson", "50000", "4", "<", "in.txt"]
- [x] "args": ["magazyn", "jetson", "raspberry", "arduino", "satel", "<", "in.txt"]
- [x] "args": ["konto", "<", "in.txt"]
- [x] "args": ["przegląd", "0", "1", "<", "in.txt"]
