
# Uvoz modula sales_operation

import sales_operations as so

def main():
# Rečnik sales

    sales = {
        "Laptop": 15,
        "Mouse": 150,
        "Keyboards": 85,
        "Monitor": 30,
        "USB cables": 200  
    }

# Dodavanje proizvoda - Web camera

    if "Web camera" not in sales:
        sales["Web camera"] = 0
    
# Povecavanje broja prodatih jedinica - Monitor(+5)

    sales["Monitor"] += 5

# Funkcija za ukupnu količinu prodatih proizvoda

    total = so.total_sold(sales)

# poziv funkcija - Najprodavaniji proizvod ime i vrednost

    max_name = so.most_sold_product(sales)

    max_value = so.get_product_sales(sales, max_name)

# poziv funkcija - najmanje prodavan proizvod ime i vrednost

    min_name = so.least_sold_product(sales)

    min_value = so.get_product_sales(sales, min_name)

# Ispis ažuriranog rečnika i rezultata

    print("\nSales:\n")
    for key, value in sales.items():
        print(f"{key}: {value} jedinica")

    print("\nUkupna kolicina prodatih proizvoda:", total)
    print(f"Proizvod koji se najvise prodavao je: {max_name}, sa ukupno {max_value} jedinica.")
    print(f"Proizvod koji se najmanje prodavao je: {min_name}, sa ukupno {min_value} jedinica.")
    print(f"Proizvodi sa kriticnom prodajom su: {so.critical_sales(sales)}")

# poziv funkcija za proveru validnosti podataka i ispis

    so.validate_sales_data(sales)

# Ovo pokreće program samo ako se main.py pokrene direktno
if __name__ == "__main__":
    main()
