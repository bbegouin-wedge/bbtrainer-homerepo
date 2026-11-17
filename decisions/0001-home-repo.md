# 0001 — Un home repo pour le système

- Statut : proposée
- Date : 2026-11-17

## Contexte

bbTrainer est fait de trois dépôts qui évoluent ensemble : `automaton` (le
serveur de règles), `bloodbowltrainer` (le client Godot) et `bb-testbackend`
(la doublure du serveur). Leur lien vit aujourd'hui dans des copies : le
client lit le protocole « sur automaton `7f5cbae` » dans sa propre doc, la
doublure le relit dans la sienne, et rien ne dit quelles versions des trois
ont été vues marcher ensemble. Les règles Kreek sont clonées sans version.

## Décision

Un dépôt dédié, sans code de composant, porte :

- le modèle du système (composants, relations) ;
- les contrats entre composants ;
- des manifestes : la baseline (SHA intégrés) et les candidats par initiative ;
- les initiatives et les décisions transverses ;
- l'outillage pour monter les composants à un manifeste et vérifier la dérive.

Les composants gardent leur autonomie : leur `CLAUDE.md`, leur kanban, leurs
portes. Le home repo ne fait que les appeler.

## Conséquences

- Une évolution transverse a un seul endroit où commencer et un seul endroit
  où dire qu'elle est intégrée.
- La baseline n'avance que par intégration réussie d'un candidat.
- Coût : tenir les relations et les contrats à jour. Les checks de dérive
  sont là pour que l'oubli se voie.
