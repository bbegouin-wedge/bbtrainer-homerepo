# 21 — Rebrancher l'arène sur automaton

## Objectif

L'arène cesse de porter des bouts de règles et devient l'écran d'automaton.
Elle montre ce que le serveur raconte et transmet ce que le coach décide. C'est
la couche que `CLAUDE.md` décrit : elle traduit les clics en commandes et les
faits en animations.

Réécrite le 2026-11-14 : elle visait le `Match` du noyau Rust, mis en sommeil
depuis qu'automaton porte les règles.

## Ce que ça déplace

| Aujourd'hui | Devient |
|---|---|
| `arena_phase.gd` décide de ce qui est permis | il lit les `options` de la demande (`request`) qu'automaton adresse au coach |
| `drag_and_drop.gd` déplace l'unité et mute la grille | il envoie une commande, puis l'unité bouge quand le fait revient |
| `movement_range.gd` calcule la portée | il trace ce que le serveur permet (cf. questions) |
| `MatchState` est écrit par l'écran | il devient le miroir des faits reçus |
| les signaux de l'`EventBus` portent l'état | les faits d'automaton portent le récit, l'`EventBus` le diffuse à l'écran |

## La difficulté réelle : le récit

Un seul pas peut produire « esquive tentée, dé jeté, joueur tombé, armure
percée, joueur sonné, revirement ». L'arène réagit aujourd'hui à des signaux
instantanés. Elle devra jouer une **file de faits**, un par un, dans l'ordre,
avec des pauses, et ne rendre la main au coach qu'à la fin de la file.

C'est le vrai travail de cette carte, et il n'a rien à voir avec les règles.

## Ce dont elle dépend

- **La carte 46** : le canal de coach vers automaton.
- **Le relais des faits par automaton** : le ticket `relay_facts_to_coaches`
  de son initiative A3. Sans lui, l'arène n'a rien à animer.
- **Les règles livrées par automaton** (A5 à A17 dans son backlog) : l'arène
  ne peut animer que ce que le serveur sait jouer. La carte se découpera
  probablement action par action, au rythme de ces livraisons.

## Questions ouvertes

- **La portée de mouvement** : automaton expose-t-il les cases atteignables
  dans les `options` de la demande, ou bbTrainer garde-t-il un calcul local,
  à titre d'aide au tracé seulement ? Dans le second cas, l'écran pourrait
  annoncer une case que le serveur refusera.
- **Le refus** : une commande refusée (`refused`, avec son statut et son
  motif) remet l'unité à sa place. Le motif doit-il s'afficher, et où ?
- **Les demandes à choix** : quand automaton demande « quel dé ? » ou
  « relancer ? », quelle interface ? Rien n'existe.
- **Le parcours local** : l'avant-match hors ligne (choix de l'équipe,
  composition) mène aujourd'hui à une arène qui joue sans serveur. Que
  devient-il quand l'arène ne sait plus jouer seule ?
- **Les tests de comportement** : cette carte réécrit le câblage, donc les
  tests qui le couvrent. Les caractériser avant, comme pour la carte 9.

## Terminé quand

- [ ] Contre un serveur automaton, un match se joue à l'écran, du coup d'envoi
  au touchdown, dans la limite de ce qu'automaton sait jouer ;
- [ ] `io/` ne contient plus aucune règle ;
- [ ] les faits s'animent dans l'ordre, un par un ;
- [ ] les demandes se répondent à la souris, et un refus se voit ;
- [ ] `make test-behaviour`, `make check-arch`, `make check-integrity` passent.
