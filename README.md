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
| pit                  | git                                | saved keystrokes including spaces |
| ---------------------|------------------------------------|-----------------------------------|
| chpl {branch}        | checkout {branch} && git pull      | 16                                |
| ch {branch}          | checkout {branch}                  | 6                                 |
| a {files}            | add {file}                         | 2                                 |
| aac "{message}"      | add . && git commit -m "{message}" | 19                                |
