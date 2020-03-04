/*INSERT STATEMENTS*/
INSERT INTO characters (first_name, last_name, strength, dexterity, endurance, intelligence)
VALUES ( :firstname_input, :lastname_input, :str_input, :dex_input, :end_input, :int_input)

INSERT INTO spells (spell_name, spell_level, spell_description)
VALUES ( :spell_name_input, :spell_level_input, :spell_description_input)

INSERT INTO guilds (guild_name, guild_description)
VALUES ( :guild_name_input, :guild_description_input)

INSERT INTO classes (class_name, stat_bonus)
VALUES ( :class_name_input, :stat_bonus_input)

/*SELECT VALUES FROM TABLES */
SELECT first_name, last_name 
FROM characters;

SELECT spell_id
FROM spells
WHERE spell_id = :spell_id_input;

SELECT * 
FROM guilds
WHERE guild_name = :"userInput";

SELECT class_id
FROM classes
WHERE class_id = :class_id_input;


/*UPDATE VALUES FROM TABLES */
UPDATE characters
SET first_name = :first_name_input, last_name = :lastname_input, strength = :str_input, dexterity = :dex_input, endurance = :end_input, intelligence =  :int_input)
WHERE char_id = :char_id_input;

UPDATE spells
SET spell_level = :spell_lev_input
WHERE spell_name = :"userInput";

UPDATE guilds
SET guild_name = :"userInput"
WHERE guild_name = :"userInput";

UPDATE classes
SET class_name = :"userInput"
WHERE class_name = :"userInput";


/*DELETE VALUES FROM TABLES */
DELETE FROM characters
WHERE char_id = :char_id_input;

DELETE FROM classes
WHERE class_id = :class_id_input;

DELETE FROM spells
WHERE spell_level = :spell_lvl_input;

DELETE FROM guilds
WHERE guild_id = :guild_id_input;