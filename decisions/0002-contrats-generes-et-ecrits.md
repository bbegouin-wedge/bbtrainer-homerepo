# 0002 — Contrats générés depuis le code, enveloppes écrites à la main

- Statut : proposée
- Date : 2026-11-17

## Contexte

Le code d'automaton décrit déjà une grande part de ses contrats : l'API HTTP
est une application FastAPI (OpenAPI), les faits et les commandes sont des
modèles pydantic. Les réécrire à la main ici, c'est créer une deuxième
source de vérité qui divergera. Mais l'enveloppe du canal websocket
(`fact`, `request`, `accepted`, `refused`, `finished`) est construite à la
main dans `bloodbowl/api/channels.py`, sans modèle : rien à générer.

## Décision

Deux sortes de contrats dans `contracts/` :

- **Générés** — `scripts/extract-contracts` lance, dans l'environnement du
  composant monté au SHA du manifeste, l'extracteur déclaré dans
  `system/components.yaml` (`scripts/extractors/`). Le fichier commence par
  `# GÉNÉRÉ` et ne s'édite jamais. Le code du composant est le lieu
  d'écriture ; le home repo en est la copie publiée et revue.
- **Écrits à la main** — l'AsyncAPI du canal du coach. Il référence les
  schémas générés pour le contenu des faits et des commandes, et indique sur
  quel SHA il a été lu.

`scripts/checks/drift --contracts` régénère et compare : un écart fait
échouer l'intégration.

## Conséquences

- Changer un contrat généré, c'est changer le code du composant, puis
  régénérer dans le candidat. Le diff du contrat dans le home repo rend la
  rupture visible à la revue.
- Les consommateurs (bbTrainer, bb-testbackend) ne se génèrent pas depuis
  ces contrats aujourd'hui ; ils pourraient valider leurs trames contre eux.
- Le contrat de `fetch_team` avec le système de gestion reste informel tant
  qu'aucun vrai système n'est branché.
