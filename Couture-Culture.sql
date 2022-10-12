BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Remeras" (
	"nombreRemera"	INTEGER,
	"marcaRemera"	TEXT,
	"precioRemera"	TEXT,
	"colorRemera"	TEXT,
	PRIMARY KEY("nombreRemera")
);
CREATE TABLE IF NOT EXISTS "Zapatillas" (
	"modeloZapatilla"	INTEGER,
	"marcaZapatilla"	TEXT,
	"precioZapatilla"	TEXT,
	"colorZapatilla"	TEXT,
	PRIMARY KEY("modeloZapatilla"),
	FOREIGN KEY("modeloZapatilla") REFERENCES "Marca"("Zapatillas")
);
CREATE TABLE IF NOT EXISTS "Buzos" (
	"nombreBuzo"	INTEGER,
	"marcaBuzo"	TEXT,
	"precioBuzo"	TEXT,
	"colorBuzo"	TEXT,
	PRIMARY KEY("nombreBuzo")
);
CREATE TABLE IF NOT EXISTS "Marca" (
	"nombreMarca"	TEXT,
	"Zapatillas"	TEXT,
	"Buzos"	TEXT,
	"Remeras"	TEXT,
	"Pantalones"	TEXT,
	PRIMARY KEY("nombreMarca")
);
CREATE TABLE IF NOT EXISTS "Login" (
	"Id"	INTEGER,
	"Contraseña"	TEXT,
	"Nombre Completo"	TEXT,
	"Mail"	TEXT,
	PRIMARY KEY("Id")
);
INSERT INTO "Remeras" VALUES (0,NULL,NULL,NULL);
INSERT INTO "Marca" VALUES ('1',NULL,NULL,NULL,'');
INSERT INTO "Marca" VALUES ('Nike',NULL,NULL,NULL,NULL);
COMMIT;
