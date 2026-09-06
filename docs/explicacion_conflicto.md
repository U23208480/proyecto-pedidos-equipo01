# Explicación del conflicto resuelto

## ¿Por qué ocurrió el conflicto?
Los integrantes del Grupo 1 (Juan y Alberto) creamos ramas independientes a
partir de `develop` (`conflicto/readme-Juan` y `conflicto/readme-Alberto`)
y ambos modificamos la misma línea de la sección "Integrantes" del archivo
`README.md`, cada uno agregando su propia información. Al integrar primero
la rama de Juan en `develop` sin problemas, y luego intentar integrar la
rama de Alberto, Git no pudo combinar automáticamente los cambios porque
ambas ramas modificaron la misma línea del archivo desde un punto de
partida común.

## ¿Qué archivos fueron afectados?
- `README.md` (sección "## Integrantes").

## ¿Cómo fue solucionado?
1. Se ejecutó `git merge conflicto/readme-Alberto`, lo que generó el
   conflicto marcado con `<<<<<<<`, `=======` y `>>>>>>>` en `README.md`.
2. Se analizó el contenido de ambas versiones en conflicto.
3. Se determinó que el contenido correcto era conservar ambas líneas, ya
   que no eran excluyentes sino complementarias (cada una describe a un
   integrante distinto del equipo).
4. Se editó manualmente el archivo `README.md` eliminando las marcas de
   conflicto y dejando ambas líneas de integrantes.
5. Se marcó el archivo como resuelto con `git add README.md`.
6. Se finalizó la integración con
   `git commit -m "fix: resolver conflicto en README.md integrando aportes de ambos integrantes"`.

El commit de resolución quedó registrado en el historial (`abeb776` en el
`git log --oneline --graph --all`), evidenciando el punto exacto donde
ambas ramas convergieron y se resolvió la divergencia.
