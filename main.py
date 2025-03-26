import datetime
from icalendar import Calendar, Event

# Correct Guatemalan Mayan Tzolk'in day names (day protectors) and translations
nawales = [
    ("Imox", "Agua, imaginación, locura, inconsciente"), ("Iq'", "Viento, espíritu, aliento de vida"), ("Ak'ab'al", "Amanecer, oscuridad, nuevo ciclo"),
    ("K'at", "Red, enredo, cautiverio, abundancia"), ("Kan", "Serpiente, energía, sabiduría, movimiento"), ("Keme", "Muerte, transformación, renacimiento"),
    ("Kiej", "Venado, equilibrio, fuerza, estabilidad"), ("Q'anil", "Semilla, creación, vida, maduración"), ("Toj", "Ofrenda, pago, fuego, justicia cósmica"),
    ("Tz'i'", "Perro, justicia, ley, fidelidad"), ("B'atz'", "Hilo del tiempo, continuidad, arte, tejido"), ("E", "Camino, destino, viaje, guía"),
    ("Aj", "Caña, autoridad, hogar, protección"), ("I'x", "Jaguar, feminidad, tierra, energía femenina"), ("Tz'ikin", "Pájaro, visión, libertad, fortuna"),
    ("Ajmaq", "Perdón, conocimiento, inteligencia, experiencias"), ("N'oj", "Sabiduría, pensamiento, mente, lógica"), ("Tijax", "Piedra de obsidiana, sanación, corte, limpieza"),
    ("Kawok", "Tormenta, purificación, abundancia, unidad"), ("Ajpu", "Sol, guerrero, fuerza, valentía"),
]

# Start and end dates for the calendar
start_date = datetime.date(1960, 1, 1)
end_date = datetime.date(2100, 12, 31)

# Tzolk'in starting point (known Mayan date for reference)
reference_date = datetime.date(2024, 11, 7)
reference_number = 1  # Ajpu
reference_protector = 18  # Ajpu (index 19)

def get_mayan_date(gregorian_date):
    days_difference = (gregorian_date - reference_date).days
    tzolkin_number = ((reference_number + days_difference - 1) % 13 + 13) % 13 + 1
    tzolkin_protector_index = (reference_protector + days_difference) % 20
    tzolkin_protector, translation = nawales[tzolkin_protector_index]
    return tzolkin_number, tzolkin_protector, translation

# Create calendar
cal = Calendar()

# Iterate over each day in the date range
current_date = start_date
while current_date <= end_date:
    tzolkin_number, tzolkin_protector, translation = get_mayan_date(current_date)
    event = Event()
    event.add('summary', f"{tzolkin_number} {tzolkin_protector} ({translation}) es el Cholq'ij del día")
    event.add('dtstart', current_date)
    event.add('dtend', current_date + datetime.timedelta(days=1))
    event.add('description', f"El Tzolk'in Maya para el día de hoy es {tzolkin_number} {tzolkin_protector}, que significa '{translation}' en español.")
    cal.add_component(event)
    current_date += datetime.timedelta(days=1)

# Save to .ics file
with open('mayan_calendar.ics', 'wb') as f:
    f.write(cal.to_ical())

print("Calendario creado exitosamente.")
