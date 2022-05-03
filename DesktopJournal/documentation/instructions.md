# Instructions

Download the latest release from the releases on the right.

## Configure

Run `poetry run python3 init_database.py` to initialize the database for the project.

## Starting the program

Download dependencies with command
```poetry install```

Now start program with command
```poetry run invoke start```

## Adding new note 
![newnote](https://github.com/rikubrandt/ot-tehtavat/blob/main/DesktopJournal/documentation/pictures/adding_note.png)

Add new note by typing text to the textfield and pressing Add Note button.
Program automatically collects all tags that are specified with #-sign.


## Search by tag
![searchtag](https://github.com/rikubrandt/ot-tehtavat/blob/main/DesktopJournal/documentation/pictures/search_tag.png)
You can search notes based on tag by typing the wanted tag with the #-sign to the textfield and pressing search-button.
Program shows all notes that have the tag.

You can go back to the normal view by clearing the textfield and pressing search again.

## Delete note
![Architecture](https://github.com/rikubrandt/ot-tehtavat/blob/main/DesktopJournal/documentation/pictures/delete_note.png)

Delete note by highlighting the wanted note and pressing the delete selected button.