"""Extracteur des contrats fournis par automaton.

Exécuté DANS l'environnement d'automaton (cwd = son workspace), par
scripts/extract-contracts :

    uv run --frozen python <home>/scripts/extractors/automaton_contracts.py

N'importe que le code d'automaton et pydantic, et écrit sur stdout un objet
JSON { chemin sous contracts/ : document }. La mise en YAML et l'écriture
sont faites côté home repo.
"""

import json

from pydantic import TypeAdapter

from bloodbowl.api.main import app
from bloodbowl.commands import GameCommand
from bloodbowl.facts import GameFact


def schema(tp: object, title: str) -> dict[str, object]:
    s = TypeAdapter(tp).json_schema(ref_template="#/$defs/{model}")
    return {"$schema": "https://json-schema.org/draft/2020-12/schema", "title": title, **s}


print(
    json.dumps(
        {
            "api/automaton/openapi.yaml": app.openapi(),
            "events/match/facts.schema.yaml": schema(GameFact, "GameFact"),
            "events/match/commands.schema.yaml": schema(GameCommand, "GameCommand"),
        }
    )
)
