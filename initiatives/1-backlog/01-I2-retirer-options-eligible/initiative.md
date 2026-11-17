---
id: I2
title: Retirer options.eligible des demandes
origine:
  type: idee
  par: humain
  le: 2026-11-17
  source: automaton:A31
---

# I2 — Retirer options.eligible des demandes

A31 d'automaton (« Joueurs éligibles dans la demande ») a été jugée inutile le 2026-11-17 et
close avec 4 tickets livrés et 3 abandonnés. Ce qui est livré publie `options.eligible` dans
trois demandes du canal du coach :

- `eligible_players` : module `bloodbowl/steps/eligible.py` ;
- `high_kick_eligible`, `kick_off_landing_eligible`, `quick_snap_eligible`.

Décision : **retirer** `eligible`. Ce que ça touche :

- **automaton** : le module et les trois étapes ; les tests ;
- **le contrat du canal** (`contracts/events/match/coach-channel.asyncapi.yaml`) : il ne l'a
  jamais décrit ; rien à retirer, mais la remise à niveau du contrat doit le savoir ;
- **bloodbowltrainer** : les cartes 55 (B8) et 57 (B9) et la note de B7 s'appuient sur la
  « décision du 2026-11-16 : automaton publie `options.eligible` » : à délier ;
- **bb-testbackend** : ne l'a jamais servi ; rien à faire ;
- **la baseline** (`manifests/current.yaml`, automaton `25aefb0`) contient déjà une partie de
  `eligible` : la promotion de cette initiative la remet en cohérence.
