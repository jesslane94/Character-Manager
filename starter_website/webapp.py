from flask import Flask, render_template, request, redirect, flash
from db_connector.db_connector import connect_to_database, execute_query

#Create the web application
webapp = Flask(__name__)

#Provide a route where requests on the web application can be addressed
@webapp.route('/')
@webapp.route('/index')

def index():
    return render_template('index.html')

@webapp.route('/viewCharacters')
def viewCharacters():

    db_connection = connect_to_database()
 
    query = "SELECT characters.first_name, characters.last_name, characters.strength, characters.dexterity, characters.endurance, characters.intelligence, guilds.guild_name, classes.class_name, characters.char_id FROM characters LEFT JOIN guilds ON characters.guild_id = guilds.guild_id LEFT JOIN classes ON characters.class_id = classes.class_id"
    result = execute_query(db_connection, query).fetchall()

    return render_template('viewCharacters.html', rows=result)

@webapp.route('/updateCharacter/<int:id>', methods=['POST','GET'])
def updateCharacter(id):
    db_connection = connect_to_database()
    
    if request.method == 'GET':

        character_query = 'SELECT char_id, first_name, last_name, strength, dexterity, endurance, intelligence FROM characters WHERE char_id = %s' % (id)
        character_result = execute_query(db_connection, character_query).fetchone()

        guild_query = 'SELECT guild_id, guild_name FROM guilds'
        guild_result = execute_query(db_connection, guild_query).fetchall()

        class_query = 'SELECT class_id, class_name FROM classes'
        class_result = execute_query(db_connection, class_query).fetchall()

        spell_query = 'SELECT spell_id, spell_name FROM spells'
        spell_result = execute_query(db_connection, spell_query).fetchall()

        remove_spell_query = 'SELECT spells.spell_id, spells.spell_name FROM spells INNER JOIN characters_spells ON spells.spell_id = characters_spells.spell_id INNER JOIN characters ON characters_spells.char_id = characters.char_id WHERE characters.char_id = %s ORDER BY spells.spell_id' % (id)
        remove_spell_result = execute_query(db_connection, remove_spell_query).fetchall()

        if character_result == None:
            return render_template('notFound.html')

        return render_template('updateCharacter.html', character = character_result, guilds = guild_result, classes = class_result, spells = spell_result, removeSpell = remove_spell_result)
        
    elif request.method == 'POST':
        
        if request.form['buttonID'] == 'Update Character':
        
            charID = request.form['char_id']
            firstName = request.form['first_name']
            lastName = request.form['last_name']
            strength = request.form['strength']
            dexterity = request.form['dexterity']
            endurance = request.form['endurance']
            intelligence = request.form['intelligence']
            guildID = request.form['guilds']
            classID = request.form['classes']

            #If character has no guild
            if (guildID == 'noGuild'):
                characterData = (firstName, lastName, strength, dexterity, endurance, intelligence, None, classID, charID)
            
            #If character does want to be inserted into a guild 
            else:
                characterData = (firstName, lastName, strength, dexterity, endurance, intelligence, guildID, classID, charID)
            
            characterQuery = 'UPDATE characters SET first_name = %s, last_name = %s, strength = %s, dexterity  = %s, endurance = %s, intelligence = %s, guild_id = %s, class_id = %s  WHERE char_id = %s'
            execute_query(db_connection, characterQuery, characterData)
            
            return redirect('/viewCharacters')

        elif request.form['buttonID'] == 'Add Spell': 
        
            charID = request.form['char_id']
            spellID = request.form['spells']
            spellQuery = 'INSERT INTO characters_spells (char_id, spell_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE char_id = %s, spell_id = %s'
            spellData = (charID, spellID, charID, spellID)
            execute_query(db_connection, spellQuery, spellData)

            return redirect('/viewCharacters')
        
        elif request.form['buttonID'] == 'Remove Spell': 
         
            charID = request.form['char_id']
            removeSpellID = request.form['removeSpell']
            removeSpellQuery = 'DELETE FROM characters_spells WHERE char_id = %s AND spell_id = %s'
            removeSpellData = (charID, removeSpellID)
            execute_query(db_connection, removeSpellQuery, removeSpellData)

            return redirect('/viewCharacters')


