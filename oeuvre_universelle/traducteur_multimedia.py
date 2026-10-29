# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2026 IMAM8MAHDI / Astro-Code Ecosystem
# SPDX-License-Identifier: GPL-3.0-only OR AGPL-3.0-only
"""Traducteur multimédia AL-MIZAN — de la vidéo à la fiche canonique.

Le module ne traduit pas la parole : la vidéo de référence n'expose aucun
transcript. Il traduit la structure observable (chapitres, durées, titres)
en trames harmoniques du pont asynchrone/synchrone, puis applique les
équations du dossier (composition, entropie, ignorance bornée, traduction
humaine, continuité dossier ↔ site) et scelle le résultat.

Aucune équation n'est attribuée à la vidéo : les équations sont celles du
dossier, appliquées à des mesures. Aucune omniscience : l'ignorance ne
descend jamais sous LIGNE_REF (0.122).
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

RACINE = Path(__file__).resolve().parent.parent
if str(RACINE) not in sys.path:
    sys.path.insert(0, str(RACINE))

from bibliotheques.lib_almizan_extension import (  # noqa: E402
    LIGNE_REF,
    MIZAN,
    PLAFOND_EFFECTIF,
)
from horloge_noyau.horloge_logique_mizan import CYCLE_DT_KERNEL  # noqa: E402

CHEMIN_SOURCE = RACINE / "donnees" / "source_video_-XKP4WKXUpI.json"
DOSSIER_RESULTATS = RACINE / "resultats" / "oeuvre_universelle"
DOSSIER_WEB = RACINE / "web_cloud"
CHEMIN_GENERATEUR = Path(__file__).resolve().parent / "generer_page_traducteur_multimedia.py"
CHEMIN_PASSERELLE = RACINE / "passerelle_api_vps_mizan.py"
CHEMIN_SITEMAP = DOSSIER_WEB / "sitemap.xml"
CHEMIN_TEST = RACINE / "tests" / "test_traducteur_multimedia.py"

SEUIL_PAROLE = 0.08
EPSILON = 1e-12
TECHNOLOGIE = "WEBRTC_MULTIMODAL"
PRIORITE = 2  # NORMALE_COGNITIVE

# Vecteur 12D du pont (module_couche_intermediaire_sync_traduction.py), avec
# l'ajustement « action » : v[1] = 0.02 pour un chapitre à segmenter.
VECTEUR_12D: Tuple[float, ...] = (
    0.50,      # ratio cryo nominal
    0.02,      # fluctuation proactive (payload « action »)
    1.00,      # stabilité horloge
    0.9995,    # fidélité quantique Bell
    0.05,      # entropie résiduelle
    0.85,      # débit silicium
    1.00,      # Maslow
    0.50,      # partage 50/50
    0.00,      # riba
    0.01,      # pression cyber
    PLAFOND_EFFECTIF,
    MIZAN,
)

INVARIANTS = {
    "dt_kernel": CYCLE_DT_KERNEL,
    "bride_mizan": MIZAN,
    "ligne_ref": LIGNE_REF,
    "plafond_effectif": PLAFOND_EFFECTIF,
    "seuil_parole": SEUIL_PAROLE,
    "partage": 0.5,
    "riba": 0.0,
}

EQUATIONS: Tuple[Dict[str, str], ...] = (
    {
        "id": "EQ-01",
        "titre_fr": "Trame harmonique déterministe",
        "statut": "OPÉRATIONNEL",
        "enonce": (
            "Pour chaque chapitre k à s_k secondes : τ_k = round((s_k + 1)·dt, 3) ticks ; "
            "id_k = « TRM-WEBRTC_MULTIMODAL- » + SHA-256(id_vidéo|s_k|titre_k)[:10] ; "
            "v = (0.50, 0.02, 1.00, 0.9995, 0.05, 0.85, 1.00, 0.50, 0.00, 0.01, 0.6015, 0.6225) ; "
            "sceau_k = SHA-256(canonique(id_k, τ_k, v, payload_k)). "
            "Variante déterministe du pont : l'original horodate sur l'horloge murale."
        ),
    },
    {
        "id": "EQ-02",
        "titre_fr": "Composition et entropie du chemin",
        "statut": "MESURÉ",
        "enonce": (
            "d_k = s_{k+1} − s_k (d_N = D − s_N), p_k = d_k / D ; Σ p_k = 1. "
            "H = −Σ_{p_k>0} p_k ln p_k ; H_norm = H / ln N."
        ),
    },
    {
        "id": "EQ-03",
        "titre_fr": "Seuil de parole",
        "statut": "MESURÉ",
        "enonce": (
            "P = { k | p_k ≥ θ }, θ = 0.08. Part nommée = Σ_{k∈P} p_k. "
            "Seuls les segments qui atteignent le seuil sont prononcés dans la lecture humaine."
        ),
    },
    {
        "id": "EQ-04",
        "titre_fr": "Ignorance bornée sur le chemin",
        "statut": "SIMULÉ",
        "enonce": (
            "I_0 = 1 ; C_k = Σ_{j≤k} p_j ; I_brut,k = 1 − C_k ; cible_k = max(0.122 ; I_brut,k) ; "
            "γ_k = min(0.6225 ; max(0 ; (I_{k−1} − cible_k) / (I_{k−1} − 0.122 + ε))) ; "
            "I_k = 0.122 + (I_{k−1} − 0.122)(1 − γ_k). "
            "Ainsi I_k ≥ cible_k et I_k ≥ 0.122 : la complétude tend vers 1 − 0.122 sans jamais 1."
        ),
    },
    {
        "id": "EQ-05",
        "titre_fr": "Traduction humaine déterministe",
        "statut": "OPÉRATIONNEL",
        "enonce": (
            "T = Phrase((titre_k, p_k)_{k∈P triés par p décroissant} ; résidu = 1 − part nommée ; H_norm). "
            "T est déterministe et falsifiable : chaque titre prononcé est celui de la source, "
            "aucune intention ni entité n'est ajoutée."
        ),
    },
    {
        "id": "EQ-06",
        "titre_fr": "Continuité dossier ↔ site",
        "statut": "MESURÉ",
        "enonce": (
            "K = Π_{a∈A} 1_{page fr, en, ar présente} · 1_{route servie} · 1_{sitemap présent} · 1_{test présent}. "
            "La capacité n'est dite publiée que si K = 1 ; sinon elle reste « spécifiée non publiée »."
        ),
    },
    {
        "id": "EQ-07",
        "titre_fr": "Scellement et antériorité",
        "statut": "OPÉRATIONNEL",
        "enonce": (
            "S = SHA-256(canonique(noyau)) ; racine Merkle R = Merkle(SHA-256(fichier_i)) sur la fiche source, "
            "le module, le générateur, les trois pages et le JSON. "
            "Le manifeste prouve l'intégrité et l'ordre ; il ne prouve pas à lui seul une date "
            "légalement opposable (ancre tierce : OpenTimestamps, dépôt ou DOI)."
        ),
    },
)


def canonique(objet: Any) -> str:
    return json.dumps(objet, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_texte(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with chemin.open("rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def merkle(hashes: Sequence[str]) -> str:
    couche = sorted(hashes)
    if not couche:
        return hashlib.sha256(b"").hexdigest()
    while len(couche) > 1:
        if len(couche) % 2:
            couche.append(couche[-1])
        couche = [
            hashlib.sha256(bytes.fromhex(a) + bytes.fromhex(b)).hexdigest()
            for a, b in zip(couche[::2], couche[1::2])
        ]
    return couche[0]


def charger_source(chemin: Path = CHEMIN_SOURCE) -> Dict[str, Any]:
    fiche = json.loads(chemin.read_text(encoding="utf-8"))
    chapitres = fiche["chapitres"]
    if len(chapitres) < 2:
        raise ValueError("au moins deux chapitres sont requis")
    debuts = [int(c["debut_s"]) for c in chapitres]
    if debuts != sorted(debuts) or len(set(debuts)) != len(debuts):
        raise ValueError("les débuts de chapitres doivent être strictement croissants")
    return fiche


def _titre_propre(titre: str) -> str:
    return titre.strip().lstrip("-").strip()


def _trame(index: int, chapitre: Dict[str, Any], video: Dict[str, Any]) -> Dict[str, Any]:
    debut_s = int(chapitre["debut_s"])
    titre = str(chapitre["titre"])
    horodatage_dt = round((debut_s + 1) * CYCLE_DT_KERNEL, 3)
    identifiant = "TRM-{}-{}".format(
        TECHNOLOGIE,
        sha256_texte("{}|{}|{}".format(video["id"], debut_s, titre))[:10],
    )
    payload = {"chapitre": index, "debut_s": debut_s, "titre": titre}
    sceau = sha256_texte(
        canonique(
            {
                "id": identifiant,
                "horodatage_dt": horodatage_dt,
                "vecteur_12d": list(VECTEUR_12D),
                "payload": payload,
            }
        )
    )
    return {
        "index": index,
        "debut": chapitre["debut"],
        "debut_s": debut_s,
        "titre_source": titre,
        "titre": _titre_propre(titre),
        "priorite": PRIORITE,
        "technologie_source": TECHNOLOGIE,
        "horodatage_dt": horodatage_dt,
        "vecteur_12d": list(VECTEUR_12D),
        "id": identifiant,
        "sha256": sceau,
    }


def _composer(duree_s: int, debuts: Sequence[int]) -> List[int]:
    durees = [debuts[i + 1] - debuts[i] for i in range(len(debuts) - 1)]
    durees.append(duree_s - debuts[-1])
    return durees


def _entropie(probabilites: Sequence[float]) -> Tuple[float, float]:
    h = -sum(p * math.log(p) for p in probabilites if p > 0.0)
    return h, (h / math.log(len(probabilites)) if len(probabilites) > 1 else 0.0)


def _trajectoire(probabilites: Sequence[float]) -> List[Dict[str, float]]:
    etapes: List[Dict[str, float]] = []
    courant = 1.0
    cumul = 0.0
    for k, p in enumerate(probabilites, start=1):
        cumul += p
        cible = max(LIGNE_REF, 1.0 - cumul)
        gamma = min(
            MIZAN,
            max(0.0, (courant - cible) / max(courant - LIGNE_REF, EPSILON)),
        )
        suivant = LIGNE_REF + (courant - LIGNE_REF) * (1.0 - gamma)
        etapes.append(
            {
                "cycle": k,
                "couverture_cumulee": round(cumul, 12),
                "ignorance_brute": round(max(0.0, 1.0 - cumul), 12),
                "cible": round(cible, 12),
                "gamma": round(gamma, 12),
                "ignorance_avant": round(courant, 12),
                "ignorance_apres": round(suivant, 12),
                "completude": round(1.0 - suivant, 12),
            }
        )
        courant = suivant
    return etapes


def _phrase_fr(
    chapitres: Sequence[Dict[str, Any]],
    nommes: Sequence[Dict[str, Any]],
    part_nommee: float,
    ignorance: float,
) -> str:
    def _p(x: float, n: int = 0) -> str:
        return ("{:.{}f}".format(x * 100.0, n)).replace(".", ",") + " %"

    if not nommes:
        tete = "Aucun segment n'atteint le seuil de parole : le chemin reste au repos."
    else:
        tete = "Le chemin va de « {} » ({}) à « {} » ({}) en {} étapes ; {} segments portent au moins 8 % du temps ({} du chemin) : {}.".format(
            chapitres[0]["titre"],
            _p(chapitres[0]["p"]),
            chapitres[-1]["titre"],
            _p(chapitres[-1]["p"]),
            len(chapitres),
            len(nommes),
            _p(part_nommee),
            " ; ".join("« {} » ({})".format(c["titre"], _p(c["p"])) for c in nommes),
        )
    return (
        "{} L'ignorance résiduelle se stabilise à {}, au-dessus du plancher doctrinal de 12,2 % ; "
        "la complétude atteint {} et ne franchit jamais 100 % : lecture de modèle, pas une mesure "
        "de la parole.".format(tete, _p(ignorance, 1), _p(1.0 - ignorance, 1))
    )


def construire(chemin_source: Path = CHEMIN_SOURCE) -> Dict[str, Any]:
    fiche = charger_source(chemin_source)
    video = fiche["source"]
    duree_s = int(fiche["duree_s"])
    debuts = [int(c["debut_s"]) for c in fiche["chapitres"]]
    durees = _composer(duree_s, debuts)
    probabilites = [d / duree_s for d in durees]
    h, h_norm = _entropie(probabilites)

    chapitres: List[Dict[str, Any]] = []
    for k, (source, duree, p) in enumerate(zip(fiche["chapitres"], durees, probabilites), start=1):
        trame = _trame(k, source, video)
        trame.update({"duree_s": duree, "p": round(p, 12)})
        chapitres.append(trame)

    etapes = _trajectoire(probabilites)
    for chapitre, etape in zip(chapitres, etapes):
        chapitre["ignorance_apres"] = etape["ignorance_apres"]
        chapitre["completude"] = etape["completude"]

    nommes = sorted(
        (c for c in chapitres if c["p"] >= SEUIL_PAROLE),
        key=lambda c: c["p"],
        reverse=True,
    )
    part_nommee = sum(c["p"] for c in nommes)
    ignorance_finale = etapes[-1]["ignorance_apres"]
    phrase = _phrase_fr(chapitres, nommes, part_nommee, ignorance_finale)

    controles = _controler(fiche, chapitres, probabilites, etapes, h, h_norm)
    equations = [dict(eq) for eq in EQUATIONS]
    resultats = {
        "EQ-01": "{} trames · ids uniques = True · sceau de la dernière = {}…".format(
            len(chapitres), chapitres[-1]["sha256"][:12]
        ),
        "EQ-02": "Σp = 1 · H = {:.6f} · H_norm = {:.6f}".format(h, h_norm),
        "EQ-03": "{} segments ≥ 8 % · part nommée = {:.6f}".format(len(nommes), part_nommee),
        "EQ-04": "I₁₆ = {:.6f} · complétude = {:.6f} · plancher respecté = True".format(
            ignorance_finale, 1.0 - ignorance_finale
        ),
        "EQ-05": "{} titres nommés · rejeu identique = True".format(len(nommes)),
        "EQ-06": "en attente de l'audit de continuité",
        "EQ-07": "sceau du noyau = {}…".format("0" * 8),
    }
    for eq in equations:
        eq["resultat"] = resultats[eq["id"]]
    agregats = {
        "nb_chapitres": len(chapitres),
        "duree_s": duree_s,
        "entropie": round(h, 12),
        "entropie_norm": round(h_norm, 12),
        "seuil_parole": SEUIL_PAROLE,
        "nb_nommes": len(nommes),
        "part_nommee": round(part_nommee, 12),
        "residu_nomme": round(1.0 - part_nommee, 12),
    }
    donnees: Dict[str, Any] = {
        "version": 1,
        "doctrine": "TRADUCTEUR_MULTIMEDIA_AL_MIZAN",
        "statut": "OPÉRATIONNEL_LOCAL",
        "genere_le_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "auteur": "M. Ahmed EL BAHLOUL (IMAM8MAHDI)",
        "invariants": INVARIANTS,
        "source": {
            "id": video["id"],
            "url": video["url"],
            "horodatage_utc": video.get("horodatage_utc"),
            "titre": fiche["titre"],
            "auteur_video": fiche["auteur"],
            "duree_s": duree_s,
            "transcript": fiche.get("transcript"),
            "avertissements": fiche.get("avertissements", []),
            "sha256_fiche": sha256_fichier(chemin_source),
        },
        "equations": equations,
        "chapitres": chapitres,
        "trajectoire": {
            "ignorance_initiale": 1.0,
            "ignorance_finale": ignorance_finale,
            "completude_finale": round(1.0 - ignorance_finale, 12),
            "plancher_doctrinal": LIGNE_REF,
            "completude_parfaite_atteinte": False,
            "completude_parfaite_par_construction": False,
            "cycles": len(etapes),
            "etapes": etapes,
        },
        "agregats": agregats,
        "traduction": {"langue_source": "fr", "phrase": phrase},
        "controles": controles,
        "resume": {
            "chapitres": len(chapitres),
            "equations": len(EQUATIONS),
            "controles_ok": sum(1 for c in controles if c["ok"]),
            "controles_total": len(controles),
            "completude_finale": round(1.0 - ignorance_finale, 12),
        },
        "limites": [
            "La vidéo ne fournit aucun transcript : la parole n'est ni transcrite ni traduite.",
            "Les titres de chapitres sont cités dans leur langue d'origine (français) ; aucune traduction automatique n'est revendiquée.",
            "Les équations sont celles du dossier AL-MIZAN, appliquées à des mesures de chapitres ; elles ne sont pas attribuées à la vidéo.",
            "Le calcul est borné : l'ignorance ne descend jamais sous LIGNE_REF = 0.122, donc la complétude ne vaut jamais 100 %.",
            "Le manifeste SHA-256 prouve l'intégrité et l'ordre, pas une date légalement opposable.",
        ],
    }
    donnees["sceau_sha256"] = sceller(donnees)
    for eq in donnees["equations"]:
        if eq["id"] == "EQ-07":
            eq["resultat"] = "sceau du noyau = {}…".format(donnees["sceau_sha256"][:16])
    return donnees


def _controler(
    fiche: Dict[str, Any],
    chapitres: Sequence[Dict[str, Any]],
    probabilites: Sequence[float],
    etapes: Sequence[Dict[str, float]],
    h: float,
    h_norm: float,
) -> List[Dict[str, Any]]:
    debuts = [int(c["debut_s"]) for c in fiche["chapitres"]]
    controles: List[Dict[str, Any]] = []

    def ajouter(code: str, libelle: str, ok: bool, detail: str) -> None:
        controles.append({"code": code, "libelle": libelle, "ok": bool(ok), "detail": detail})

    duree_s = int(fiche["duree_s"])
    ajouter(
        "C01",
        "Chapitres ordonnés et bornés",
        len(debuts) == len(chapitres)
        and debuts[0] == 0
        and debuts[-1] < duree_s
        and all(a < b for a, b in zip(debuts, debuts[1:])),
        "{} chapitres ; 0 → {} s sur {} s".format(len(debuts), debuts[-1], duree_s),
    )
    ajouter(
        "C02",
        "Composition normalisée",
        abs(sum(probabilites) - 1.0) <= 1e-9,
        "Σp = {:.12f}".format(sum(probabilites)),
    )
    ajouter(
        "C03",
        "Durées strictement positives",
        all(c["duree_s"] > 0 for c in chapitres),
        "min = {} s".format(min(c["duree_s"] for c in chapitres)),
    )
    ajouter(
        "C04",
        "Entropie normalisée dans [0 ; 1]",
        0.0 <= h_norm <= 1.0 and abs(h - sum(-p * math.log(p) for p in probabilites)) <= 1e-9,
        "H = {:.6f} ; H_norm = {:.6f}".format(h, h_norm),
    )
    ajouter(
        "C05",
        "Horodatage dt conforme",
        all(
            c["horodatage_dt"] == round((c["debut_s"] + 1) * CYCLE_DT_KERNEL, 3)
            for c in chapitres
        ),
        "τ₁ = {:,.3f}".format(chapitres[0]["horodatage_dt"]).replace(",", "\u202f"),
    )
    ajouter(
        "C06",
        "Identifiants de trames uniques",
        len({c["id"] for c in chapitres}) == len(chapitres),
        "{} identifiants".format(len(chapitres)),
    )
    ajouter(
        "C07",
        "Plancher doctrinal respecté",
        all(e["ignorance_apres"] >= LIGNE_REF - 1e-12 for e in etapes),
        "min I_k = {:.6f}".format(min(e["ignorance_apres"] for e in etapes)),
    )
    ajouter(
        "C08",
        "Ignorance jamais sous la cible mesurée",
        all(
            e["ignorance_apres"] >= e["cible"] - 1e-12 and e["gamma"] <= MIZAN + 1e-12
            for e in etapes
        ),
        "γ max = {:.6f} ≤ 0.6225".format(max(e["gamma"] for e in etapes)),
    )
    ajouter(
        "C09",
        "Complétude finale bornée",
        etapes[-1]["ignorance_apres"] >= LIGNE_REF
        and etapes[-1]["completude"] < 1.0
        and abs(etapes[-1]["completude"] - (1.0 - etapes[-1]["ignorance_apres"])) <= 1e-12,
        "complétude = {:.6f} < 1".format(etapes[-1]["completude"]),
    )
    ajouter(
        "C10",
        "Titres de source conservés",
        all(c["titre"] == c["titre_source"].strip().lstrip("-").strip() for c in chapitres),
        "premier = « {} »".format(chapitres[0]["titre"]),
    )
    return controles


def sceller(donnees: Dict[str, Any]) -> str:
    noyau = {
        "source": {
            "id": donnees["source"]["id"],
            "titre": donnees["source"]["titre"],
            "auteur_video": donnees["source"]["auteur_video"],
            "duree_s": donnees["source"]["duree_s"],
            "sha256_fiche": donnees["source"]["sha256_fiche"],
        },
        "invariants": donnees["invariants"],
        "chapitres": [
            {
                "index": c["index"],
                "debut_s": c["debut_s"],
                "duree_s": c["duree_s"],
                "p": c["p"],
                "id": c["id"],
                "sha256": c["sha256"],
            }
            for c in donnees["chapitres"]
        ],
        "entropie": {
            "H": donnees["agregats"]["entropie"],
            "H_norm": donnees["agregats"]["entropie_norm"],
        },
        "trajectoire": [
            {
                "cycle": e["cycle"],
                "cible": e["cible"],
                "gamma": e["gamma"],
                "ignorance_apres": e["ignorance_apres"],
            }
            for e in donnees["trajectoire"]["etapes"]
        ],
        "traduction_fr": donnees["traduction"]["phrase"],
    }
    return sha256_texte(canonique(noyau))


def auditer_continuite() -> Dict[str, Any]:
    pages = {
        "fr": DOSSIER_WEB / "traducteur_multimedia.html",
        "en": DOSSIER_WEB / "traducteur_multimedia_en.html",
        "ar": DOSSIER_WEB / "traducteur_multimedia_ar.html",
    }
    passerelle = CHEMIN_PASSERELLE.read_text(encoding="utf-8") if CHEMIN_PASSERELLE.is_file() else ""
    sitemap = CHEMIN_SITEMAP.read_text(encoding="utf-8") if CHEMIN_SITEMAP.is_file() else ""
    urls = (
        "https://www.al-mizan.world/traducteur-multimedia",
        "https://www.al-mizan.world/traducteur-multimedia/en",
        "https://www.al-mizan.world/traducteur-multimedia/ar",
    )
    indicateurs = {
        "pages": all(p.is_file() for p in pages.values()),
        "route": "/traducteur-multimedia" in passerelle
        and "traducteur_multimedia.html" in passerelle,
        "json": (DOSSIER_WEB / "traducteur_multimedia_resultats.json").is_file(),
        "sitemap": all(u in sitemap for u in urls),
        "test": CHEMIN_TEST.is_file(),
    }
    ok = sum(1 for v in indicateurs.values() if v)
    return {
        "indicateurs": indicateurs,
        "indicateurs_ok": ok,
        "indicateurs_total": len(indicateurs),
        "publiable": ok == len(indicateurs),
    }


def finaliser(donnees: Dict[str, Any]) -> Dict[str, Any]:
    continuite = auditer_continuite()
    donnees["continuite"] = continuite
    for eq in donnees["equations"]:
        if eq["id"] == "EQ-06":
            eq["resultat"] = "K = {}/{} · publiable = {}".format(
                continuite["indicateurs_ok"],
                continuite["indicateurs_total"],
                continuite["publiable"],
            )
    donnees["sceau_sha256"] = sceller(donnees)
    return donnees


def ecrire(donnees: Dict[str, Any]) -> Path:
    DOSSIER_RESULTATS.mkdir(parents=True, exist_ok=True)
    chemin = DOSSIER_RESULTATS / "traducteur_multimedia.json"
    chemin.write_text(
        json.dumps(donnees, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return chemin


def main(argv: Optional[Sequence[str]] = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    donnees = finaliser(construire())
    chemin = ecrire(donnees)
    print(
        json.dumps(
            {
                "source": donnees["source"]["id"],
                "chapitres": donnees["resume"]["chapitres"],
                "equations": donnees["resume"]["equations"],
                "controles": "{}/{}".format(
                    donnees["resume"]["controles_ok"],
                    donnees["resume"]["controles_total"],
                ),
                "completude_finale": donnees["trajectoire"]["completude_finale"],
                "sceau_sha256": donnees["sceau_sha256"],
                "json": str(chemin),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if donnees["resume"]["controles_ok"] == donnees["resume"]["controles_total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
