import datetime
from icalendar import Calendar, Event

# Guatemalan Mayan Tzolk'in day names (day protectors)
day_protectors = [
    "Imox", "Iq'", "Ajpu", "Kat", "Kan", "Kame", "Kej", "Q'anil", 
    "Toj", "Tz'i'", "B'atz'", "E", "Aj", "Ix", "Tz'ikin", "Ajmaq", 
    "No'j", "Tijax", "Kawoq", "Ajpu"
]

# Start and end dates
start_date = datetime.date(1960, 1, 1)
end_date = datetime.date(2100, 12, 31)

# Tzolk'in starting point (arbitrary reference date with known Mayan date)
reference_date = datetime.date(2024, 11, 7)
reference_number = 1  # Ajpu
reference_protector = 19  # Ajpu

def get_mayan_date(gregorian_date):
    days_difference = (gregorian_date - reference_date).days
    tzolkin_number = ((reference_number + days_difference - 1) % 13) + 1
    tzolkin_protector = day_protectors[(reference_protector + days_difference) % 20]
    return tzolkin_number, tzolkin_protector

# Create calendar
cal = Calendar()

# Iterate over each day in the date range
current_date = start_date
while current_date <= end_date:
    tzolkin_number, tzolkin_protector = get_mayan_date(current_date)
    event = Event()
    event.add('summary', f'Mayan Day: {tzolkin_number} {tzolkin_protector}')
    event.add('dtstart', current_date)
    event.add('dtend', current_date + datetime.timedelta(days=1))
    event.add('description', f'The Mayan Tzolk\'in date for today is {tzolkin_number} {tzolkin_protector}.')
    cal.add_component(event)
    current_date += datetime.timedelta(days=1)

# Save to .ics file
with open('mayan_calendar.ics', 'wb') as f:
    f.write(cal.to_ical())

print("Calendar created successfully.")
