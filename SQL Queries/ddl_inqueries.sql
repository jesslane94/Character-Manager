/*
drop statements to clear out old records if they exist
*/

DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS guilds;
DROP TABLE IF EXISTS spells;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS classes_spells;
DROP TABLE IF EXISTS characters_spells;

/* Create Tables */
/* Create Character Table */
CREATE TABLE characters (
    char_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    strength INT(11) NOT NULL,
    dexterity INT(11) NOT NULL,
    endurance INT(11) NOT NULL,
    intelligence INT(11) NOT NULL
);


CREATE TABLE spells (
    spell_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    spell_name VARCHAR(255) NOT NULL,
    spell_level VARCHAR(255) NOT NULL,
    spell_description VARCHAR(255) NOT NULL
);


CREATE TABLE guilds (
   guild_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
   guild_name VARCHAR(255) NOT NULL,
   guild_description VARCHAR(255) NOT NULL,
   char_id int(11),
   FOREIGN KEY(char_id) REFERENCES characters(char_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE classes (
   class_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
   class_name VARCHAR(255) NOT NULL,
   stat_bonus VARCHAR(255) NOT NULL,
   char_id int(11) NULL,
   FOREIGN KEY(char_id) REFERENCES characters(char_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE classes_spells (
    class_id INT(11) NOT NULL,
    spell_id INT(11) NOT NULL,
    FOREIGN KEY(class_id) REFERENCES classes(class_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY(spell_id) REFERENCES spells(spell_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT AK_Character_Spells UNIQUE (char_id, spell_id)
);

/*Unsure if this will be implemented 
CREATE TABLE characters_spells (
    char_id INT(11) NOT NULL,
    spell_id INT(11) NOT NULL,
    FOREIGN KEY(char_id) REFERENCES characters(char_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY(spell_id) REFERENCES spells(spell_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE 
);*/