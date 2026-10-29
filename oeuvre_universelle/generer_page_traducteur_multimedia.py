# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2026 IMAM8MAHDI / Astro-Code Ecosystem
# SPDX-License-Identifier: GPL-3.0-only OR AGPL-3.0-only
"""Génère la page trilingue du traducteur multimédia AL-MIZAN.

Entrée  : resultats/oeuvre_universelle/traducteur_multimedia.json
Sorties : web_cloud/traducteur_multimedia{,_en,_ar}.html et
          web_cloud/traducteur_multimedia_resultats.json
"""

from __future__ import annotations

import html
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Sequence

RACINE = Path(__file__).resolve().parent.parent
if str(RACINE) not in sys.path:
    sys.path.insert(0, str(RACINE))
if str(RACINE / "oeuvre_universelle") not in sys.path:
    sys.path.insert(0, str(RACINE / "oeuvre_universelle"))

import traducteur_multimedia as tm  # noqa: E402

WEB = RACINE / "web_cloud"
RESULTATS = RACINE / "resultats" / "oeuvre_universelle"
PREUVES = RACINE.parent / "PREUVES" / "traducteur_multimedia_2026-10-29"

LANGUES = ("fr", "en", "ar")
SITE = "https://www.al-mizan.world"
AUTEUR = "M. Ahmed EL BAHLOUL (IMAM8MAHDI)"
DOI = "10.5281/zenodo.23554838"
DEPOT = "https://github.com/Loulbak78920/AL-MIZAN-TRADUCTEUR-MULTIMEDIA"
VERIF_LIENS_UTC = "2026-10-29T13:40:00Z"
DOI_RESOLU = False
DEPOT_PUBLIC_RESOLU = True
CHEMINS = {
    "fr": "/traducteur-multimedia",
    "en": "/traducteur-multimedia/en",
    "ar": "/traducteur-multimedia/ar",
}
PAGES = {
    "fr": WEB / "traducteur_multimedia.html",
    "en": WEB / "traducteur_multimedia_en.html",
    "ar": WEB / "traducteur_multimedia_ar.html",
}
PUBLICATION = WEB / "preuves_traducteur"
PREUVES_PUBLIEES = (
    ("source.json", RACINE / "donnees" / "source_video_-XKP4WKXUpI.json", "source_video.json"),
    ("traducteur_multimedia.py", Path(tm.__file__), "traducteur_multimedia.py"),
    ("generer_page_traducteur_multimedia.py", Path(__file__), "generer_page_traducteur_multimedia.py"),
)


def _ecrire(chemin: Path, texte: str) -> None:
    """Écrit en LF pour que les octets servis par la passerelle soient ceux scellés."""
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "w", encoding="utf-8", newline="\n") as flux:
        flux.write(texte)

COULEURS = ("#1f5f8b", "#2f7fae", "#4b93bd", "#6fa9c9", "#8bbbd6")

