# Pit

This project is just a bit of fun I made to help with learning Python.

Pit simplifies some git commands into single commands. For example, when checking out a branch and pulling it straight away:
* With git:
```
git checkout develop && git pull
```
* With pit:
```
pit chpl develop
```

Although this project is just a bit of fun, the commands that are currently supported are listed below:
| pit                  | git                                  |
| ---------------------|:------------------------------------:|
| chpl <branch>        | git checkout <branch> && git pull    |
| ch <branch>          | git checkout <branch>                |
| a <files>            | git add <file>                       |
| aac <commit message> | git add . && git commit -m <message> |