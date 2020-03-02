from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
webapp = Flask(__name__)

#provide a route where requests on the web application can be addressed
@webapp.route('/index')
#provide a view (fancy name for a function) which responds to any requests on this route
def index():
    return render_template('index.html')

@webapp.route('/viewCharacters')
def viewCharacters():
    db_connection = connect_to_database()
    query = "SELECT first_name, last_name, strength, dexterity, endurance, intelligence FROM characters"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('viewCharacters.html', rows=result)

@webapp.route('/updateCharacter/<int:id>', methods=['POST','GET'])
def updateCharacter(id):
    db_connection = connect_to_database()
    
    #display existing data
    if request.method == 'GET':
        character_query = 'SELECT first_name, last_name, strength, dexterity, endurance, intelligence FROM characters WHERE char_id = %s' % (id)
        character_result = execute_query(db_connection, character_query).fetchone()

        if character_result == None:
            return "No such character found!"

        return render_template('updateCharacter.html', person = character_result)
        
    elif request.method == 'POST':
        print("Update characters!");
        char_id = request.form['char_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        strength = request.form['strength']
        dexterity = request.form['dexterity']
        endurance = request.form['endurance']
        intelligence = request.form['intelligence']

        print(request.form);

        query = "UPDATE characters SET first_name = %s, last_name = %s, strength = %s, dexterity  = %s, endurance = %s, intelligence = %s  WHERE char_id = %s"
        data = (first_name, last_name, strength, dexterity, endurance, intelligence, char_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated!");

        return redirect('/viewCharacters')

@webapp.route('/addNewCharacter', methods=['POST','GET'])
def addNewCharacter():

    db_connection = connect_to_database()

    if request.method == 'GET':
        guild_query = 'SELECT guild_id, guild_name FROM guilds'
        guild_result = execute_query(db_connection, guild_query).fetchall();

        print(guild_result)

        class_query = 'SELECT class_id, class_name FROM classes'
        class_result = execute_query(db_connection, class_query).fetchall(); 

        return render_template('addNewCharacter.html', guilds = guild_result, classes = class_result)

    elif request.method == 'POST':
        print ("Add new people!");
        
        firstName = request.form.get('firstName', False)
        lastName = request.form.get('lastName', False)
        strength = request.form.get('strength', False)
        dexterity = request.form.get('dexterity', False)
        endurance = request.form.get('endurance', False)
        intelligence = request.form.get('intelligence', False)
        guildID = request.form.get('guilds', False)
        classID = request.form.get('classes', False)

        query = 'INSERT INTO characters (first_name, last_name, strength, dexterity, endurance, intelligence, guild_id, class_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        data = (firstName, lastName, strength, dexterity, endurance, intelligence, guildID, classID)
        execute_query(db_connection, query, data)

        return ('Character added!')

@webapp.route('/viewClasses')
def viewClasses():
    db_connection = connect_to_database()
    query = "SELECT class_name, stat_bonus_name, stat_bonus FROM classes"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('viewClasses.html', rows=result)

@webapp.route('/addClass', methods=['POST','GET'])
def addClass():

    db_connection = connect_to_database()

    print ("Add new class!");

    if request.method == 'GET':
        query = 'SELECT class_name, stat_bonus, stat_bonus_name FROM classes'
        result = execute_query(db_connection, query).fetchall();
        print (result)

        return render_template('addClass.html')

    elif request.method == 'POST':

        className = request.form.get('className', False)
        bonusStat = request.form.get('bonusStat', False)
        statBonusName = request.form.get('statBonusName', False)

        query = 'INSERT INTO classes (class_name, stat_bonus, stat_bonus_name) VALUES (%s, %s, %s)'

        db_connection = connect_to_database()
        data = (className, bonusStat, statBonusName)
        execute_query(db_connection, query, data)

        return ('Class added!')
    
@webapp.route('/viewGuilds')
def viewGuilds():
    db_connection = connect_to_database()
    query = "SELECT guild_name, guild_description FROM guilds"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('viewGuilds.html', rows=result)

@webapp.route('/addGuild', methods=['POST','GET'])
def addGuild():

    db_connection = connect_to_database()

    print ("Add new guild!");

    if request.method == 'GET':
        query = 'SELECT guild_name, guild_description FROM guilds'
        result = execute_query(db_connection, query).fetchall();
        print (result)

        return render_template('addGuild.html')

    elif request.method == 'POST':

        guildName = request.form.get('guildName', False)
        guildDescription = request.form.get('guildDescription', False)

        query = 'INSERT INTO guilds (guild_name, guild_description) VALUES (%s, %s)'

        db_connection = connect_to_database()
        data = (guildName, guildDescription)
        execute_query(db_connection, query, data)

        return ('Guild added!')

@webapp.route('/viewSpells')
def viewSpells():
    db_connection = connect_to_database()
    query = "SELECT spell_name, spell_description, spell_level FROM spells"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('viewSpells.html', rows=result)

@webapp.route('/addSpell', methods=['POST','GET'])
def addSpell():

    db_connection = connect_to_database()

    print ("Add new spell!");

    if request.method == 'GET':
        query = 'SELECT spell_name, spell_level, spell_description FROM spells'
        result = execute_query(db_connection, query).fetchall();
        print (result)

        return render_template('addSpell.html')

    elif request.method == 'POST':

        spellName = request.form.get('spellName', False)
        spellLevel = request.form.get('spellLevel', False)
        spellDescription = request.form.get('spellDescription', False)

        query = 'INSERT INTO spells (spell_name, spell_level, spell_description) VALUES (%s, %s, %s)'

        db_connection = connect_to_database()
        data = (spellName, spellLevel, spellDescription)
        execute_query(db_connection, query, data)

        return ('Spell added!')

    
    """
    #Populate query
    query = 'INSERT INTO characters (first_name, last_name, strength, dexterity, endurance, intelligence) VALUES (%s, %s, %s, %s, %s, %s)'
    data = (firstName, lastName, strength, dexterity, endurance, intelligence)

    #Connect to the database and submite the query
    db_connection = connect_to_database()
    execute_query(db_connection, query, data) 
    
    if request.method == 'GET':
        query = 'SELECT char_id FROM characters'
        result = execute_query(db_connection, query).fetchall();
        print(result)

        return render_template('addCharacters.html', character = result)

    elif request.method == 'POST':
        print("Add new character!");
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        strength = request.form['strength']
        dexterity = request.form['dexterity']
        endurance = request.form['endurance']
        intelligence = request.form['intelligence']

        query = 'INSERT INTO characters (firstName, lastName, strength, dexterity, endurance,intelligence) VALUES (%s,%s,%s,%s, %s,%s)'
        data = (firstName, lastName, strength, dexterity, endurance,intelligence)
        execute_query(db_connection, query, data)
        return ('Character added!'); """

""" 
@webapp.route('/browse_bsg_people')
#the name of this function is just a cosmetic thing
def browse_people():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT fname, lname, homeworld, age, character_id from bsg_people;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('people_browse.html', rows=result) """

""" @webapp.route('/add_new_people', methods=['POST','GET'])
def add_new_people():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT planet_id, name from bsg_planets'
        result = execute_query(db_connection, quer
        y).fetchall();
        print(result)

        return render_template('people_add_new.html', planets = result)
    elif request.method == 'POST':
        print("Add new people!");
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        query = 'INSERT INTO bsg_people (fname, lname, age, homeworld) VALUES (%s,%s,%s,%s)'
        data = (fname, lname, age, homeworld)
        execute_query(db_connection, query, data)
        return ('Person added!');

@webapp.route('/')
def index():
    return "<p>Are you looking for /db-test or /hello or <a href='/browse_bsg_people'>/browse_bsg_people</a> or /add_new_people or /update_people/id or /delete_people/id </p>"

@webapp.route('/db-test')
def test_database_connection():
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    db_connection = connect_to_database()
    query = "SELECT * from bsg_people;"
    result = execute_query(db_connection, query);
    return render_template('db_test.html', rows=result)

#display update form and process any updates, using the same function
@webapp.route('/update_people/<int:id>', methods=['POST','GET'])
def update_people(id):
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        people_query = 'SELECT character_id, fname, lname, homeworld, age from bsg_people WHERE character_id = %s' % (id)
        people_result = execute_query(db_connection, people_query).fetchone()

        if people_result == None:
            return "No such person found!"

        planets_query = 'SELECT planet_id, name from bsg_planets'
        planets_results = execute_query(db_connection, planets_query).fetchall();

        return render_template('people_update.html', planets = planets_results, person = people_result)
    elif request.method == 'POST':
        print("Update people!");
        character_id = request.form['character_id']
        
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        print(request.form);

        query = "UPDATE bsg_people SET fname = %s, lname = %s, age = %s, homeworld = %s WHERE character_id = %s"
        data = (fname, lname, age, homeworld, character_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated");

        return redirect('/browse_bsg_people')

@webapp.route('/delete_people/<int:id>')
def delete_people(id):
    '''deletes a person with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM bsg_people WHERE character_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return (str(result.rowcount) + "row deleted")
 """