@webapp.route('/addCharacter', methods=['POST','GET'])
def addNewCharacter():

    db_connection = connect_to_database()

    if request.method == 'GET':

        guild_query = 'SELECT guild_id, guild_name FROM guilds'
        guild_result = execute_query(db_connection, guild_query).fetchall()

        class_query = 'SELECT class_id, class_name FROM classes'
        class_result = execute_query(db_connection, class_query).fetchall()

        return render_template('addNewCharacter.html', guilds = guild_result, classes = class_result)

    elif request.method == 'POST':
        
        firstName = request.form.get('firstName', False)
        lastName = request.form.get('lastName', False)
        strength = request.form.get('strength', False)
        dexterity = request.form.get('dexterity', False)
        endurance = request.form.get('endurance', False)
        intelligence = request.form.get('intelligence', False)
        guildID = request.form.get('guilds', False)
        classID = request.form.get('classes', False)

        if (guildID == 'noGuild'):
            query = 'INSERT INTO characters (first_name, last_name, strength, dexterity, endurance, intelligence, class_id) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            data = (firstName, lastName, strength, dexterity, endurance, intelligence, classID)

        else:
            query = 'INSERT INTO characters (first_name, last_name, strength, dexterity, endurance, intelligence, guild_id, class_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            data = (firstName, lastName, strength, dexterity, endurance, intelligence, guildID, classID)

        execute_query(db_connection, query, data)

        return redirect('/viewCharacters')

@webapp.route('/deleteCharacter/<int:id>')
def deleteCharacter(id):

    db_connection = connect_to_database()

    query = "DELETE FROM characters WHERE char_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect('viewCharacters')

@webapp.route('/searchCharacters', methods=['GET'])
def displaySearchPage():

    return render_template('searchCharacters.html')

@webapp.route('/search', methods=['POST','GET'])
def search():

    db_connection = connect_to_database()

    if request.method == 'POST':
        firstName = request.form.get('f_name', False)

        query = "SELECT first_name, last_name, strength, dexterity, endurance, intelligence, char_id FROM characters WHERE first_name = '%s'" % (firstName)
        result = execute_query(db_connection, query).fetchall()

        if len(result) == 0:
            return render_template('notFound.html')

        return render_template('results.html', rows=result) 

@webapp.route('/viewClasses')
def viewClasses():

    db_connection = connect_to_database()
    query = "SELECT class_name, stat_bonus_name, stat_bonus, class_id FROM classes"
    result = execute_query(db_connection, query).fetchall()
    return render_template('viewClasses.html', rows=result)

@webapp.route('/addClass', methods=['POST','GET'])
def addClass():

    db_connection = connect_to_database()

    if request.method == 'GET':
        query = 'SELECT class_name, stat_bonus, stat_bonus_name FROM classes'
        result = execute_query(db_connection, query).fetchall()
        return render_template('addClass.html')

    elif request.method == 'POST':
        className = request.form.get('className', False)
        bonusStat = request.form.get('bonusStat', False)
        statBonusName = request.form.get('statBonusName', False)

        query = 'INSERT INTO classes (class_name, stat_bonus, stat_bonus_name) VALUES (%s, %s, %s)'

        db_connection = connect_to_database()
        data = (className, bonusStat, statBonusName)
        execute_query(db_connection, query, data)
        return redirect('/viewClasses')

@webapp.route('/updateClass/<int:id>', methods=['POST','GET'])
def updateClass(id):
    db_connection = connect_to_database()
    
    #display existing data
    if request.method == 'GET':
        class_query = 'SELECT class_id, class_name, stat_bonus, stat_bonus_name FROM classes WHERE class_id = %s' % (id)
        class_result = execute_query(db_connection, class_query).fetchone()

        if class_query == None:
            return render_template('notFound.html')

        return render_template('updateClass.html', classes = class_result)
        
    elif request.method == 'POST':

        class_id = request.form['class_id']
        class_name = request.form['class_name']
        stat_bonus = request.form['stat_bonus']
        stat_bonus_name = request.form['stat_bonus_name']

        query = "UPDATE classes SET class_name = %s, stat_bonus= %s, stat_bonus_name = %s WHERE class_id = %s"
        data = (class_name, stat_bonus, stat_bonus_name, class_id)
        result = execute_query(db_connection, query, data)

        return redirect('/viewClasses')

@webapp.route('/deleteClass/<int:id>')
def deleteClass(id):

    db_connection = connect_to_database()

    query = "DELETE FROM classes WHERE class_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect('/viewClasses')

@webapp.route('/searchClasses', methods=['GET'])
def displayClassSearchPage():

    return render_template('searchClasses.html')

