# Initiatives du projet bbtrainer

Toute évolution du produit naît ici, même si elle ne touche qu'un dépôt
(modèle multi-dépôts de la software factory, `spec/multi-depots/` de wedge-factory).
Quatre niveaux : **initiative projet** `I1` → **epic projet** `I1-E1` → **epic repo**
`I1-E1-AU` (sa part dans un dépôt ; `AU`, `TB`, `BT` : codes courts des dépôts) →
**ticket repo** `I1-E1-AU-T3`.

Le dossier où se trouve une initiative est sa colonne :

| Colonne | Ce qui s'y produit | Pour passer |
|---|---|---|
| `1-backlog/` | une idée, avec son origine ; préfixe de priorité (`01-I2-…`) | priorité |
| `2-grilling/` | besoins numérotés `I<n>-B<k>` (`grilling.md`) | validation humaine |
| `3-maquettes/` | écrans `I<n>-M<k>` | validation humaine |
| `4-contrats/` | cibles des contrats touchés, avant tout code (`contrats.md`, `contrats/`) | validation humaine |
| `5-epics/` | epics projet, chacun partagé en epics repo (un dossier `I<n>-E<k>-…/epic.md`) | validation humaine |
| `6-depots/` | les epics repo sont réalisés dans les dépôts, puis intégrés | promotion validée |
| `7-livree/` | archive, avec la baseline promue | — |
| `8-abandonnee/` | archive | — |

`initiative.md` porte son origine, écrite une fois :

```yaml
origine:
  type: idee | report | remontee | reprise
  par: humain | chef d'usine
  le: 2026-11-17
  source: automaton:A5        # report : I0-B5 ; remontee : I0-E1-AU-T4 ; reprise : <dépôt>:<id>
```

Modèle : [`_modele/initiative.md`](_modele/initiative.md).
