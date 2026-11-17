# Initiatives transverses

Une initiative est ici quand elle touche **plus d'un composant ou un contrat**.
Une évolution interne à un composant vit dans le kanban de ce composant.

Une initiative = un répertoire `initiatives/<id>/`, où `<id>` vaut
`I<nn>-<slug>` (ex. `I01-relais-des-faits`). Il porte, selon les besoins :

| Fichier | Contenu |
|---|---|
| `initiative.md` | objectif, exigences numérotées, statut, découpage (obligatoire) |
| `maquettes/` | maquettes d'écran |
| `event-model.md` | commandes, faits, demandes et vues, dans l'ordre du parcours |
| `contrats.md` | les modifications de contrat attendues, avant code |

Le statut est dans l'en-tête d'`initiative.md` :
`cadrage → contrats → réalisation → intégration → livrée` (ou `abandonnée`).
À partir de `réalisation`, l'initiative a son manifeste candidat
`manifests/candidates/<id>.yaml`. Elle est `livrée` à la promotion.

Modèle : [`_modele/initiative.md`](_modele/initiative.md).
