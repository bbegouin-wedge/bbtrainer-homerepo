# bbtrainer-homerepo

Le home repo du système bbTrainer : ce qui relie `automaton`,
`bloodbowltrainer` et `bb-testbackend`, sans le code d'aucun d'eux.

```
system/components.yaml       composants, dépôts, responsabilités
system/relations.yaml        dépendances déclarées, via quels contrats
manifests/current.yaml       la baseline : les SHA qui marchent ensemble
manifests/candidates/        les SHA proposés par une initiative
contracts/api/automaton/     POST /games, journal (OpenAPI, généré)
contracts/events/match/      canal du coach (AsyncAPI) ; faits et commandes (générés)
initiatives/<id>/            initiatives transverses
decisions/                   ADR transverses
.claude/skills/              skills de niveau système
scripts/workspace            monte workspace/ aux SHA d'un manifeste
scripts/extract-contracts    régénère les contrats depuis le code
scripts/checks/              validations croisées, dérive
ci/                          validation (PR) et intégration d'un manifeste
```

## Démarrer

Prérequis : `uv`, `git`, et les dépôts des composants clonés à côté de
celui-ci (`../automaton`, `../bloodbowltrainer`, `../bb-testbackend`).

```bash
make workspace     # clone chaque composant dans workspace/, au SHA de la baseline
make check         # structure + dérive
make integrate     # portes de chaque composant, doublure contre le vrai, contrats
```

Le flux d'une évolution transverse et les règles : [`CLAUDE.md`](CLAUDE.md).
