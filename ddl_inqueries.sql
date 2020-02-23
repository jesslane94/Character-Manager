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

/* Create Charaacter Table */
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
   guild_specialization VARCHAR(255) NOT NULL,
   char_id int(11),
   FOREIGN KEY(char_id) REFERENCES characters(char_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE classes (
   class_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
   class_name VARCHAR(255) NOT NULL,
   stat_bonus VARCHAR(255) NOT NULL,
   char_id int(11) NOT NULL,
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
        ON UPDATE CASCADE 
);

CREATE TABLE characters_spells (
    char_id INT(11) NOT NULL,
    spell_id INT(11) NOT NULL,
    FOREIGN KEY(char_id) REFERENCES characters(char_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY(spell_id) REFERENCES spells(spell_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE 
);

/*Insert Values into the Tables */
INSERT INTO characters (:first_name, :last_name, :strength, :dexterity, :endurance, :intelligence)
VALUES ("Grey", "Skull", 1/2, 15, 13, 8),
       ("Dryany", "Enyn", 8, 12, 8, 15),
       ("Adriel", "Serielye", 10, 15, 12, 11);

INSERT INTO spells (:spell_name, :spell_level, :spell_description) 
VALUES ("Fireball", "Level 1", "Shoots a fireball. Caution: It's hot."),
    ("Healing Touch", "Level 1", "Restores 5-10 HP to Target."), 
    ("Cast Light", "Level 1", "Makes an object you touch glow. Yippee!");

INSERT INTO guilds (:guild_name, :guild_specialization)
VALUES ("Merchants", "You like? You buy! I give you a good price"),
       ("Mages", "Never trust a mage"),
       ("Dark Brotherhood", "I just want a nightmare'ish looking horse to ride on");

INSERT INTO classes (:class_name, :stat_bonus) 
VALUES ("Rogue", "+2 Dexterity"),
    ("Bard","+2 Charisma"), 
    ("Fighter", "+2 Strength");