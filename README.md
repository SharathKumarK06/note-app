# Note

Note app in Django

## Dependencies
- Python
- Django
- DRF
- SQLite3

## TODO
- [ ] Add models for
    - [x] Notes
    - [x] Tag
    - [ ] User
- [ ] Add serializer for models
- [ ] Use viewset from drf
- [ ] Use router in urlconf
- [ ] Use UserManager for user table
- [ ] User collaboration (give permission to other user to use one's notes)
- [ ] Add authorization (users and group) and authentication (jwt)

## Planning
Tables
---
```
| note                                |
| ---                                 |
| id (INT NOT NULL PRIMARY KEY)       |
| name (VARCHAR(128) NOT NULL UNIQUE) |
| owner FOREIGN KEY to user           |
| text (TEXT)                         |
| created_at (DATE)                   |
| modified_at (DATE)                  |

| tag                                 |
| ---                                 |
| id (INT NOT NULL PRIMARY KEY)       |
| name (VARCHAR(32) NOT NULL UNIQUE)  |
| description (VARCHAR(128))          |

| note_tag                            |
| ---                                 |
| id (INT NOT NULL PRIMARY KEY)       |
| note_id FOREIGN KEY to note         |
| tag_id FOREIGN KEY to tag           |

| user                                |
| ---                                 |
| id (INT NOT NULL PRIMARY KEY)       |
| name (VARCHAR(128) NOT NULL)        |
| email (VARCHAR(128) NOT NULL)       |
| password (VARCHAR(128) NOT NULL)    |
| created_at (DATE)                   |
```

