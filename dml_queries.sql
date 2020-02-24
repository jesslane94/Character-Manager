/*INSERT STATEMENTS*/
INSERT INTO characters (first_name, last_name, strength, dexterity, endurance, intelligence)
VALUES ( firstname_input, lastname_input, str_input, dex_input, end_input, int_input)

INSERT INTO spells (spell_name, spell_level, spell_description)
VALUES ( spell_name_input, spell_level_input, spell_description_input)

INSERT INTO guilds (guild_name, guild_specialization)
VALUES ( guild_name_input, guild_specialization_input)

INSERT INTO classes (class_name, stat_bonus)
VALUES ( class_name_input, stat_bonus_input)

/*SELECT VALUES FROM TABLES */
SELECT first_name, last_name 
FROM characters;

SELECT spell_id
FROM spells
WHERE spell_id = 1;

SELECT * 
FROM guilds
WHERE guild_name = "Mages";

/* added this - Jess */
SELECT class_id
FROM classes
WHERE class_id = 1;


/*UPDATE VALUES FROM TABLES */
UPDATE characters
SET first_name = first_name_input, last_name = lastname_input, strength = str_input, dexterity = dex_input, endurance = end_input, intelligence =  int_input)
WHERE char_id = char_id_input;

UPDATE spells
SET spell_level = "Level 2"
WHERE spell_name = "Fireball";

UPDATE guilds
SET guild_name = "The Former Dark Brotherhood"
WHERE guild_name = "Dark Brotherhood";

/*added this - Jess */
UPDATE classes
SET class_name = "Ranger"
WHERE class_name = "Rogue";


/*DELETE VALUES FROM TABLES */
DELETE FROM characters
WHERE char_id = char_id_input;

DELETE FROM classes
WHERE class_id = 3;

DELETE FROM spells
WHERE spell_level = "Level 2";

/* added this one - Jess */
DELETE FROM guilds
WHERE guild_id = 1;