# Architecture

## User interface
User interface has only one view called mainwindow or Ui_Notes.
Mainwindow calls methods in the NotesService class and shows the given notes accordingly.

## Application logic

Program has one entity called Note, that represents a note object:
![Note](https://github.com/rikubrandt/ot-tehtavat/blob/main/DesktopJournal/documentation/pictures/note.png)

All the actions are performed by NotesService object. 
NotesService class offers all the functions for user interface
For example:
- `create_note`
- `get_notes`
- `get_tags`
- `delete_note`
- `search_by_tag`

NotesService object calls NotesRepository object that is responsible for performing database related queries.

![Architecture](https://github.com/rikubrandt/ot-tehtavat/blob/main/DesktopJournal/documentation/pictures/architecture.png)


## Saving of information
NotesRepository class is responsible for saving and retrieving the information from the sqlite database.

NotesService also has a method called export_notes that can backup the notes to a .txt file.

## Main functions

### Sequence diagram of adding new note
![Sequence](https://github.com/rikubrandt/ot-tehtavat/blob/main/DesktopJournal/documentation/pictures/seq_add_note.png)

### Displaying notes

![ShowingNotes](https://github.com/rikubrandt/ot-tehtavat/blob/main/DesktopJournal/documentation/pictures/showing_notes.png)

### Searching notes by tag
![Sequence](https://github.com/rikubrandt/ot-tehtavat/blob/main/DesktopJournal/documentation/pictures/search_notes_by_tag.png)