@webapp.route('/searchForClass', methods=['POST','GET'])
def searchClass():

    db_connection = connect_to_database()

    if request.method == 'POST':

        className = request.form.get('c_name', False)
        query = "SELECT class_name, stat_bonus_name, stat_bonus, class_id FROM classes WHERE class_name = '%s'" % (className)
        result = execute_query(db_connection, query).fetchall()
        
        if len(result) == 0:
            return render_template('notFound.html')

        return render_template('resultsClass.html', rows=result) 

@webapp.route('/viewGuilds')
def viewGuilds():

    db_connection = connect_to_database()
    query = "SELECT guild_name, guild_description, guild_id FROM guilds"
    result = execute_query(db_connection, query).fetchall()
    return render_template('viewGuilds.html', rows=result)

@webapp.route('/addGuild', methods=['POST','GET'])
def addGuild():

    db_connection = connect_to_database()

    if request.method == 'GET':

        query = 'SELECT guild_name, guild_description FROM guilds'
        result = execute_query(db_connection, query).fetchall();

        return render_template('addGuild.html')

    elif request.method == 'POST':

        guildName = request.form.get('guildName', False)
        guildDescription = request.form.get('guildDescription', False)

        query = 'INSERT INTO guilds (guild_name, guild_description) VALUES (%s, %s)'

        db_connection = connect_to_database()
        data = (guildName, guildDescription)
        execute_query(db_connection, query, data)

        return redirect('/viewGuilds')

@webapp.route('/updateGuild/<int:id>', methods=['POST','GET'])
def updateGuild(id):
    
    db_connection = connect_to_database()
    
    #display existing data
    if request.method == 'GET':

        guild_query = 'SELECT guild_id, guild_name, guild_description FROM guilds WHERE guild_id = %s' % (id)
        guild_result = execute_query(db_connection, guild_query).fetchone()

        if guild_query == None:
            return render_template('notFound.html')

        return render_template('updateGuild.html', guild = guild_result)
        
    elif request.method == 'POST':

        guild_id = request.form['guild_id']
        guild_name = request.form['guild_name']
        guild_description = request.form['guild_description']
  
        query = "UPDATE guilds SET guild_name= %s, guild_description = %s WHERE guild_id = %s"
        data = (guild_name, guild_description, guild_id)
        result = execute_query(db_connection, query, data)

        return redirect('/viewGuilds')
        

@webapp.route('/deleteGuild/<int:id>')
def deleteGuild(id):
    db_connection = connect_to_database()

    query = "DELETE FROM guilds WHERE guild_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect('viewGuilds')

@webapp.route('/searchGuilds', methods=['GET'])
def displayGuildSearchPage():

    return render_template('searchGuilds.html')

@webapp.route('/searchForGuild', methods=['POST','GET'])
def searchGuild():

    db_connection = connect_to_database()

    if request.method == 'POST':

        guildName = request.form.get('g_name', False)
        query = "SELECT guild_name, guild_description, guild_id FROM guilds WHERE guild_name = '%s'" % (guildName)
        result = execute_query(db_connection, query).fetchall()

        if len(result) == 0:
            return render_template('notFound.html')

        return render_template('resultsGuild.html', rows=result) 

@webapp.route('/viewSpells')
def viewSpells():

    db_connection = connect_to_database()
    query = "SELECT spells.spell_name, spells.spell_description, spells.spell_level, schools.school_name, spells.spell_id FROM spells LEFT JOIN schools ON spells.school_id = schools.school_id"
    result = execute_query(db_connection, query).fetchall();

    return render_template('viewSpells.html', rows=result)

@webapp.route('/addSpell', methods=['POST','GET'])
def addSpell():

    db_connection = connect_to_database()

    if request.method == 'GET':

        school_query = 'SELECT school_id, school_name FROM schools'
        school_result = execute_query(db_connection, school_query).fetchall()

        query = 'SELECT spell_name, spell_level, spell_description, school_id FROM spells'
        result = execute_query(db_connection, query).fetchall()
 
        return render_template('addSpell.html', schools = school_result)

    elif request.method == 'POST':

        spellName = request.form.get('spellName', False)
        spellLevel = request.form.get('spellLevel', False)
        spellDescription = request.form.get('spellDescription', False)
        spellSchool = request.form.get('schools', False)

        if (spellSchool == 'noSchool'):
            query = 'INSERT INTO spells (spell_name, spell_level, spell_description) VALUES (%s, %s, %s)'
            data = (spellName, spellLevel, spellDescription)
            
        else:
            query = 'INSERT INTO spells (spell_name, spell_level, spell_description, school_id) VALUES (%s, %s, %s, %s)'
            data = (spellName, spellLevel, spellDescription, spellSchool)

        execute_query(db_connection, query, data)
        return redirect('/viewSpells')