T: Dict[str, Dict[str, Any]] = {
    "fr": {
        "lang": "fr", "dir": "ltr", "locale": "fr_FR",
        "titre": "Traducteur multimédia Al-Mizan — de la vidéo au chemin canonique",
        "description": "Seize chapitres d'une vidéo traduits en trames harmoniques, équations posées, ignorance bornée et sceau SHA-256 vérifiable.",
        "nav": ("Accueil", "Œuvre", "Observateur", "Portefeuille", "Développeurs"),
        "h1": "Traducteur multimédia : de la vidéo au chemin canonique",
        "lead": "Une vidéo entre ; une fiche vérifiable sort. Le traducteur ne traduit pas la parole absente : il traduit la structure observable — seize chapitres, des durées, des titres — en trames du pont asynchrone/synchrone, puis applique les équations du dossier et scelle le résultat.",
        "badge_chapitres": "16 chapitres · 32 min 30 s",
        "badge_controles": "{ok}/{total} contrôles",
        "badge_hon": "complétude {comp} — jamais 100 %",
        "warn_titre": "Ce que ce document ne fait pas.",
        "warn_corps": "Il ne transcrit pas la parole : la vidéo ne renvoie aucun sous-titre (0 octet sur trois formats). Il ne traduit pas les titres en trois langues : ils restent cités en français, langue de la source. L'analyse, elle, est rédigée en français, anglais et arabe. Aucune équation n'est attribuée à la vidéo : ce sont celles du dossier, appliquées à des mesures.",
        "s_source": "La source et ses limites",
        "p_source": "Métadonnées obtenues par oEmbed et par la page publique de la vidéo, chapitres extraits des horodatages de la description. La fiche source est scellée avant tout calcul.",
        "th_meta": "Champ", "th_valeur": "Valeur",
        "m_titre": "Titre", "m_auteur": "Chaîne", "m_duree": "Durée", "m_transcript": "Transcript", "m_sha": "SHA-256 de la fiche",
        "transcript_absent": "absent — 0 octet (json3, srv3, xml)",
        "s_equations": "Les équations, posées puis résolues",
        "p_equations": "Sept équations, toutes issues du dossier. Chaque carte indique son statut : mesuré sur les chapitres, simulé par la doctrine, ou opérationnel comme code exécuté. Les énoncés formels restent en français, langue du dossier.",
        "th_id": "ID", "th_objet": "Objet", "th_formule": "Formule", "th_resultat": "Résultat", "th_statut": "Statut",
        "s_chemin": "Le chemin, du début à la fin",
        "p_chemin": "Chaque segment porte sa part du temps ; la trajectoire d'ignorance est calculée pas à pas, sans jamais franchir le plancher doctrinal.",
        "s_chapitres": "Les seize étapes",
        "th_num": "#", "th_debut": "Début", "th_duree": "Durée", "th_part": "Part", "th_cumul": "Cumul", "th_gamma": "γ", "th_ign": "I_k", "th_comp": "Complétude", "th_trame": "Trame",
        "s_traduction": "La traduction humaine",
        "p_traduction": "Une phrase déterministe, construite uniquement avec les titres de la source et les nombres calculés. Rejouer le module produit exactement la même phrase et le même sceau.",
        "s_difficultes": "Difficultés rencontrées et réponses",
        "p_difficultes": "Chaque difficulté est nommée, puis traitée par une règle vérifiable — jamais contournée par une affirmation.",
        "s_anteriorite": "Sceau et antériorité",
        "p_anteriorite": "Le sceau couvre le noyau canonique ; le manifeste couvre les fichiers : un pair peut vérifier leur intégrité et leur ordre en recalculant la racine. Le dépôt public GitHub est accessible et porte ces artefacts ; le DOI déclaré, lui, ne se résout pas au 29 octobre 2026 (404) et n'est donc pas présenté comme preuve. La date opposable de cette page reste à ancrer chez un tiers.",
        "th_fichier": "Fichier", "th_sha": "SHA-256",
        "an_racine": "Racine Merkle des sources",
        "an_sceau": "Sceau du noyau",
        "an_date": "Horodatage UTC de génération",
        "an_auteur": "Auteur",
        "an_doi": "DOI déclaré (404 au 2026-10-29)",
        "an_depot": "Dépôt public GitHub",
        "an_verif": "Vérification par un pair",
        "an_limite": "Le manifeste prouve l'intégrité et l'ordre des fichiers. Il ne prouve pas à lui seul une date légalement opposable : pour cela, ancrer la racine via OpenTimestamps, un dépôt ou un DOI.",
        "s_repro": "Reproduire et vérifier",
        "p_repro": "Trois commandes suffisent : calcul, rendu, tests. Le JSON public expose les mêmes nombres que cette page.",
        "s_limites": "Limites assumées",
        "actions_json": "Télécharger le JSON",
        "actions_oeuvre": "Retour à l'œuvre",
        "actions_source": "Voir la vidéo source",
        "note_langue": "Titres de chapitres cités en français d'origine ; analyse rédigée en français, anglais et arabe.",
        "pied": "AL-MIZAN × ASTRO-Q°ODE — {auteur}. Page générée depuis le dossier local ; aucune donnée personnelle au-delà du nom public.",
        "statuts": {"OPÉRATIONNEL": "OPÉRATIONNEL", "MESURÉ": "MESURÉ", "SIMULÉ": "SIMULÉ", "SPÉCIFIÉ": "SPÉCIFIÉ"},
        "eq": {
            "EQ-01": ("Trame harmonique déterministe", "Chaque chapitre devient une trame datée sur dt, avec un identifiant et un sceau reproductibles.", "Le pont d'origine horodate sur l'horloge murale ; cette variante fige l'horodatage pour permettre le rejeu."),
            "EQ-02": ("Composition et entropie", "Les durées se répartissent en parts qui somment à 1 ; l'entropie mesure l'égalité de cette répartition.", "H_norm proche de 1 signifie des segments de tailles comparables."),
            "EQ-03": ("Seuil de parole", "Seuls les segments qui atteignent 8 % du temps sont prononcés dans la phrase humaine.", "Le seuil vient du dossier ; il évite de nommer quinze miettes."),
            "EQ-04": ("Ignorance bornée", "La couverture croît avec les chapitres ; l'ignorance descend vers 0,122 sans jamais passer dessous.", "Le plafond γ = 0,6225 ralentit la chute : c'est la bride, pas un défaut."),
            "EQ-05": ("Traduction humaine", "La phrase est une fonction déterministe des titres et des parts ; rien n'est ajouté.", "Rejouer donne la même phrase et le même sceau."),
            "EQ-06": ("Continuité dossier ↔ site", "La capacité n'est publiée que si page, route, JSON, sitemap et test existent ensemble.", "Un seul indicateur manquant et la capacité reste « spécifiée non publiée »."),
            "EQ-07": ("Scellement et antériorité", "Le noyau est scellé ; les fichiers sont listés par empreinte et racine Merkle.", "L'intégrité est prouvée ; la date opposable exige un ancrage tiers."),
        },
        "diffs": (
            ("Transcript absent", "La vidéo renvoie 0 octet sur json3, srv3 et xml : aucune parole n'est accessible. Réponse : ne rien inventer ; calculer sur les chapitres et le dire."),
            ("La vidéo ne contient pas d'équations", "Réponse : les équations sont celles du dossier AL-MIZAN ; elles sont appliquées à des mesures de chapitres et ne sont jamais attribuées à la vidéo."),
            ("« Complétude complète »", "Réponse bornée : la doctrine interdit 100 %. La page affiche la complétude atteinte (87,6 %) et le plancher d'ignorance (12,2 %), avec la preuve par construction."),
            ("Trois langues", "Réponse : l'analyse est rédigée en FR/EN/AR ; les titres restent en français d'origine, faute de traducteur contenu dans le dossier. Aucune traduction automatique n'est revendiquée."),
            ("Publication publique", "Réponse : K = 5/5 (pages FR/EN/AR, route, JSON, sitemap, test). Sans K = 1, la page ne serait pas déployée."),
            ("Antériorité", "Réponse : sceau SHA-256 + racine Merkle + horodatage UTC ; DOI public antérieur pour l'auteur. La date légalement opposable reste à ancrer (OTS, dépôt, DOI)."),
        ),
        "th_cle": "Difficulté", "th_reponse": "Réponse",
    },
    "en": {
        "lang": "en", "dir": "ltr", "locale": "en_GB",
        "titre": "Al-Mizan multimedia translator — from video to canonical path",
        "description": "Sixteen video chapters translated into harmonic frames, equations posed, bounded ignorance and a verifiable SHA-256 seal.",
        "nav": ("Home", "Work", "Observer", "Wallet", "Developers"),
        "h1": "Multimedia translator: from video to canonical path",
        "lead": "A video goes in; a verifiable record comes out. The translator does not translate absent speech: it translates the observable structure — sixteen chapters, durations, titles — into frames of the asynchronous/synchronous bridge, applies the folder's equations, then seals the result.",
        "badge_chapitres": "16 chapters · 32 min 30 s",
        "badge_controles": "{ok}/{total} checks",
        "badge_hon": "completeness {comp} — never 100%",
        "warn_titre": "What this document does not do.",
        "warn_corps": "It does not transcribe speech: the video returns no captions (0 bytes in three formats). It does not translate chapter titles into three languages: they remain quoted in French, the source language. The analysis itself is written in French, English and Arabic. No equation is attributed to the video: they come from the folder and are applied to measurements.",
        "s_source": "The source and its limits",
        "p_source": "Metadata from oEmbed and the public watch page; chapters taken from description timestamps. The source record is sealed before any computation.",
        "th_meta": "Field", "th_valeur": "Value",
        "m_titre": "Title", "m_auteur": "Channel", "m_duree": "Duration", "m_transcript": "Transcript", "m_sha": "Record SHA-256",
        "transcript_absent": "absent — 0 bytes (json3, srv3, xml)",
        "s_equations": "Equations, posed then solved",
        "p_equations": "Seven equations, all from the folder. Each card states its status: measured on chapters, simulated by doctrine, or operational as executed code. Formal statements stay in French, the folder's language.",
        "th_id": "ID", "th_objet": "Object", "th_formule": "Formula", "th_resultat": "Result", "th_statut": "Status",
        "s_chemin": "The path, start to end",
        "p_chemin": "Each segment carries its share of time; the ignorance trajectory is computed step by step, never crossing the doctrinal floor.",
        "s_chapitres": "The sixteen steps",
        "th_num": "#", "th_debut": "Start", "th_duree": "Duration", "th_part": "Share", "th_cumul": "Cumulative", "th_gamma": "γ", "th_ign": "I_k", "th_comp": "Completeness", "th_trame": "Frame",
        "s_traduction": "The human translation",
        "p_traduction": "A deterministic sentence, built only from the source titles and computed numbers. Replaying the module produces exactly the same sentence and the same seal.",
        "s_difficultes": "Difficulties met and answers",
        "p_difficultes": "Each difficulty is named, then handled by a verifiable rule — never bypassed by an assertion.",
        "s_anteriorite": "Seal and anteriority",
        "p_anteriorite": "The seal covers the canonical core; the manifest covers the files: a peer can verify their integrity and order by recomputing the root. The public GitHub repository is reachable and holds these artifacts; the declared DOI does not resolve on 29 October 2026 (404) and is therefore not presented as proof. A legally opposable date for this page still needs a third-party anchor.",
        "th_fichier": "File", "th_sha": "SHA-256",
        "an_racine": "Merkle root of sources",
        "an_sceau": "Core seal",
        "an_date": "UTC generation timestamp",
        "an_auteur": "Author",
        "an_doi": "Declared DOI (404 on 2026-10-29)",
        "an_depot": "Public GitHub repository",
        "an_verif": "Peer verification",
        "an_limite": "The manifest proves file integrity and order. It does not by itself prove a legally opposable date: anchor the root via OpenTimestamps, a repository or a DOI.",
        "s_repro": "Reproduce and verify",
        "p_repro": "Three commands suffice: compute, render, test. The public JSON exposes the same numbers as this page.",
        "s_limites": "Acknowledged limits",
        "actions_json": "Download the JSON",
        "actions_oeuvre": "Back to the work",
        "actions_source": "Watch the source video",
        "note_langue": "Chapter titles quoted in their original French; analysis written in French, English and Arabic.",
        "pied": "AL-MIZAN × ASTRO-Q°ODE — {auteur}. Page generated from the local folder; no personal data beyond the public name.",
        "statuts": {"OPÉRATIONNEL": "OPERATIONAL", "MESURÉ": "MEASURED", "SIMULÉ": "SIMULATED", "SPÉCIFIÉ": "SPECIFIED"},
        "eq": {
            "EQ-01": ("Deterministic harmonic frame", "Each chapter becomes a frame dated on dt, with a reproducible identifier and seal.", "The original bridge stamps wall-clock time; this variant fixes the timestamp so the run can be replayed."),
            "EQ-02": ("Composition and entropy", "Durations split into shares summing to 1; entropy measures how even that split is.", "H_norm near 1 means segments of comparable size."),
            "EQ-03": ("Speech threshold", "Only segments reaching 8% of time are spoken in the human sentence.", "The threshold comes from the folder; it avoids naming fifteen crumbs."),
            "EQ-04": ("Bounded ignorance", "Coverage grows with chapters; ignorance falls towards 0.122 without ever crossing it.", "The cap γ = 0.6225 slows the fall: that is the bridle, not a defect."),
            "EQ-05": ("Human translation", "The sentence is a deterministic function of titles and shares; nothing is added.", "Replaying gives the same sentence and the same seal."),
            "EQ-06": ("Folder ↔ site continuity", "The capability is published only if page, route, JSON, sitemap and test all exist.", "One missing indicator and the capability stays “specified, unpublished”."),
            "EQ-07": ("Sealing and anteriority", "The core is sealed; files are listed by hash and Merkle root.", "Integrity is proven; an opposable date requires a third-party anchor."),
        },
        "diffs": (
            ("Missing transcript", "The video returns 0 bytes on json3, srv3 and xml: no speech is accessible. Answer: invent nothing; compute on chapters and say so."),
            ("The video contains no equations", "Answer: the equations are those of the AL-MIZAN folder; they are applied to chapter measurements and never attributed to the video."),
            ("“Complete completeness”", "Bounded answer: doctrine forbids 100%. The page shows the completeness reached (87.6%) and the ignorance floor (12.2%), proven by construction."),
            ("Three languages", "Answer: the analysis is written in FR/EN/AR; titles remain in original French, since the folder contains no translator. No machine translation is claimed."),
            ("Public deployment", "Answer: K = 5/5 (FR/EN/AR pages, route, JSON, sitemap, test). Without K = 1, the page would not be deployed."),
            ("Anteriority", "Answer: SHA-256 seal + Merkle root + UTC timestamp; an earlier public DOI for the author. A legally opposable date still needs anchoring (OTS, repository, DOI)."),
        ),
        "th_cle": "Difficulty", "th_reponse": "Answer",
    },
    "ar": {
        "lang": "ar", "dir": "rtl", "locale": "ar_MA",
        "titre": "مترجم الوسائط المتعددة الميزاني — من الفيديو إلى المسار القانوني",
        "description": "ستة عشر فصلاً من فيديو تُترجم إلى إطارات توافقية، معادلات مطروحة، جهل محدود وخاتم SHA-256 قابل للتحقق.",
        "nav": ("الرئيسية", "العمل", "المراقب", "المحفظة", "المطورون"),
        "h1": "مترجم الوسائط المتعددة: من الفيديو إلى المسار القانوني",
        "lead": "يدخل فيديو، وتخرج بطاقة قابلة للتحقق. لا يترجم المترجم الكلام الغائب: بل يترجم البنية القابلة للملاحظة — ستة عشر فصلاً ومدداً وعناوين — إلى إطارات جسر التزامن غير المتزامن/المتزامن، ثم يطبّق معادلات الملف ويختم النتيجة.",
        "badge_chapitres": "16 فصلاً · 32 د 30 ث",
        "badge_controles": "{ok}/{total} فحوص",
        "badge_hon": "الاكتمال {comp} — لا يبلغ 100٪ أبداً",
        "warn_titre": "ما لا يفعله هذا المستند.",
        "warn_corps": "لا يفرّغ الكلام: الفيديو لا يعيد أي ترجمة نصية (0 بايت بثلاثة صيغ). لا يترجم عناوين الفصول إلى ثلاث لغات: تبقى مقتبسة بالفرنسية، لغة المصدر. أما التحليل فيُكتب بالفرنسية والإنجليزية والعربية. ولا تُنسب أي معادلة إلى الفيديو: إنها معادلات الملف مطبقة على قياسات.",
        "s_source": "المصدر وحدوده",
        "p_source": "بيانات وصفية من oEmbed ومن صفحة المشاهدة العامة؛ الفصول مأخوذة من الطوابع الزمنية في الوصف. تُختم بطاقة المصدر قبل أي حساب.",
        "th_meta": "الحقل", "th_valeur": "القيمة",
        "m_titre": "العنوان", "m_auteur": "القناة", "m_duree": "المدة", "m_transcript": "النص المنقول", "m_sha": "بصمة البطاقة",
        "transcript_absent": "غائب — 0 بايت (json3، srv3، xml)",
        "s_equations": "المعادلات: طرح ثم حل",
        "p_equations": "سبع معادلات، كلها من الملف. تبيّن كل بطاقة حالتها: مقاسة على الفصول، أو محاكاة بالمذهب، أو تشغيلية كشيفرة منفذة. تبقى الصياغات الرسمية بالفرنسية، لغة الملف.",
        "th_id": "المعرّف", "th_objet": "الموضوع", "th_formule": "الصيغة", "th_resultat": "النتيجة", "th_statut": "الحالة",
        "s_chemin": "المسار من البداية إلى النهاية",
        "p_chemin": "يحمل كل مقطع حصته من الزمن؛ ويُحسب مسار الجهل خطوة بخطوة دون تجاوز الحد الأدنى المذهبي.",
        "s_chapitres": "الخطوات الست عشرة",
        "th_num": "#", "th_debut": "البداية", "th_duree": "المدة", "th_part": "الحصة", "th_cumul": "التراكم", "th_gamma": "γ", "th_ign": "I_k", "th_comp": "الاكتمال", "th_trame": "الإطار",
        "s_traduction": "الترجمة البشرية",
        "p_traduction": "جملة حتمية، مبنية فقط من عناوين المصدر والأرقام المحسوبة. إعادة تشغيل الوحدة تنتج الجملة نفسها والخاتم نفسه.",
        "s_difficultes": "الصعوبات والردود",
        "p_difficultes": "تُسمّى كل صعوبة، ثم تُعالج بقاعدة قابلة للتحقق — لا تُلتفّ عليها بدعوى.",
        "s_anteriorite": "الخاتم والأسبقية",
        "p_anteriorite": "يغطي الخاتم النواة القانونية؛ ويغطي البيان الملفات: يستطيع القرين التحقق من سلامتها وترتيبها بإعادة حساب الجذر. مستودع GitHub العام متاح ويحمل هذه الملفات؛ أما DOI المعلن فلا يُحلّ في 29 أكتوبر 2026 (404)، لذلك لا يُقدَّم كدليل. والتاريخ المعترف به قانوناً لهذه الصفحة يحتاج إلى تثبيت طرف ثالث.",
        "th_fichier": "الملف", "th_sha": "SHA-256",
        "an_racine": "جذر Merkle للمصادر",
        "an_sceau": "خاتم النواة",
        "an_date": "طابع التوليد UTC",
        "an_auteur": "المؤلف",
        "an_doi": "DOI معلن (404 في 2026-10-29)",
        "an_depot": "مستودع GitHub العام",
        "an_verif": "التحقق من قبل القرين",
        "an_limite": "يثبت البيان سلامة الملفات وترتيبها. ولا يثبت بذاته تاريخاً معترفاً به قانوناً: لذلك يُثبَّت الجذر عبر OpenTimestamps أو مستودع أو DOI.",
        "s_repro": "إعادة الإنتاج والتحقق",
        "p_repro": "تكفي ثلاثة أوامر: الحساب، والعرض، والاختبارات. ويعرض JSON العام الأرقام نفسها الواردة في هذه الصفحة.",
        "s_limites": "حدود معترف بها",
        "actions_json": "تنزيل JSON",
        "actions_oeuvre": "العودة إلى العمل",
        "actions_source": "مشاهدة الفيديو المصدر",
        "note_langue": "عناوين الفصول مقتبسة بالفرنسية الأصلية؛ والتحليل مكتوب بالفرنسية والإنجليزية والعربية.",
        "pied": "AL-MIZAN × ASTRO-Q°ODE — {auteur}. صفحة مولّدة من الملف المحلي؛ لا بيانات شخصية تتجاوز الاسم العام.",
        "statuts": {"OPÉRATIONNEL": "تشغيلي", "MESURÉ": "مقاس", "SIMULÉ": "محاكى", "SPÉCIFIÉ": "محدد"},
        "eq": {
            "EQ-01": ("إطار توافقي حتمي", "يصبح كل فصل إطاراً مؤرخاً على dt، بمعرّف وخاتم قابلين لإعادة الإنتاج.", "الجسر الأصلي يؤرخ بساعة الجدار؛ هذا البديل يثبّت الطابع الزمني لتمكين الإعادة."),
            "EQ-02": ("التركيب والإنتروبيا", "تتوزع المدد إلى حصص مجموعها 1؛ والإنتروبيا تقيس تساوي هذا التوزيع.", "قرب H_norm من 1 يعني مقاطع متقاربة الحجم."),
            "EQ-03": ("عتبة الكلام", "لا تُنطق في الجملة البشرية إلا المقاطع التي تبلغ 8٪ من الزمن.", "العتبة من الملف؛ وهي تمنع تسمية خمس عشرة فتاتاً."),
            "EQ-04": ("جهل محدود", "تنمو التغطية مع الفصول؛ وينخفض الجهل نحو 0.122 دون أن يعبره.", "السقف γ = 0.6225 يبطئ الهبوط: إنه اللجام لا عيب."),
            "EQ-05": ("الترجمة البشرية", "الجملة دالة حتمية للعناوين والحصص؛ لا يُضاف شيء.", "الإعادة تعطي الجملة نفسها والخاتم نفسه."),
            "EQ-06": ("استمرارية الملف ↔ الموقع", "لا تُنشر القدرة إلا إذا وُجدت معاً الصفحة والمسار وJSON وخريطة الموقع والاختبار.", "مؤشر واحد ناقص فتبقى القدرة «محددة غير منشورة»."),
            "EQ-07": ("الختم والأسبقية", "تُختم النواة؛ وتُدرج الملفات ببصماتها وجذر Merkle.", "السلامة مثبتة؛ أما التاريخ المعترف به قانوناً فيتطلب تثبيتاً خارجياً."),
        },
        "diffs": (
            ("غياب النص المنقول", "يعيد الفيديو 0 بايت بصيغ json3 وsrv3 وxml: لا كلام متاح. الرد: لا اختلاق؛ الحساب على الفصول والقول بذلك."),
            ("الفيديو لا يحوي معادلات", "الرد: المعادلات هي معادلات ملف AL-MIZAN؛ تُطبّق على قياسات الفصول ولا تُنسب إلى الفيديو أبداً."),
            ("«الاكتمال الكامل»", "رد محدود: المذهب يمنع 100٪. تعرض الصفحة الاكتمال المحقق (87.6٪) وأرضية الجهل (12.2٪)، بدليل بالبناء."),
            ("ثلاث لغات", "الرد: التحليل مكتوب بالفرنسية والإنجليزية والعربية؛ أما العناوين فتبقى بالفرنسية الأصلية لغياب مترجم في الملف. ولا تُدّعى ترجمة آلية."),
            ("النشر العام", "الرد: K = 5/5 (صفحات FR/EN/AR، المسار، JSON، خريطة الموقع، الاختبار). وبدون K = 1 لا تُنشر الصفحة."),
            ("الأسبقية", "الرد: خاتم SHA-256 + جذر Merkle + طابع UTC؛ وDOI عام سابق للمؤلف. ويبقى التاريخ المعترف به قانوناً بحاجة إلى تثبيت (OTS أو مستودع أو DOI)."),
        ),
        "th_cle": "الصعوبة", "th_reponse": "الرد",
    },
}

