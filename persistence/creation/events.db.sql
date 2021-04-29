BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "locations" (
	"id"	INTEGER NOT NULL UNIQUE,
	"city"	TEXT NOT NULL,
	"country"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "organisations" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"location_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("location_id") REFERENCES "locations"("id")
);
CREATE TABLE IF NOT EXISTS "events" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"type"	TEXT NOT NULL CHECK("type" == "Seminar" OR "type" == "Workshop" OR "type" == "Presentation"),
	"host_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("host_id") REFERENCES "organisations"("id")
);
CREATE TABLE IF NOT EXISTS "presenters" (
	"id"	INTEGER NOT NULL UNIQUE,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"organisation_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("organisation_id") REFERENCES "organisations"("id")
);
CREATE TABLE IF NOT EXISTS "event_presenters" (
	"presenter_id"	INTEGER NOT NULL,
	"event_id"	INTEGER NOT NULL,
	FOREIGN KEY("presenter_id") REFERENCES "presenters"("id"),
	FOREIGN KEY("event_id") REFERENCES "events"("id")
);
INSERT INTO "locations" VALUES (1,'Southampton','UK');
INSERT INTO "locations" VALUES (2,'London','UK');
INSERT INTO "locations" VALUES (3,'Atlanta','USA');
INSERT INTO "locations" VALUES (4,'Kinshasa','DRC');
INSERT INTO "locations" VALUES (5,'Paris','FR');
INSERT INTO "organisations" VALUES (1,'Training World',1);
INSERT INTO "organisations" VALUES (2,'Bam Productions',2);
INSERT INTO "organisations" VALUES (3,'Kaizen Corp',3);
INSERT INTO "organisations" VALUES (4,'Top World',4);
INSERT INTO "organisations" VALUES (5,'Chasers',5);
INSERT INTO "events" VALUES (1,'101 Coding Nights','Workshop',1);
INSERT INTO "events" VALUES (2,'Caw Blimey','Seminar',2);
INSERT INTO "events" VALUES (3,'Recording Live','Workshop',3);
INSERT INTO "events" VALUES (4,'Cuisine 101','Workshop',4);
INSERT INTO "events" VALUES (5,'Random Nights','Presentation',5);
INSERT INTO "presenters" VALUES (1,'Prins','Butt',1);
INSERT INTO "presenters" VALUES (2,'Chez','Chriss',2);
INSERT INTO "presenters" VALUES (3,'Kaizen','Grace',3);
INSERT INTO "presenters" VALUES (4,'Guy','Waku',4);
INSERT INTO "presenters" VALUES (5,'Mamie','Kokolo',5);
INSERT INTO "event_presenters" VALUES (1,1);
INSERT INTO "event_presenters" VALUES (2,2);
INSERT INTO "event_presenters" VALUES (3,3);
INSERT INTO "event_presenters" VALUES (4,4);
INSERT INTO "event_presenters" VALUES (5,5);
COMMIT;
