leap_years = []
years = list(range(1900,2025))

for year in years:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # es año bisiesto
                leap_years.append(year)
        else:
            # es año bisiesto
            leap_years.append(year)

print(f"Hay {len(leap_years)} años bisiestos desde 1900 hasta 2024 y son:")
for  leap_year in leap_years:
    print(f"-{leap_year}")