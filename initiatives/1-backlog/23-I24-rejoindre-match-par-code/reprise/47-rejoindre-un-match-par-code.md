# 47 — Rejoindre un match par code

## Objectif

À l'accueil, « REJOINDRE », taper son code, et se retrouver à sa place — sans
connaître ni le `game_id` ni son `coach_id`.

## La décision

**Un code court par coach**, délivré par automaton à la création du match et
affiché par bloodbowlclub.com. Pas d'identifiant à manipuler, pas de lien à
installer : le plus simple à ce stade. Le lien `https` vers une page du site, le
schéma `bbtrainer://` et la liste « Mes matchs » des coachs connectés viendront
s'y brancher sans le défaire.

Le code dit **une place**, pas seulement un match : il porte aussi le droit d'y
jouer. C'est ce qui ferme la brèche actuelle, où connaître le `game_id` et le
`coach_id` suffit à ouvrir le canal d'un autre.

## Le contenu

- Un champ de saisie derrière « REJOINDRE », tolérant à la casse et au tiret :
  `k7p4qx` vaut `K7P-4QX`. Un message clair pour un code inconnu, expiré, ou un
  serveur absent.
- La résolution du code auprès d'automaton : le `game_id`, le `coach_id` et le
  jeton de place.
- L'ouverture du canal avec ce jeton : les `@export` de la carte 46 laissent la
  place au code.

## Dépend de

Dépend de : 46-rejoindre-un-match-d-automaton

- la carte 46 ;
- l'initiative A29 d'automaton, « Rejoindre un match par code », pour la route
  de résolution et le jeton de place. Le format du code — 6 caractères en base 32
  de Crockford — y sera tranché.

Les matchs d'exhibition (initiative A30, `POST /games/exhibition`) passent par le
même code : rien de plus à faire ici.

## Terminé quand

Un code délivré par automaton amène le client à sa place ; un code faux est
refusé avec un message clair. Couvert par des tests sur le modèle de la
carte 30 : serveur absent, code refusé, code accepté.
