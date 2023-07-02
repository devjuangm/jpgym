# jpgym
Proyecto de aprendizaje para un gym.


## COMO HACER COMMIT A GITHUB
1. Abrir una ventana de terminal en vscode
2. Escribir en la terminal 

```console
git status
```
El resultado de ejecutar git status es: 
```console
ubuntu@DESKTOP-RD2D6DN:~/proyectos/jpgym$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   app.py
``` 
3. Para agregar el archivo app.py a los cambios de github se debe ejecutar el siguiente comando
```console
git add .
git status
```
el resultado de correr este codigo es:
```console
ubuntu@DESKTOP-RD2D6DN:~/proyectos/jpgym$ git add .
ubuntu@DESKTOP-RD2D6DN:~/proyectos/jpgym$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
        new file:   app.py
```