CSS = """
:root{--encre:#10263a;--bleu:#1f5f8b;--pale:#f5f7fa;--or:#b45309;--gris:#5b6b7a;}
*{box-sizing:border-box}
body{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--encre);
     background:#fbfcfd;line-height:1.62;font-size:17px}
html[dir="rtl"] body{font-family:'Segoe UI',Tahoma,'Traditional Arabic',Arial,sans-serif}
header.site{background:#0f2438;color:#eef4f9;padding:14px 22px;display:flex;flex-wrap:wrap;
     gap:14px;align-items:center;justify-content:space-between;font-family:'Segoe UI',Arial,sans-serif}
header.site a{color:#dce9f4;text-decoration:none;margin-left:16px;font-size:14px}
header.site .marque{font-weight:700;letter-spacing:.06em;font-size:15px}
header.site nav .langues{margin-left:14px;padding-left:12px;border-left:1px solid #34506a}
header.site nav .langues a{margin-left:6px;padding:2px 7px;border:1px solid #34506a;border-radius:5px;font-size:12.5px}
header.site nav .langues a.on{background:#dce9f4;color:#0f2438;border-color:#dce9f4;font-weight:700}
html[dir="rtl"] header.site nav .langues{margin-left:0;padding-left:0;border-left:0;margin-right:14px;
     padding-right:12px;border-right:1px solid #34506a}
main{max-width:1120px;margin:0 auto;padding:30px 22px 60px}
h1{font-size:32px;line-height:1.2;margin:10px 0 6px}
h2{font-size:23px;margin-top:44px;border-bottom:1px solid #d7e0e8;padding-bottom:6px}
h3{font-size:18px;margin:0 0 6px}
p.lead{font-size:19px;color:#33475a}
.badges{margin:14px 0 6px}
.badges span{display:inline-block;font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;
     margin:0 8px 8px 0;padding:4px 10px;border-radius:20px;border:1px solid #cfdbe6;
     background:#eef4f9;color:#1f5f8b}
.badges .or{background:#fdf3e7;border-color:#ecc79a;color:#8a4b06}
.avertissement{margin:18px 0;padding:14px 16px;border-left:4px solid var(--or);
     background:#fdf8f2;font-size:15.5px;color:#4a3a28}
html[dir="rtl"] .avertissement{border-left:0;border-right:4px solid var(--or)}
.tableau{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:14.5px;margin:14px 0}
th,td{text-align:left;padding:9px 10px;border-bottom:1px solid #e2e9ef;vertical-align:top}
html[dir="rtl"] th,html[dir="rtl"] td{text-align:right}
th{font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;text-transform:uppercase;
   letter-spacing:.05em;color:#5b6b7a;background:#f5f7fa}
tbody tr:hover{background:#f8fbfd}
td.id{white-space:nowrap;font-weight:700;color:#0f3d5c}
.num{direction:ltr;unicode-bidi:embed;white-space:nowrap;text-align:left}
.formule{display:block;font-family:Consolas,monospace;font-size:13.5px;color:#1f4e6b;background:#f4f8fb;
     padding:10px 12px;border-radius:6px;overflow-x:auto;direction:ltr;text-align:left}
.grille{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:18px}
.eqcarte{border:1px solid #dde6ed;border-radius:10px;padding:16px 18px;background:#fff}
.eqcarte .entete{display:flex;justify-content:space-between;align-items:center;
     font-family:'Segoe UI',Arial,sans-serif;font-size:12.5px;color:#5b6b7a;margin-bottom:8px}
.eqcarte .pose{font-size:15px;color:#33475a;margin:0 0 10px}
.eqcarte .res{font-size:15px;margin:10px 0 0;padding:8px 10px;background:#f4f8fb;border-radius:6px}
.eqcarte .lecture{font-size:15px;color:#3c4f61;margin:10px 0 0}
.statut{display:inline-block;font-family:'Segoe UI',Arial,sans-serif;font-size:11.5px;
     padding:2px 9px;border-radius:20px;border:1px solid #cfdbe6;background:#eef4f9;color:#1f5f8b}
.statut.o{background:#eaf6ef;border-color:#bfe0cb;color:#1e6b3a}
.statut.s{background:#fdf3e7;border-color:#ecc79a;color:#8a4b06}
.statut.m{background:#f0eefc;border-color:#cfc6f2;color:#4b3a9a}
.parcours{display:flex;height:40px;border:1px solid #d7e0e8;border-radius:6px;overflow:hidden;margin:16px 0}
.parcours .seg{display:flex;align-items:center;justify-content:center;height:100%;
     font-family:'Segoe UI',Arial,sans-serif;font-size:11px;color:#fff;overflow:hidden;white-space:nowrap}
.parcours .seg span{padding:0 3px}
.legende{font-size:13px;color:var(--gris);font-family:'Segoe UI',Arial,sans-serif}
.phrase{margin:16px 0;padding:16px 18px;border-left:4px solid var(--bleu);background:#f4f8fb;font-size:16.5px}
html[dir="rtl"] .phrase{border-left:0;border-right:4px solid var(--bleu)}
.encadre{margin:18px 0;padding:14px 16px;border-left:4px solid var(--bleu);background:#f4f8fb}
html[dir="rtl"] .encadre{border-left:0;border-right:4px solid var(--bleu)}
ul{margin:10px 0 0;padding-left:20px}
html[dir="rtl"] ul{padding-left:0;padding-right:20px}
li{margin:6px 0}
pre{background:#f6f8fa;border:1px solid #d7e0e8;border-radius:8px;padding:14px;overflow-x:auto;font-size:13.5px;direction:ltr;text-align:left}
.actions{margin-top:26px;display:flex;flex-wrap:wrap;gap:10px}
.actions a{font-family:'Segoe UI',Arial,sans-serif;font-size:14px;text-decoration:none;
     padding:9px 16px;border-radius:8px;border:1px solid #1f5f8b;color:#1f5f8b}
.actions a.principal{background:#1f5f8b;color:#fff}
.note-langue{font-size:13.5px;color:#5b6b7a;margin-top:10px}
footer.site{background:#0f2438;color:#c9d9e6;padding:18px 22px;font-size:13.5px;
     font-family:'Segoe UI',Arial,sans-serif;text-align:center}
footer.site a{color:#dce9f4}
@media (max-width:900px){.grille{grid-template-columns:1fr}}
"""


