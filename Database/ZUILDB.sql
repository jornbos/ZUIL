
CREATE TABLE moderator(
ModNaam VARCHAR(255) NOT NULL,
ModMail VARCHAR(255) NOT NULL,
PRIMARY KEY(ModNaam)
);

CREATE TABLE station(
Stationnaam VARCHAR(255) NOT NULL,
Land VARCHAR(255) NOT NULL,
ovfietsinfo VARCHAR(255) NOT NULL,
liftinfo VARCHAR(255) NOT NULL,
toiletinfo VARCHAR(255) NOT NULL,
prinfo VARCHAR(255) NOT NULL,
PRIMARY KEY(Stationnaam)
);

CREATE TABLE bericht(
Naam VARCHAR(255) NOT NULL,				 
Bericht VARCHAR(140) NOT NULL,
datum_tijd TIMESTAMP NOT NULL,
Stationnaam VARCHAR(255) NOT NULL,
Goedgekeurd_door VARCHAR(255) NOT NULL,
Mailadres VARCHAR(255) NOT NULL,
Goedgekeurd_tijd TIME NOT NULL,
FOREIGN KEY (Goedgekeurd_door) REFERENCES moderator(ModNaam),
FOREIGN KEY (Stationnaam) REFERENCES station(stationnaam)
);

INSERT INTO moderator VALUES ('jorn bos', 'jorn.bos@student.hu.nl');

INSERT INTO station (
stationnaam, land, ovfietsinfo, liftinfo, toiletinfo, prinfo)
VALUES
('Arnhem', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Almere', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Amersfoort', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Almelo', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Alkmaar', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Apeldoorn', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Assen', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Amsterdam', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Boxtel', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Breda', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Dordrecht', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Delft', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Deventer', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Enschede', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Gouda', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Groningen', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Den Haag', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Hengelo', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Haarlem', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Helmond', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Hoorn', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Heerlen', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Den Bosch', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Hilversum', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Leiden', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Lelystad', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Leeuwarden', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Maastricht', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Nijmegen', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Oss', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Roermond', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Roosendaal', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Sittard', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Tilburg', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Utrecht', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Venlo', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Vlissingen', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Zaandam', 'NL', 'nee', 'ja', 'nee', 'ja'),
('Zwolle', 'NL', 'ja', 'nee', 'ja', 'nee'),
('Zutphen', 'NL', 'nee', 'ja', 'nee', 'ja');
