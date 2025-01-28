from ics import Calendar, Event
from datetime import datetime

# Funktion: Generiere ein Event mit dynamischen Updates
def create_event(name, start_time, end_time, uid, sequence):
    event = Event()
    event.name = name
    event.begin = start_time
    event.end = end_time
    event.uid = uid
    event.description = f"Dieses Event wurde zuletzt aktualisiert am {datetime.utcnow()}"
    event.sequence = sequence  # Version des Events
    return event

# Funktion: Schreibe Kalenderdatei
def write_calendar_file(calendar, file_name):
    with open(file_name, "w") as file:
        file.writelines(calendar.serialize_iter())
    print(f".ics-Datei gespeichert: {file_name}")

# Main-Logik
if __name__ == "__main__":
    # Erstelle einen Kalender
    calendar = Calendar()

    # Event-Parameter
    event_name = "Test-Event mit Updates"
    event_start = "2025-01-30 14:00:00"
    event_end = "2025-01-30 15:00:00"
    event_uid = "test-event-123@example.com"  # Bleibt gleich für Updates
    event_sequence = 1  # Startsequenz

    # Generiere das Event und füge es dem Kalender hinzu
    event = create_event(event_name, event_start, event_end, event_uid, event_sequence)
    calendar.events.add(event)

    # Schreibe die Kalenderdatei
    write_calendar_file(calendar, "calendar.ics")
