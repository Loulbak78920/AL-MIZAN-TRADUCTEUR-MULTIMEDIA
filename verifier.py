#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 IMAM8MAHDI / Astro-Code Ecosystem
# SPDX-License-Identifier: GPL-3.0-only OR AGPL-3.0-only
"""Vérifie l'intégrité du lot publié à partir du manifeste SHA-256.

Usage : python verifier.py [chemin/du/manifeste_sha256.json]
Sortie : une ligne par fichier, la racine recalculée, puis un verdict.
Code de retour : 0 si le lot est intègre, 1 sinon.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent
MANIFESTE = RACINE / "PREUVES" / "traducteur_multimedia_2026-10-29" / "manifeste_sha256.json"


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with chemin.open("rb") as flux:
        for bloc in iter(lambda: flux.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def merkle(hashes) -> str:
    couche = sorted(hashes)
    if not couche:
        return ""
    while len(couche) > 1:
        if len(couche) % 2:
            couche.append(couche[-1])
        couche = [
            hashlib.sha256(bytes.fromhex(a) + bytes.fromhex(b)).hexdigest()
            for a, b in zip(couche[::2], couche[1::2])
        ]
    return couche[0]


def main() -> int:
    chemin = Path(sys.argv[1]) if len(sys.argv) > 1 else MANIFESTE
    manifeste = json.loads(chemin.read_text(encoding="utf-8"))

    hashes = []
    ecarts = 0
    for f in manifeste["fichiers"]:
        p = RACINE / f["chemin"]
        if not p.is_file():
            print("ABSENT   {0}".format(f["chemin"]))
            ecarts += 1
            continue
        h = sha256_fichier(p)
        octets = p.stat().st_size
        hashes.append(h)
        if h == f["sha256"] and octets == f["octets"]:
            print("OK       {0}".format(f["chemin"]))
        else:
            print("ECART    {0} sha={1}... octets={2} attendu={3}".format(
                f["chemin"], h[:16], octets, f["octets"]))
            ecarts += 1

    racine = merkle(hashes)
    integre = ecarts == 0 and racine == manifeste["racine_merkle_sha256"]
    print()
    print("racine recalculee :", racine)
    print("racine manifeste  :", manifeste["racine_merkle_sha256"])
    print("sceau du noyau    :", manifeste["sceau_noyau_sha256"])
    print("auteur            :", manifeste["auteur"])
    print("genere_le_utc     :", manifeste["genere_le_utc"])
    print("preuve_integrite  :", bool(manifeste["preuve_integrite"]) and ecarts == 0)
    print("preuve_date_legale:", manifeste["preuve_date_legale"])
    print("VERDICT           :", "INTEGRE" if integre else "NON_CONFORME")
    return 0 if integre else 1


if __name__ == "__main__":
    sys.exit(main())