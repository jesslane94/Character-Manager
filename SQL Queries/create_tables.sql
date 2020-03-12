CREATE TABLE guilds (
   guild_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
   guild_name VARCHAR(255) NOT NULL,
   guild_description VARCHAR(255) NOT NULL
);

CREATE TABLE classes (
   class_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
   class_name VARCHAR(255) NOT NULL,
   stat_bonus int(11) NOT NULL,
   stat_bonus_name varchar(255) NOT NULL
);

CREATE TABLE characters (
    char_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NULL,
    strength INT(11) NOT NULL,
    dexterity INT(11) NOT NULL,
    endurance INT(11) NOT NULL,
    intelligence INT(11) NOT NULL,
    guild_id INT(11) NULL,
    class_id INT(11) NULL,
    FOREIGN KEY(guild_id) REFERENCES guilds(guild_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY(class_id) REFERENCES classes(class_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE       
);

CREATE TABLE spells (
    spell_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    spell_name VARCHAR(255) NOT NULL,
    spell_level INT(11) NOT NULL,
    spell_description VARCHAR(255) NOT NULL
);

CREATE TABLE characters_spells (
    char_id INT(11) NOT NULL,
    spell_id INT(11) NOT NULL,
    FOREIGN KEY(char_id) REFERENCES characters(char_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY(spell_id) REFERENCES spells(spell_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT characters_spells UNIQUE (char_id, spell_id)
);

