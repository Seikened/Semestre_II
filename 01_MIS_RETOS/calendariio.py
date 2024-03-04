import calendar
from datetime import date


today = date.today()
print("Hoy es:", today.strftime("%d/%m/%Y"))
yy = today.year
mm = today.month
print("Calendario del mes actual:")
print(calendar.month(yy, mm))
print("")