def _ech(valeur: Any) -> str:
    return html.escape(str(valeur), quote=True)


def _nom(x: float, lang: str, n: int = 2) -> str:
    texte = f"{x:.{n}f}"
    return texte.replace(".", ",") if lang in ("fr", "ar") else texte


def _pct(x: float, lang: str, n: int = 1) -> str:
    return _nom(x * 100.0, lang, n) + " %"


def _nav(lang: str) -> str:
    t = T[lang]
    liens = (
        ("/", t["nav"][0]),
        ("/oeuvre-universelle", t["nav"][1]),
        ("/observateur-triniter", t["nav"][2]),
        ("/portefeuille", t["nav"][3]),
        ("/developpeurs", t["nav"][4]),
    )
    corps = "".join(f"<a href='{h}'>{_ech(libelle)}</a>" for h, libelle in liens)
    langues = "".join(
        f"<a class='langue{' on' if code == lang else ''}' href='{CHEMINS[code]}' "
        f"hreflang='{code}' lang='{code}'>{libelle}</a>"
        for code, libelle in (("fr", "FR"), ("en", "EN"), ("ar", "العربية"))
    )
    return (
        "<header class='site'><div class='marque'>AL-MIZAN.WORLD</div><nav>"
        f"{corps}<span class='langues'>{langues}</span></nav></header>"
    )


