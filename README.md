# AL-MIZAN — traducteur multimédia (lot scellé)

Lot vérifiable produit par le dossier AL-MIZAN / ASTRO-Q°ODE à partir de la vidéo
« L'IA vient-elle de tuer les mathématiques ? » (Numerama, `-XKP4WKXUpI`, 1 950 s, 16 chapitres).

Ce dépôt public existe pour qu'un pair puisse **recalculer** la preuve au lieu de la croire :
il contient les entrées, les deux scripts qui produisent les sorties, les sorties elles-mêmes
et le manifeste SHA-256 qui les lie.

## Vérifier en une commande

```bash
git clone https://github.com/Loulbak78920/AL-MIZAN-TRADUCTEUR-MULTIMEDIA.git
cd AL-MIZAN-TRADUCTEUR-MULTIMEDIA
python verifier.py
```

Attendu : une ligne `OK` par fichier, puis

```
VERDICT           : INTEGRE
```

La racine recalculée doit égaler `racine_merkle_sha256` du manifeste. Le script n'a aucune
dépendance : bibliothèque standard Python seulement.

## Ce que le lot contient

| Chemin | Rôle |
|---|---|
| `donnees/source_video_-XKP4WKXUpI.json` | fiche source scellée (métadonnées, 16 chapitres, transcript absent) |
| `oeuvre_universelle/traducteur_multimedia.py` | calcul : trames 12D, sept équations, trajectoire bornée, dix contrôles |
| `oeuvre_universelle/generer_page_traducteur_multimedia.py` | rendu trilingue, JSON public, manifeste |
| `web_cloud/traducteur_multimedia{,_en,_ar}.html` | pages FR / EN / AR telles que servies |
| `web_cloud/traducteur_multimedia_resultats.json` | résultat complet (équations, chapitres, trajectoire, sceau) |
| `resultats/oeuvre_universelle/traducteur_multimedia.json` | même contenu, copie de travail |
| `PREUVES/traducteur_multimedia_2026-10-29/manifeste_sha256.json` | 8 empreintes, racine Merkle, sceau du noyau |

Pages en ligne : <https://www.al-mizan.world/traducteur-multimedia>
(et `/en`, `/ar`, `/traducteur-multimedia.json`).

## Ce que ce lot prouve — et ce qu'il ne prouve pas

Prouvé par recalcul :

- l'intégrité et l'ordre des huit fichiers (SHA-256 + racine Merkle) ;
- la reproductibilité : rejouer `generer_page_traducteur_multimedia.py` régénère les mêmes
  pages, le même JSON et le même sceau sur la même entrée ;
- les bornes du calcul : 10/10 contrôles, ignorance finale `0,124126` au-dessus du plancher
  doctrinal `0,122`, complétude `0,875874` — **jamais 100 %** (`completude_parfaite_atteinte: false`).

Non prouvé, et revendiqué comme tel :

- **aucune date légalement opposable** : `preuve_date_legale: false`. Pour une date opposable,
  ancrer la racine Merkle chez un tiers (OpenTimestamps, dépôt horodaté, DOI résolvable) ;
- **aucune transcription ni traduction de la parole** : la vidéo ne renvoie aucun sous-titre
  (0 octet sur `json3`, `srv3`, `xml`). Les titres restent en français, langue de la source ;
- **aucune équation attribuée à la vidéo** : les sept équations viennent du dossier AL-MIZAN et
  sont appliquées à des mesures de chapitres ;
- le DOI déclaré `10.5281/zenodo.23554838` renvoyait 404 (doi.org, handle.net, DataCite) à la
  vérification du 2026-10-29 ; il n'est pas présenté comme preuve.

## Auteur et licence

M. Ahmed EL BAHLOUL (IMAM8MAHDI) — auteur du modèle AL-MIZAN / ASTRO-Q°ODE.
Licence : GPL-3.0-only OR AGPL-3.0-only (voir `LICENSE`).