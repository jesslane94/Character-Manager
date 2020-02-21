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