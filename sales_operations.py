
# Funkcija za ukupnu količinu prodatih proizvoda

def total_sold(sales):
    return sum(sales.values())

# Lambda funkcija - Najprodavaniji proizvod

def most_sold_product(sales):
    return max(sales, key=lambda s: sales[s])

# Lambda funkcija - najmanje prodavan proizvod 

def least_sold_product(sales):
    return min(sales, key=lambda s: sales[s])

# Lambda funkcija za kreiranje liste kriticnih proizvoda i ispis

def critical_sales(sales):
	return list(filter(lambda s: sales[s] < 50, sales))

# Funkcija za proveru validnosti podataka i ispis

def validate_sales_data(sales):
    validno = True

    for key, value in sales.items():
        
        if value < 0:
            validno = False
            print(f"Error: Proizvod '{key}' ima negativnu količinu ({value})!")
        elif value > 100000:
            validno = False
            print(f"Error: Proizvod '{key}' ima neuobičajeno visoku količinu ({value})!")

    if validno:
        print("Svi podaci su validni. Ne postoji proizvod sa negativnom količinom ili neuobičajeno visokom vrednošću!")

    return validno
    
# Funkcija za dobijanje broja prodaje za dati proizvod i obradu izuzetaka

def get_product_sales(sales, product_name):
    
    try:
        return sales[product_name]  # pokušavamo da uzmemo vrednost direktno
    except KeyError:
        return f"Proizvod '{product_name}' nije pronađen."
    except Exception as e:
        return f"Došlo je do greške: {e}"  # hvata sve ostale neočekivane greške


   
    