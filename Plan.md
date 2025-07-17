# Note App Plan

## Tables
Note
---
| note                                |
| ---                                 |
| id (INT NOT NULL PRIMARY KEY)       |
| name (VARCHAR(128) NOT NULL UNIQUE) |
| owner FOREIGN KEY to user           |
| text (TEXT)                         |
| created\_at (DATE)                  |
| modified\_at (DATE)                 |

Tag
---
| tag                                 |
| ---                                 |
| id (INT NOT NULL PRIMARY KEY)       |
| name (VARCHAR(32) NOT NULL UNIQUE)  |
| description (VARCHAR(128))          |

Note\_Tag
---
| note\_tag                           |
| ---                                 |
| id (INT NOT NULL PRIMARY KEY)       |
| note\_id FOREIGN KEY to note        |
| tag\_id FOREIGN KEY to tag          |

User
---
| user                                |
| ---                                 |
| id (INT NOT NULL PRIMARY KEY)       |
| name (VARCHAR(128) NOT NULL)        |
| email (VARCHAR(128) NOT NULL)       |
| password (VARCHAR(128) NOT NULL)    |
| created\_at (DATE)                  |


## URLs
Read
---
`/notes/`             - (GET) Note list
`/notes/<id>/`        - (GET) View note with id `<id>`

Create
---
`/notes/create/`      - (GET) Show form to create note
`/notes/create/`      - (POST) Submit data to create note

Update
---
`/notes/<id>/edit/`   - (GET) Show form to edit note with id `<id>`
`/notes/<id>/edit/`   - (POST/PUT) Submit data to make changes in note with id `<id>`

Delete
---
`/notes/<id>/delete/` - (GET) Show conformation to delete note with id `<id>`
`/notes/<id>/delete/` - (POST/DELETE) Delete note with id `<id>`

