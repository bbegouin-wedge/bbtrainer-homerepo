---
name: initiative-systeme
description: Ouvrir, cadrer et mener une initiative transverse du système bbTrainer (plus d'un composant parmi automaton, bloodbowltrainer, bb-testbackend, ou un contrat). À utiliser quand l'utilisateur veut lancer une évolution qui traverse les dépôts, modifier un contrat (canal du coach, POST /games, faits, commandes), ou ajouter une dépendance entre composants.
---

# Mener une initiative transverse

Suivre l'ordre du flux de `CLAUDE.md`. Chaque étape produit un livrable
**présenté et validé avant d'être écrit**.

## 1. Est-ce bien transverse ?

Lire `system/relations.yaml`. Si un seul composant change et qu'aucun
contrat ne bouge, ce n'est pas une initiative système : renvoyer vers le
kanban du composant et s'arrêter.

## 2. Cadrage

- Monter la baseline (`make workspace`) et lire les composants **dans
  `workspace/`**, pas dans leurs clones de travail.
- Choisir l'id : `I<nn>-<slug>`, `nn` = le plus grand existant + 1.
- Proposer `initiatives/<id>/initiative.md` d'après `initiatives/_modele/`.
  Exigences numérotées et vérifiables. Event model si de nouveaux faits,
  commandes ou demandes apparaissent.

## 3. Contrats

Pour chaque contrat touché (`contracts/`) :
- **généré** (`# GÉNÉRÉ` en tête) : décrire le changement dans
  l'initiative ; il sera régénéré depuis le code du composant fournisseur.
- **écrit à la main** : proposer le diff du fichier, le faire valider,
  mettre à jour son SHA de lecture.
- Dire si le changement est **compatible**. Sinon, l'ordre de livraison
  doit le dire (qui livre d'abord, comment la doublure suit).
- Nouvelle dépendance → entrée dans `system/relations.yaml`.
- Choix structurant → ADR dans `decisions/` (numéro suivant).

## 4. Découpage

Une ligne par composant dans l'initiative : ce qu'il fait, et les tickets
**à créer dans son propre kanban, selon ses propres règles** (lire son
`CLAUDE.md`). Ne pas créer ces tickets sans le demander : ils relèvent de
chaque dépôt.

Ordre usuel : contrat → automaton → bb-testbackend (la doublure suit le
vrai, `make check-automaton`) → bloodbowltrainer.

## 5. Candidat

Passer l'initiative en `réalisation` et créer
`manifests/candidates/<id>.yaml` (voir son README). Y reporter les SHA au fil
des fusions. Puis skill `integration`.

`make structure` doit passer après chaque étape.