def _pied(lang: str) -> str:
    return f"<footer class='site'>{T[lang]['pied'].format(auteur=_ech(AUTEUR))}</footer>"


def _classe_statut(statut: str) -> str:
    return {"OPÉRATIONNEL": "o", "SIMULÉ": "s", "MESURÉ": "m"}.get(statut, "")


def _source(donnees: Dict[str, Any], lang: str) -> str:
    t = T[lang]
    s = donnees["source"]
    lignes = (
        (t["m_titre"], _ech(s["titre"])),
        (t["m_auteur"], _ech(s["auteur_video"])),
        (t["m_duree"], f"<span class='num'>{s['duree_s']} s</span>"),
        (t["m_transcript"], _ech(t["transcript_absent"])),
        (
            t["m_sha"],
            f"<span class='num'>{_ech(s['sha256_fiche'][:24])}…</span>",
        ),
    )
    corps = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in lignes)
    return (
        f"<div class='tableau'><table><tbody>{corps}</tbody></table></div>"
        f"<p><a href='{_ech(s['url'])}' rel='noopener'>{_ech(s['url'])}</a></p>"
    )


def _table_equations(donnees: Dict[str, Any], lang: str) -> str:
    t = T[lang]
    lignes = []
    for eq in donnees["equations"]:
        statut = t["statuts"][eq["statut"]]
        resultat = eq.get("resultat", "—")
        lignes.append(
            "<tr>"
            f"<td class='id'><a href='#{eq['id'].lower()}'>{eq['id']}</a></td>"
            f"<td>{_ech(t['eq'][eq['id']][0])}</td>"
            f"<td><span class='formule'>{_ech(eq['enonce'])}</span></td>"
            f"<td>{_ech(resultat)}</td>"
            f"<td><span class='statut {_classe_statut(eq['statut'])}'>{_ech(statut)}</span></td>"
            "</tr>"
        )
    return (
        "<div class='tableau'><table><thead><tr>"
        f"<th>{t['th_id']}</th><th>{t['th_objet']}</th><th>{t['th_formule']}</th>"
        f"<th>{t['th_resultat']}</th><th>{t['th_statut']}</th>"
        "</tr></thead><tbody>" + "".join(lignes) + "</tbody></table></div>"
    )


