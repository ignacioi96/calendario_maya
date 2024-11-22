import datetime
from icalendar import Calendar, Event

import datetime

# Correct Guatemalan Mayan Tzolk'in day names (day protectors)
day_protectors = [
    "Imox", "Iq'", "Aq'ab'al", "Kat", "Kan", "Kame", "Kej", "Q'anil", 
    "Toj", "Tz'i'", "B'atz'", "E", "Aj", "Ix", "Tz'ikin", "Ajmaq", 
    "No'j", "Tijax", "Kawoq", "Ajpu"
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
    tzolkin_protector = day_protectors[tzolkin_protector_index]
    return tzolkin_number, tzolkin_protector

# Test Date: November 21, 2024
test_date = datetime.date(2024, 11, 21)

# Get the Mayan date for the test date
test_mayan_date = get_mayan_date(test_date)
print(test_date, ': ', test_mayan_date)

# Create calendar
cal = Calendar()

# Iterate over each day in the date range
current_date = start_date
while current_date <= end_date:
    tzolkin_number, tzolkin_protector = get_mayan_date(current_date)
    event = Event()
    event.add('summary', f'Nahual del día: {tzolkin_number} {tzolkin_protector}')
    event.add('dtstart', current_date)
    event.add('dtend', current_date + datetime.timedelta(days=1))
    event.add('description', f'El Tzolk\'in Maya para el día de hoy es {tzolkin_number} {tzolkin_protector}.')
    cal.add_component(event)
    current_date += datetime.timedelta(days=1)

# Save to .ics file
with open('mayan_calendar.ics', 'wb') as f:
    f.write(cal.to_ical())

print("Calendar created successfully.")
