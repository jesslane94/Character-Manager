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
    last_name VARCHAR(255) NOT NULL
);
