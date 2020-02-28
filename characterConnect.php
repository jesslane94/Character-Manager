<?php
    $servername = classmysql.engr.oregonstate.edu
    $username = cs340_kuhnku
    $password = 3321
    $dbname = cs340_kuhnku

    //Create new connection
    $conn = new mysqli($servername, $username, $password, $dbname);

    //Check Connection
    if ($!conn->connect_error) {
        die("Connection failed: ". $ conn->connect_error);
    }

    //Assign html variables to PHP variables
    $firstName = $_POST('firstName');
    $lastName = $_POST('lastName');
    $strength = $_POST('strength');
    $dexterity = $_POST('dexterity');
    $endurance = $_POST('endurance');
    $intelligence = $_POST('intelligence');
    $guild = $_POST('guild');
    $class = $_POST('class');
    $spell = $_POST('spell');




    $sql = "INSERT INTO characters (firstname, lastname, strength, dexterity, endurance, intelligence, guild, class, spell)
    VALUES = ('$firstName', '$lastName', '$strength', '$dexterity', '$endurance', '$intelligence', '$guild', '$class', '$spell' )

    if ($conn->query($sql) === TRUE )
        echo "New character created successfully!" }

    else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    header("refresh: 2; url = "addCharacter.html");

    $conn->close();
?>