@webapp.route('/updateSpell/<int:id>', methods=['POST','GET'])
def updateSpell(id):
    db_connection = connect_to_database()
    
    #display existing data
    if request.method == 'GET':

        school_query = 'SELECT school_id, school_name FROM schools'
        school_result = execute_query(db_connection, school_query).fetchall()

        spell_query = 'SELECT spell_id, spell_name, spell_level, spell_description, school_id FROM spells WHERE spell_id = %s' % (id)
        spell_result = execute_query(db_connection, spell_query).fetchone()

        if spell_result == None:
            return render_template('notFound.html')

        return render_template('updateSpell.html', spell = spell_result, spellSchool = school_result)
        
    elif request.method == 'POST':
        
        spell_id = request.form['spell_id']
        spell_name = request.form['spell_name']
        spell_level = request.form['spell_level']
        spell_description = request.form['spell_description']
        school_id = request.form['spellSchool']

        if (school_id == 'noSchool'):
            spellData = (spell_name, spell_level, spell_description, None, spell_id)
        
        else:
            spellData = (spell_name, spell_level, spell_description, school_id, spell_id)

        query = "UPDATE spells SET spell_name= %s, spell_level= %s, spell_description = %s, school_id = %s WHERE spell_id = %s"
        result = execute_query(db_connection, query, spellData)
        return redirect('/viewSpells')

@webapp.route('/deleteSpell/<int:id>')
def deleteSpell(id):
    db_connection = connect_to_database()

    query = "DELETE FROM spells WHERE spell_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect('/viewSpells')

@webapp.route('/searchSpells', methods=['GET'])
def displaySpellSearchPage():
    return render_template('searchSpells.html')

@webapp.route('/searchForSpells', methods=['POST','GET'])
def searchSpell():
    db_connection = connect_to_database()

    if request.method == 'POST':
        
        spellName = request.form.get('s_name', False)
       
        query = "SELECT spell_name, spell_description, spell_level, spell_id FROM spells WHERE spell_name = '%s'" % (spellName)
        result = execute_query(db_connection, query).fetchall()

        if len(result) == 0:
            return render_template('notFound.html')

        return render_template('resultsSpell.html', rows=result)

@webapp.route('/viewSchools')
def viewSchools():
    db_connection = connect_to_database()
    query = "SELECT school_name, school_description, school_id FROM schools"
    result = execute_query(db_connection, query).fetchall()
    return render_template('viewSchools.html', rows=result)

@webapp.route('/addSchool', methods=['POST','GET'])
def addSchool():

    db_connection = connect_to_database()

    if request.method == 'GET':

        query = 'SELECT school_name, school_description FROM schools'
        result = execute_query(db_connection, query).fetchall()

        return render_template('addSchool.html')

    elif request.method == 'POST':

        schoolName = request.form.get('schoolName', False)
        schoolDescription = request.form.get('schoolDescription', False)

        query = 'INSERT INTO schools (school_name, school_description) VALUES (%s, %s)'

        db_connection = connect_to_database()
        data = (schoolName, schoolDescription)
        execute_query(db_connection, query, data)

        return redirect('/viewSchools')


@webapp.route('/updateSchool/<int:id>', methods=['POST','GET'])
def updateSchool(id):
    
    db_connection = connect_to_database()
    
    #display existing data
    if request.method == 'GET':

        school_query = 'SELECT school_id, school_name, school_description FROM schools WHERE school_id = %s' % (id)
        school_result = execute_query(db_connection, school_query).fetchone()

        if school_query == None:
            return render_template('notFound.html')

        return render_template('updateSchool.html', school = school_result)
        
    elif request.method == 'POST':

        school_id = request.form['school_id']
        school_name = request.form['school_name']
        school_description = request.form['school_description']
  
        query = "UPDATE schools SET school_name= %s, school_description = %s WHERE school_id = %s"

        data = (school_name, school_description, school_id)
        result = execute_query(db_connection, query, data)

        return redirect('/viewSchools')

@webapp.route('/deleteSchool/<int:id>')
def deleteSchool(id):
    db_connection = connect_to_database()

    query = "DELETE FROM schools WHERE school_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return redirect('/viewSchools')