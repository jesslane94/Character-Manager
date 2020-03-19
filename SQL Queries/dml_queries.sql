--  SELECT Queries THAT ARE USED TO POPULATE TABLES FOR ALL /VIEW ROUTES

--  From /viewCharacters
--  Used to view all the characters in the database. It will display all their states, their guild (if they are in one) and their class
SELECT characters.first_name, characters.last_name, characters.strength, characters.dexterity, characters.endurance, characters.intelligence, guilds.guild_name, classes.class_name, characters.char_id FROM characters LEFT JOIN guilds ON characters.guild_id = guilds.guild_id LEFT JOIN classes ON characters.class_id = classes.class_id

-- From /viewClasses
-- Displays each class, their stat bonus and the class description
SELECT class_name, stat_bonus_name, stat_bonus, class_id FROM classes

-- /From viewGuilds
-- Displays all the guilds and the guild information
SELECT guild_name, guild_description, guild_id FROM guilds

-- From/viewSpells
-- Displays the the spells in the database, including their spell level and the text description 

SELECT spell_name, spell_description, spell_level, spell_id FROM spells



-- SELECT QUERIES THAT ARE USED TO POPULATE DROP DOWN MENUS FROM /ADD ROUTES

-- From /addCharacter
-- Populate form for adding character
SELECT guild_id, guild_name FROM guilds
SELECT class_id, class_name FROM classes

-- From /addClass
-- Populate form for adding class
SELECT class_name, stat_bonus, stat_bonus_name FROM classes

-- From /addSpell
-- Populate form for adding spells
SELECT spell_name, spell_level, spell_description FROM spells

-- From /addGuild
-- Populate form for adding guild
SELECT guild_name, guild_description FROM guilds

-- INSERT QUERIES FROM ALL /ADD ROUTES

-- From /addCharacter
--Query to insert a new character into the database that has no guild
INSERT INTO characters (first_name, last_name, strength, dexterity, endurance, intelligence, class_id) VALUES (%s, %s, %s, %s, %s, %s, %s)

--Query to insert a new character into the database that does ahve a guild
INSERT INTO characters (first_name, last_name, strength, dexterity, endurance, intelligence, guild_id, class_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)

-- From /addClass
-- Query to insert a new class
INSERT INTO classes (class_name, stat_bonus, stat_bonus_name) VALUES (%s, %s, %s)

-- From /addGuilds
-- Query to insert a new a new guild
INSERT INTO guilds (guild_name, guild_description) VALUES (%s, %s)

-- From /addSpell
-- Query to add a new spell
INSERT INTO spells (spell_name, spell_level, spell_description) VALUES (%s, %s, %s)

-- UPDATE QUERIES FROM ALL /UPDATE ROUTES

-- From /updateCharacters
-- Populate form based on character id passed in
SELECT char_id, first_name, last_name, strength, dexterity, endurance, intelligence FROM characters WHERE char_id = %s % (id)
SELECT guild_id, guild_name FROM guilds
SELECT class_id, class_name FROM classes
SELECT spell_id, spell_name FROM spells
SELECT spells.spell_id, spells.spell_name FROM spells INNER JOIN characters_spells ON spells.spell_id = characters_spells.spell_id INNER JOIN characters ON characters_spells.char_id = characters.char_id WHERE characters.char_id = %s ORDER BY spells.spell_id % (id)

UPDATE characters SET first_name = %s, last_name = %s, strength = %s, dexterity  = %s, endurance = %s, intelligence = %s, guild_id = %s, class_id = %s  WHERE char_id = %s

INSERT INTO characters_spells (char_id, spell_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE char_id = %s, spell_id = %s

DELETE FROM characters_spells WHERE char_id = %s AND spell_id = %s

-- From /updateClass
-- Populate form based on class id passed in
SELECT class_id, class_name, stat_bonus, stat_bonus_name FROM classes WHERE class_id = %s % (id)

UPDATE classes SET class_name = %s, stat_bonus= %s, stat_bonus_name = %s WHERE class_id = %s

-- From /updateGuild
-- Populate form based on guild id passed in
SELECT guild_id, guild_name, guild_description FROM guilds WHERE guild_id = %s % (id)

UPDATE guilds SET guild_name= %s, guild_description = %s WHERE guild_id = %s

-- From /updateSpell
--Populate form based on spell id passed in
SELECT spell_id, spell_name, spell_level, spell_description FROM spells WHERE spell_id = %s % (id)

UPDATE spells SET spell_name= %s, spell_level= %s, spell_description = %s WHERE spell_id = %s

--Delete Queries
DELETE FROM characters WHERE char_id = %s

DELETE FROM classes WHERE class_id = %s

DELETE FROM guilds WHERE guild_id = %s

DELETE FROM spells WHERE spell_id = %s

--Search/Filter Queries
SELECT first_name, last_name, strength, dexterity, endurance, intelligence, char_id FROM characters WHERE first_name = %s % (firstName)

SELECT class_name, stat_bonus_name, stat_bonus, class_id FROM classes WHERE class_name = %s % (className)

SELECT guild_name, guild_description, guild_id FROM guilds WHERE guild_name = %s % (guildName)

SELECT spell_name, spell_description, spell_level, spell_id FROM spells WHERE spell_name = %s % (spellName)





















