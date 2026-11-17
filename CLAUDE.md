# CLAUDE.md — home repo du système bbTrainer

## Rôle du repo

Ce dépôt ne contient **aucun code de composant**. Il décrit le système formé
par plusieurs dépôts et garde ce qui n'appartient à aucun d'eux :

- **qui** compose le système et de quoi chacun répond (`system/components.yaml`) ;
- **qui dépend de qui, via quel contrat** (`system/relations.yaml`) ;
- **les contrats** entre composants (`contracts/`) ;
- **quelles versions marchent ensemble** (`manifests/current.yaml`), et celles
  qu'une initiative propose (`manifests/candidates/`) ;
- **les initiatives transverses** (`initiatives/`) et les **décisions
  transverses** (`decisions/`).

Les composants, leurs dépôts voisins (`../<composant>`) :

| Composant | Rôle | Kanban propre |
|---|---|---|
| `automaton` | serveur de règles d'un match, seul détenteur du journal | `bloodbowl/specs/` |
| `bloodbowltrainer` | bbTrainer, le client de jeu Godot d'un coach | `specs/` |
| `bb-testbackend` | doublure d'automaton sur le canal du coach | `kanban/` |
| `kreek-references` | règles de référence, lues par automaton | — |
| `management-system` | externe (bloodbowlclub.com) : crée les matchs, détient les équipes | — |

Chaque composant garde son `CLAUDE.md`, ses règles et son kanban : ils
s'appliquent quand on travaille dans ce composant. Ce fichier ne régit que
le niveau système.

## L'ordre du flux

Une évolution qui touche **plus d'un composant, ou un contrat**, suit cet ordre.
Une évolution interne à un composant ne passe pas par ici.

1. **Initiative** — `initiatives/<id>/` : exigences, maquettes, event model,
   découpage par composant (modèle : `initiatives/_modele/`). Skill
   `initiative-systeme`.
2. **Contrats et relations d'abord** — la modification de contrat est
   écrite et validée **avant** tout code : contrat écrit à la main modifié
   ici ; contrat généré décrit dans l'initiative (il sera régénéré). Une
   nouvelle dépendance s'ajoute à `system/relations.yaml`. Un choix
   transverse structurant donne un ADR dans `decisions/`.
3. **Découpage dans les composants** — chaque part devient des tickets dans
   le kanban **du composant**, selon ses propres règles. Le home repo ne
   porte pas de tickets.
4. **Manifeste candidat** — `manifests/candidates/<id>.yaml` fixe les SHA des
   composants livrés pour l'initiative (les autres héritent de la baseline).
5. **Intégration** — `uv run ci/integrate manifests/candidates/<id>.yaml` :
   portes de chaque composant, doublure contre le vrai, dérive des contrats.
6. **Promotion** — sur validation de l'utilisateur, `--promote` : la baseline
   prend les SHA du candidat. Les contrats régénérés et `current.yaml` sont
   commités ensemble.

## Règles

- **Validation humaine** : chaque livrable (initiative, contrat, ADR,
  manifeste, promotion) est présenté et discuté avant d'être écrit ou commité.
- **La baseline ne change que par promotion** : ne jamais éditer les SHA de
  `manifests/current.yaml` à la main.
- **Contrats générés, contrats écrits** (`decisions/0002`) : un fichier qui
  commence par `# GÉNÉRÉ` sort de `scripts/extract-contracts` ; on ne l'édite
  jamais, on change le code du composant. Les autres sont écrits à la main
  et déclarent sur quel SHA ils ont été lus.
- **Toute dépendance est déclarée** : une relation entre composants absente
  de `system/relations.yaml` n'existe pas. Un contrat dans `contracts/` est
  porté par au moins une relation.
- **Les composants se lisent au SHA du manifeste**, dans `workspace/`
  (`make workspace`), jamais dans leur clone de travail quand on raisonne sur
  le système. `workspace/` est jetable et ignoré par git ; on n'y commite rien.
- **Ne jamais modifier un dépôt de composant depuis ici** sans le demander :
  ses fichiers relèvent de ses propres règles.
- `make check` (structure + dérive) passe avant tout commit du home repo.
- Échanger en français, avec le vocabulaire des composants (coach, joueur,
  commande, demande, fait…).
- Ne commiter et ne pousser que sur demande ; sur `main`, créer une branche.

## Outils

| Commande | Effet |
|---|---|
| `make workspace [MANIFEST=…]` | monte `workspace/` aux SHA du manifeste |
| `make status` | ce qui est monté, et à quel SHA |
| `make contracts` | régénère les contrats issus du code, depuis `workspace/` |
| `make check` | validations croisées + dérive (contrats et SHA) |
| `make integrate MANIFEST=…` | intégration complète d'un manifeste |
| `uv run ci/integrate <candidat> --promote` | promotion d'un candidat |