def _cartes_equations(donnees: Dict[str, Any], lang: str) -> str:
    t = T[lang]
    blocs = []
    for eq in donnees["equations"]:
        titre, pose, lecture = t["eq"][eq["id"]]
        statut = t["statuts"][eq["statut"]]
        resultat = eq.get("resultat", "—")
        blocs.append(
            f"<article class='eqcarte' id='{eq['id'].lower()}'>"
            f"<div class='entete'><span class='id'>{eq['id']}</span>"
            f"<span class='statut {_classe_statut(eq['statut'])}'>{_ech(statut)}</span></div>"
            f"<h3>{_ech(titre)}</h3>"
            f"<p class='pose'>{_ech(pose)}</p>"
            f"<div class='formule'>{_ech(eq['enonce'])}</div>"
            f"<p class='res'><strong>{t['th_resultat']} :</strong> {_ech(resultat)}</p>"
            f"<p class='lecture'>{_ech(lecture)}</p>"
            "</article>"
        )
    return "<div class='grille'>" + "".join(blocs) + "</div>"


def _parcours(donnees: Dict[str, Any], lang: str) -> str:
    segments = []
    for i, chapitre in enumerate(donnees["chapitres"]):
        couleur = COULEURS[i % len(COULEURS)]
        largeur = chapitre["p"] * 100.0
        contenu = ""
        if chapitre["p"] >= tm.SEUIL_PAROLE:
            contenu = f"<span>{_ech(chapitre['debut'])}</span>"
        infobulle = "{} — {} — {}".format(
            chapitre["debut"], chapitre["titre"], _pct(chapitre["p"], lang)
        )
        segments.append(
            f"<div class='seg' style='width:{largeur:.6f}%;background:{couleur}' "
            f"title='{_ech(infobulle)}'>{contenu}</div>"
        )
    return (
        "<div class='parcours'>" + "".join(segments) + "</div>"
        "<p class='legende'>"
        + _ech(
            {
                "fr": "Largeur = part du temps ; seuls les segments ≥ 8 % affichent leur début.",
                "en": "Width = share of time; only segments ≥ 8% show their start.",
                "ar": "العرض = حصة الزمن؛ لا تظهر البداية إلا للمقاطع ≥ 8٪.",
            }[lang]
        )
        + "</p>"
    )


def _table_trajectoire(donnees: Dict[str, Any], lang: str) -> str:
    t = T[lang]
    lignes = []
    for chapitre, etape in zip(donnees["chapitres"], donnees["trajectoire"]["etapes"]):
        lignes.append(
            "<tr>"
            f"<td class='num'>{chapitre['index']}</td>"
            f"<td class='num'>{_ech(chapitre['debut'])}</td>"
            f"<td class='num'>{chapitre['duree_s']} s</td>"
            f"<td class='num'>{_pct(chapitre['p'], lang)}</td>"
            f"<td class='num'>{_pct(etape['couverture_cumulee'], lang)}</td>"
            f"<td class='num'>{_nom(etape['gamma'], lang, 4)}</td>"
            f"<td class='num'>{_nom(etape['ignorance_apres'], lang, 4)}</td>"
            f"<td class='num'>{_pct(etape['completude'], lang)}</td>"
            f"<td class='num'>{_ech(chapitre['id'][-10:])}</td>"
            "</tr>"
        )
    return (
        "<div class='tableau'><table><thead><tr>"
        f"<th>{t['th_num']}</th><th>{t['th_debut']}</th><th>{t['th_duree']}</th>"
        f"<th>{t['th_part']}</th><th>{t['th_cumul']}</th><th>{t['th_gamma']}</th>"
        f"<th>{t['th_ign']}</th><th>{t['th_comp']}</th><th>{t['th_trame']}</th>"
        "</tr></thead><tbody>" + "".join(lignes) + "</tbody></table></div>"
    )


