/* INSERT VALUES INTO TABLES */
INSERT INTO characters (:first_name, :last_name, :strength, :dexterity, :endurance, :intelligence)
VALUES ("Grey", "Skull", 12, 15, 13, 8),
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
SET strength = 16
WHERE char_id = 1;

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
WHERE last_name = "Enyn";

DELETE FROM classes
WHERE class_id = 3;

DELETE FROM spells
WHERE spell_level = "Level 2";

/* added this one - Jess */
DELETE FROM guilds
WHERE guild_id = 1;