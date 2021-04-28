BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "organisations" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"location_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "locations" (
	"id"	INTEGER NOT NULL UNIQUE,
	"city"	TEXT NOT NULL,
	"country"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "presenters" (
	"id"	INTEGER NOT NULL UNIQUE,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"organisation_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "event_presenters" (
	"presenter_id"	INTEGER NOT NULL,
	"event_id"	INTEGER NOT NULL,
	FOREIGN KEY("presenter_id") REFERENCES "presenters"("id"),
	FOREIGN KEY("event_id") REFERENCES "events "("id")
);
CREATE TABLE IF NOT EXISTS "events " (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"type"	INTEGER NOT NULL CHECK("type" == "Seminar" OR "type" == "Workshop" OR "type" == "Presentation"),
	"host_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("host_id") REFERENCES "organisations"("id")
);
COMMIT;