def _phrase(donnees: Dict[str, Any], lang: str) -> str:
    if lang == "fr":
        return donnees["traduction"]["phrase"]
    agregats = donnees["agregats"]
    nommes = [c for c in donnees["chapitres"] if c["p"] >= tm.SEUIL_PAROLE]
    nommes.sort(key=lambda c: c["p"], reverse=True)
    premier = donnees["chapitres"][0]
    dernier = donnees["chapitres"][-1]
    ignorance = donnees["trajectoire"]["ignorance_finale"]
    completude = donnees["trajectoire"]["completude_finale"]
    if lang == "en":
        return (
            "The path runs from “{p}” ({pp}) to “{d}” ({dp}) in {n} steps; {k} segments carry at least "
            "8% of the time ({part} of the path): {liste}. Residual ignorance settles at {ign}, above "
            "the doctrinal floor of 12.2%; completeness reaches {comp} and never crosses 100%: "
            "a model reading, not a measurement of speech."
        ).format(
            p=premier["titre"], pp=_pct(premier["p"], lang, 0),
            d=dernier["titre"], dp=_pct(dernier["p"], lang, 0),
            n=len(donnees["chapitres"]), k=len(nommes),
            part=_pct(agregats["part_nommee"], lang, 0),
            liste="; ".join("“{}” ({})".format(c["titre"], _pct(c["p"], lang, 0)) for c in nommes),
            ign=_pct(ignorance, lang), comp=_pct(completude, lang),
        )
    return (
        "يمتد المسار من «{p}» ({pp}) إلى «{d}» ({dp}) في {n} خطوة؛ وتحمل {k} مقاطع ما لا يقل عن "
        "8٪ من الزمن ({part} من المسار): {liste}. يستقر الجهل المتبقي عند {ign}، فوق الأرضية "
        "المذهبية 12.2٪؛ ويبلغ الاكتمال {comp} ولا يعبر 100٪ أبداً: قراءة نموذج لا قياس كلام."
    ).format(
        p=premier["titre"], pp=_pct(premier["p"], lang, 0),
        d=dernier["titre"], dp=_pct(dernier["p"], lang, 0),
        n=len(donnees["chapitres"]), k=len(nommes),
        part=_pct(agregats["part_nommee"], lang, 0),
        liste="؛ ".join("«{}» ({})".format(c["titre"], _pct(c["p"], lang, 0)) for c in nommes),
        ign=_pct(ignorance, lang), comp=_pct(completude, lang),
    )


def _difficultes(lang: str) -> str:
    t = T[lang]
    lignes = "".join(
        f"<tr><td>{_ech(cle)}</td><td>{_ech(reponse)}</td></tr>"
        for cle, reponse in t["diffs"]
    )
    return (
        f"<div class='tableau'><table><thead><tr><th>{t['th_cle']}</th>"
        f"<th>{t['th_reponse']}</th></tr></thead><tbody>{lignes}</tbody></table></div>"
    )


def _anteriorite(donnees: Dict[str, Any], lang: str) -> str:
    t = T[lang]
    an = donnees.get("anteriorite") or {
        "fichiers": [],
        "racine_merkle": "en attente de scellement",
    }
    lignes = "".join(
        f"<tr><td><span class='num'>{_ech(f['chemin'])}</span></td>"
        f"<td><span class='num'>{_ech(f['sha256'][:32])}…</span></td></tr>"
        for f in an["fichiers"]
    )
    return f"""
<div class='tableau'><table><thead><tr><th>{t['th_fichier']}</th><th>{t['th_sha']}</th></tr></thead>
<tbody>{lignes}</tbody></table></div>
<div class='encadre'>
<p><strong>{t['an_racine']} :</strong> <span class='num'>{_ech(an['racine_merkle'])}</span></p>
<p><strong>{t['an_sceau']} :</strong> <span class='num'>{_ech(donnees['sceau_sha256'])}</span></p>
<p><strong>{t['an_date']} :</strong> <span class='num'>{_ech(donnees['genere_le_utc'])}</span></p>
<p><strong>{t['an_auteur']} :</strong> {_ech(AUTEUR)}</p>
<p><strong>{t['an_doi']} :</strong> <a href='https://doi.org/{DOI}' rel='noopener'>{DOI}</a></p>
<p><strong>{t['an_depot']} :</strong> <a href='{DEPOT}' rel='noopener'>{DEPOT}</a></p>
<p><strong>{t['an_verif']} :</strong>
<a href='/traducteur-multimedia/manifeste.json' rel='noopener'>manifeste_sha256.json</a> ·
<a href='/traducteur-multimedia/source.json' rel='noopener'>source_video_-XKP4WKXUpI.json</a> ·
<a href='/traducteur-multimedia/code/traducteur_multimedia.py' rel='noopener'>traducteur_multimedia.py</a> ·
<a href='/traducteur-multimedia/code/generer_page_traducteur_multimedia.py' rel='noopener'>generer_page_traducteur_multimedia.py</a></p>
</div>
<div class='avertissement'>{_ech(t['an_limite'])}</div>
"""


def _corps(donnees: Dict[str, Any], lang: str) -> str:
    t = T[lang]
    resume = donnees["resume"]
    comp = _pct(donnees["trajectoire"]["completude_finale"], lang)
    valeurs = {"ok": resume["controles_ok"], "total": resume["controles_total"], "comp": comp}
    limites = "".join(f"<li>{_ech(limite)}</li>" for limite in donnees["limites"])
    return f"""
<h1>{_ech(t['h1'])}</h1>
<p class="lead">{_ech(t['lead'])}</p>
<div class="badges">
  <span>{_ech(t['badge_chapitres'])}</span>
  <span>{t['badge_controles'].format(**valeurs)}</span>
  <span class="or">{t['badge_hon'].format(**valeurs)}</span>
</div>
<div class="avertissement"><strong>{_ech(t['warn_titre'])}</strong> {_ech(t['warn_corps'])}</div>

<h2 id="source">{_ech(t['s_source'])}</h2>
<p>{_ech(t['p_source'])}</p>
{_source(donnees, lang)}

<h2 id="equations">{_ech(t['s_equations'])}</h2>
<p>{_ech(t['p_equations'])}</p>
{_table_equations(donnees, lang)}
{_cartes_equations(donnees, lang)}

<h2 id="chemin">{_ech(t['s_chemin'])}</h2>
<p>{_ech(t['p_chemin'])}</p>
{_parcours(donnees, lang)}
<h3 id="chapitres">{_ech(t['s_chapitres'])}</h3>
{_table_trajectoire(donnees, lang)}

<h2 id="traduction">{_ech(t['s_traduction'])}</h2>
<p>{_ech(t['p_traduction'])}</p>
<p class="phrase">{_ech(_phrase(donnees, lang))}</p>

<h2 id="difficultes">{_ech(t['s_difficultes'])}</h2>
<p>{_ech(t['p_difficultes'])}</p>
{_difficultes(lang)}

<h2 id="anteriorite">{_ech(t['s_anteriorite'])}</h2>
<p>{_ech(t['p_anteriorite'])}</p>
{_anteriorite(donnees, lang)}

<h2 id="reproductibilite">{_ech(t['s_repro'])}</h2>
<pre>py -3 oeuvre_universelle/traducteur_multimedia.py
py -3 oeuvre_universelle/generer_page_traducteur_multimedia.py
py -3 -m unittest tests.test_traducteur_multimedia -v</pre>
<p>{_ech(t['p_repro'])}</p>

<h2 id="limites">{_ech(t['s_limites'])}</h2>
<ul>{limites}</ul>

<div class="actions">
  <a class="principal" href="/traducteur-multimedia.json">{_ech(t['actions_json'])}</a>
  <a href="/oeuvre-universelle">{_ech(t['actions_oeuvre'])}</a>
  <a href="{_ech(donnees['source']['url'])}" rel="noopener">{_ech(t['actions_source'])}</a>
</div>
<p class="note-langue">{_ech(t['note_langue'])}</p>
"""


