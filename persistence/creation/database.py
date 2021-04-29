import sqlite3


def display_presenters():
    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    sql = """
       SELECT p.first_name, p.last_name, o.name 
       FROM presenters p 
       INNER JOIN organisations o ON p.organisation_id = o.id;
       """
    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(f"{record[0]} ({record[1]})")


def display_events():
    db = sqlite3.connect("events.db")
    cursor = db.cursor()


    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    sql = """
       SELECT e.name AS "event", l.city, l.country 
       FROM events e 
       INNER JOIN organisations O ON e.host_id = o.id 
       INNER JOIN locations l ON o.location_id = l.id;
       """
    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
      print(f"{record[0]} ({record[1]}, {record[2]})")


def display_presenters_for_event(event_id):
    db = sqlite3.connect("events.db")
    cursor = db.cursor()

    sql = "SELECT presenter.first_name, presenter.last_name, event.name" \
          "FROM events " \
          "INNER JOIN event_presenters ep ON ep.presenter_id = presenter.id" \
          f"WHERE e.id = {event_id}"
    cursor.execute(sql)
    records = cursor.fetchall()

    for record in records:
        print(record)

def display_events_for_presenter(presenter_id):
    db = sqlite3.connect('events.db')
    cursor = db.cursor()
    sql = "SELECT p.first_name, p.last_name " \
          "FROM presenters p " \
          f"WHERE presenter.id = {presenter_id}"
    values = [presenter_id]
    cursor.execute(sql, values)
    record = cursor.fetchone()

    for record in record:
        print(record)

    sql = "SELECT event.name" \
          "FROM events e" \
          "INNER JOIN event_presenters ep ON ep.event_id = event.id" \
          "INNER JOIN presenters p ON ep.presenter_id = presenter.id" \
          f"WHERE presenter.id = {presenter_id}"
    cursor.execute(sql, values)
    records = cursor.fetchall()

    print("The events for this presenter are as follows:")
    for record in records:
        print(record)