/*Insert Values into the Tables*/
INSERT INTO guilds (guild_name, guild_description)
VALUES ("Merchants", "You like? You buy! I give you a good price"),
       ("Mage Guild", "Never trust a mage"),
       ("Dark Brotherhood", "I just want a nightmare'ish looking horse to ride on"),
       ("Cenarion Circle", "Harmonious order that watches over the world's druids and their practices."),
       ("Banking", "They really just want your money.");

INSERT INTO classes (class_name, stat_bonus, stat_bonus_name) 
VALUES ("Rogue", 2, "Dexterity"),
       ("Bard", 2, "Charisma"),
       ("Fighter", 2, "Strength"),
       ("Wizard", 2, "Intelligence"),
       ("Druid", 2, "Intelligence");

INSERT INTO characters (first_name, last_name, strength, dexterity, endurance, intelligence, guild_id, class_id)
VALUES ("Grey", "Skull", 12, 15, 13, 8, 2, 3),
       ("Dryany", "Enyn", 8, 12, 8, 15, 5, 2),
       ("Adriel", "Serielye", 10, 15, 12, 11, 1, 3),
       ("Chald", "Omega", 20, 15, 15, 15, 3, 2); 


INSERT INTO spells (spell_name, spell_level, spell_description) 
VALUES ("Fireball", 2, "Shoots a fireball. Caution: It's hot."),
    ("Healing Touch", 1, "Restores 5-10 HP to Target."), 
    ("Cast Light", 1, "Makes an object you touch glow. Yippee!"),
    ("Polymorph", 3, "Make your enemy into a sheep, frog or a turtle!"),
    ("Magic Missle", 1, "You create three glowing darts of magical force."),
    ("Acid Arrow", 2, "A shimmering green arrow streaks toward a target within range and bursts in a spray of acid"),
    ("Bark Skin", 2, "You touch a willing creature. Until the spell ends, the target's skin has a rough, bark-like appearance");

INSERT INTO characters_spells (char_id, spell_id)
VALUES (1, 2),
       (1, 3),
       (2, 1),
       (2, 2),
       (3, 1),
       (4, 4),
       (4, 6);