def _html(donnees: Dict[str, Any], lang: str) -> str:
    t = T[lang]
    alternates = "".join(
        f"<link rel='alternate' hreflang='{code}' href='{SITE}{CHEMINS[code]}'>\n"
        for code in LANGUES
    )
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}"{' dir="rtl"' if t['dir'] == 'rtl' else ''}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_ech(t['titre'])}</title>
<meta name="description" content="{_ech(t['description'])}">
<link rel="canonical" href="{SITE}{CHEMINS[lang]}">
{alternates}<link rel="alternate" hreflang="x-default" href="{SITE}/traducteur-multimedia">
<meta property="og:title" content="{_ech(t['titre'])}">
<meta property="og:description" content="{_ech(t['description'])}">
<meta property="og:type" content="article">
<meta property="og:locale" content="{t['locale']}">
<style>{CSS}</style>
</head>
<body>
{_nav(lang)}
<main>
{_corps(donnees, lang)}
</main>
{_pied(lang)}
</body>
</html>
"""


def construire_anteriorite(donnees: Dict[str, Any]) -> Dict[str, Any]:
    fichiers = []
    for chemin in (tm.CHEMIN_SOURCE, Path(tm.__file__), Path(__file__)):
        stat = chemin.stat()
        fichiers.append(
            {
                "chemin": str(chemin.relative_to(tm.RACINE)).replace("\\", "/"),
                "sha256": tm.sha256_fichier(chemin),
                "octets": stat.st_size,
            }
        )
    return {
        "genere_le_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fichiers": fichiers,
        "racine_merkle": tm.merkle([f["sha256"] for f in fichiers] + [donnees["sceau_sha256"]]),
        "auteur": AUTEUR,
        "doi_anterieur": DOI,
        "depot": DEPOT,
        "doi_anterieur_resolu": DOI_RESOLU,
        "depot_public_resolu": DEPOT_PUBLIC_RESOLU,
        "liens_verifies_le_utc": VERIF_LIENS_UTC,
        "preuve_integrite": True,
        "preuve_date_legale": False,
        "limite": (
            "Le manifeste prouve l'intégrité et l'ordre des fichiers. Il ne prouve pas à lui seul "
            "une date légalement opposable : ancrer la racine via OpenTimestamps, un dépôt public "
            "ou un DOI résolvable. Le DOI déclaré renvoyait 404 à la vérification du 2026-10-29 : "
            "il ne vaut pas preuve en l'état. Le dépôt public GitHub est accessible."
        ),
    }


def ecrire_manifeste(donnees: Dict[str, Any], chemin_json: Path, chemin_web: Path) -> Dict[str, Any]:
    fichiers = []
    for chemin in (
        tm.CHEMIN_SOURCE,
        Path(tm.__file__),
        Path(__file__),
        PAGES["fr"],
        PAGES["en"],
        PAGES["ar"],
        chemin_json,
        chemin_web,
    ):
        stat = chemin.stat()
        fichiers.append(
            {
                "chemin": str(chemin.relative_to(tm.RACINE)).replace("\\", "/"),
                "sha256": tm.sha256_fichier(chemin),
                "octets": stat.st_size,
                "mtime_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc)
                .strftime("%Y-%m-%dT%H:%M:%SZ"),
            }
        )
    manifeste = {
        "titre": "Manifeste d'intégrité et d'antériorité — traducteur multimédia AL-MIZAN",
        "auteur": AUTEUR,
        "doi_anterieur": DOI,
        "depot": DEPOT,
        "doi_anterieur_resolu": DOI_RESOLU,
        "depot_public_resolu": DEPOT_PUBLIC_RESOLU,
        "liens_verifies_le_utc": VERIF_LIENS_UTC,
        "source": donnees["source"]["url"],
        "genere_le_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "nb_fichiers": len(fichiers),
        "racine_merkle_sha256": tm.merkle([f["sha256"] for f in fichiers]),
        "sceau_noyau_sha256": donnees["sceau_sha256"],
        "fichiers": fichiers,
        "preuve_integrite": True,
        "preuve_date_legale": False,
        "limite": (
            "Le manifeste prouve l'intégrité et l'ordre. Pour une date opposable : OpenTimestamps, "
            "dépôt public ou DOI résolvable. Le DOI déclaré renvoyait 404 à la vérification du "
            "2026-10-29 : il ne vaut pas preuve en l'état. Le dépôt public GitHub est accessible."
        ),
    }
    PREUVES.mkdir(parents=True, exist_ok=True)
    _ecrire(PREUVES / "manifeste_sha256.json", json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n")
    _publier_preuves()
    return manifeste


def _publier_preuves() -> None:
    """Copie octet pour octet les preuves sous web_cloud/ pour qu'un pair puisse vérifier."""
    PUBLICATION.mkdir(parents=True, exist_ok=True)
    for _nom, origine, cible in PREUVES_PUBLIEES:
        (PUBLICATION / cible).write_bytes(origine.read_bytes())
    (PUBLICATION / "manifeste_sha256.json").write_bytes(
        (PREUVES / "manifeste_sha256.json").read_bytes()
    )


def generer() -> Dict[str, Any]:
    donnees = tm.construire()
    if donnees["resume"]["controles_ok"] != donnees["resume"]["controles_total"]:
        echoues = [c["code"] for c in donnees["controles"] if not c["ok"]]
        raise RuntimeError(f"Contrôles en échec : {echoues}")

    WEB.mkdir(parents=True, exist_ok=True)
    for lang in LANGUES:
        _ecrire(PAGES[lang], _html(donnees, lang))
    _ecrire(
        WEB / "traducteur_multimedia_resultats.json",
        json.dumps(donnees, ensure_ascii=False, indent=2) + "\n",
    )

    donnees = tm.finaliser(tm.construire())
    donnees["anteriorite"] = construire_anteriorite(donnees)
    if not donnees["continuite"]["publiable"]:
        raise RuntimeError(f"Continuité incomplète : {donnees['continuite']}")

    for lang in LANGUES:
        _ecrire(PAGES[lang], _html(donnees, lang))
    charge = json.dumps(donnees, ensure_ascii=False, indent=2)
    chemin_json = RESULTATS / "traducteur_multimedia.json"
    _ecrire(chemin_json, charge + "\n")
    chemin_web = WEB / "traducteur_multimedia_resultats.json"
    _ecrire(chemin_web, charge + "\n")
    manifeste = ecrire_manifeste(donnees, chemin_json, chemin_web)
    return {
        "pages": {
            lang: {"chemin": str(PAGES[lang]), "octets": PAGES[lang].stat().st_size}
            for lang in LANGUES
        },
        "json": str(chemin_web),
        "controles": f"{donnees['resume']['controles_ok']}/{donnees['resume']['controles_total']}",
        "equations": len(donnees["equations"]),
        "completude": round(donnees["trajectoire"]["completude_finale"], 6),
        "sceau_sha256": donnees["sceau_sha256"],
        "racine_merkle": manifeste["racine_merkle_sha256"],
        "continuite": donnees["continuite"],
    }


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(json.dumps(generer(), ensure_ascii=False, indent=2))
