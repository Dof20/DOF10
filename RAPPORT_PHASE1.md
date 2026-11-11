# LYRA V2.1 — Rapport de phase 1 (11 novembre 2026)

**Verdict : aucune opportunité n'est validée à ce stade.** Un candidat principal se dégage — une mini-marque « routine eau dure » autour d'un filtre de douche avec cartouches récurrentes — mais trois preuves manquent pour le retenir : le coût fournisseur réel, un fournisseur dropship US confirmé et le paysage publicitaire. Le protocole interdit de forcer la sélection ; je ne la force pas.

Tout est rejouable : `python3 research/build_db.py` recrée `research/lyra.db` et les CSV de `research/exports/`.

## 1. Audit de l'environnement

| Capacité | État | Conséquence |
|---|---|---|
| WebSearch | OK | Seul accès web fonctionnel ; donne des résumés, pas la lecture des pages |
| AdWhispr (Google Keyword Planner + Google Shopping) | Quota épuisé (15/15, retour le 1er décembre) | 7 jeux de mots-clés complets obtenus ; auto/voyage et bébé non couverts |
| Ubersuggest | 3 rapports/jour | 2 fiches mot-clé + autocomplétion Google utilisées |
| Semrush | 0 unité API | Inutilisable |
| Perplexity (configuré dans `.mcp.json`) | Échec réseau | Inutilisable tant que son hôte n'est pas autorisé |
| Ahrefs, Similarweb, AdsAgent, AdCopilot, Klaviyo… | 403 à la connexion | Inutilisables |
| HTTP direct, Playwright, lecture de pages | Bloqués par la politique réseau | Amazon, Reddit, Google Trends, TikTok Creative Center, Meta Ads Library, Pinterest Trends et sites fournisseurs inaccessibles |
| Shopify | Connecté, boutique France / EUR / Basic | Shopify Collective refuse de sourcer pour cette boutique |
| Python, pandas, sqlite3, Node | OK | Base et exports construits |

Deux points demandent votre décision (section 7) : la boutique Shopify est en EUR alors que la mission vise l'USD, et le réseau de l'environnement bloque presque toutes les sources primaires.

## 2. Méthode

Les huit missions ont été exécutées séquentiellement par un seul agent, en appels parallèles. Chaque observation est stockée dans `evidence` avec source, URL, date, méthode, fiabilité et limites, et un statut :

- **FACT** : donnée observée dans un outil ou une source citée.
- **ESTIMATE** : calcul ou jugement à partir de faits.
- **HYPOTHESIS** : non vérifié.
- **UNAVAILABLE** : inaccessible.

Attention : les faits issus de WebSearch sont des résumés de résultats ; les pages n'ont pas pu être ouvertes pour recoupement.

## 3. Demande consommateur américaine

Données Google Keyword Planner (US, recherches mensuelles moyennes), sauf mention contraire. Toutes sont des FACT.

| Besoin recherché | Mot-clé principal | Recherches/mois | CPC haut de page | Lecture |
|---|---|---:|---|---|
| Eau dure sous la douche | hard water shower filter | 22 200 | $0.55–3.70 | Intention d'achat nette |
| | shower filter (Ubersuggest) | 33 100 | $4.67 moyen | 27 100 en juillet → 33 100 d'août à octobre |
| | water softener shower head | 9 900 | $0.58–3.29 | Promesse que le produit ne tient pas (voir §4) |
| Douleur cervicale au sommeil | cervical pillow | 40 500 | $0.47–2.23 | Ubersuggest : 33 100, CPC $1.75 |
| | best pillow for neck pain | 27 100 | $0.58–2.93 | Résultats saturés de comparatifs affiliés |
| Posture | posture corrector | 49 500 | $0.27–2.82 | Produit à $15–25, hors fourchette |
| Lumière rouge | red light therapy at home | 33 100 | $0.48–2.82 | Dispositif FDA, prix au-dessus de $90 |
| Chien qui tire | best dog no pull harness | 6 600 | $0.45–2.04 | Volume faible ; DTC déjà à $36–40 |
| Chat et canapé | cat scratcher couch | 6 600 | $0.38–1.50 | Prix sous $40 |
| Bureau | foot rest under desk | 12 100 | $0.27–1.45 | Commodité sous $45 |
| Chute de cheveux (femmes) | hair loss treatment for women | 27 100 | $2.16–12.70 | Médical ; alimente la demande « eau dure » |

L'autocomplétion Google révèle des sous-segments pour le filtre de douche : dortoirs universitaires (« for college dorm », « for communal bathrooms »), eau de puits, eczéma, bébé, extensions capillaires, cheveux blonds. Elle révèle aussi le doute : « shower filters that actually work », « reddit », « causing rash ».

## 4. Candidat principal : routine eau dure

**Pour**

- Demande forte et en hausse : Spate mesure +33,4 % sur un an toutes plateformes (cité par Fast Company).
- Récurrence structurelle : cartouche à remplacer tous les 90 jours. Jolie vend la recharge $33–38.
- Espace de prix : entre l'entrée de gamme ($18–35 chez Walmart, Stone Stream à $34.99) et Jolie ($165), un héros à $49–79 est crédible.
- Preuve de marché : Jolie a dépassé $28 M en 2023 ; son fondateur annonce environ $50 M en 2025 (non recoupé).

**Contre**

- La promesse que les gens recherchent n'est pas tenue par le produit. Les filtres réduisent le chlore, pas la dureté ni le fer. « Water softener shower head » est une allégation à ne pas reprendre.
- Risque juridique réel : deux class actions contre Jolie en 2026 (chlore « réduit » d'environ 66 % et non « éliminé »), avis public NSF de 2024 sur des allégations NSF-177 non autorisées, Eskiin épinglé par TINA.org pour allégations eczéma et chute de cheveux.
- Acquisition chère : difficulté payante 100/100 et CPC moyen $4.67 sur « shower filter ».
- Californie : les pommeaux doivent respecter 1,8 gpm et être certifiés CEC. Un filtre « inline » sans pommeau y échapperait peut-être (HYPOTHESIS, à confirmer).
- Fournisseurs : aucun coût unitaire obtenu. Pistes US non confirmées : Crystal Quest (programme dropship annoncé), Sprite Industries (fabriqué en Californie, NSF/ANSI 177), Fresh Water Systems.

**Gamme envisagée (HYPOTHESIS, à valider avec les fournisseurs)**

| Rôle | Produit | Prix cible |
|---|---|---|
| Héros | Filtre de douche inline certifié NSF/ANSI 177 | $49–69 |
| Complément 1 | Cartouche de remplacement, en abonnement 90 jours | $22–28 |
| Complément 2 | Kit de bandelettes de test (dureté, chlore, fer) | $12–15 |
| Bundle | Filtre + 2 cartouches + kit de test | $79–89 |

Le kit de test sert le positionnement honnête : « mesurez votre eau, voici ce que le filtre change et ce qu'il ne change pas ». C'est l'angle laissé libre par les concurrents attaqués sur leurs allégations.

## 5. Économie unitaire (ESTIMATE)

Base : CPA Meta médian de $38.99 (Triple Whale, plus de 40 000 marques), frais Shopify 2,9 % + $0.30. Le coût produit + port est une HYPOTHESIS, faute de devis.

| Prix héros | Coût + port | Marge 1re commande | Avec 2 recharges à $25 | CPA maximum supportable |
|---|---|---:|---:|---:|
| $49 | $20 | −$11.71 | +$20.24 | $27.28 |
| $59 | $20 | −$2.00 | +$29.95 | $36.99 |
| $69 | $20 | +$7.71 | +$39.66 | $46.70 |
| $59 | $25 | −$7.00 | +$24.95 | $31.99 |

Au CPA médian, la première commande est à l'équilibre ou en perte : la rentabilité dépend entièrement du réachat de cartouches. Un budget de 1 500 € finance environ 40 acquisitions au CPA médian, ce qui est trop peu pour mesurer un taux de réabonnement. Le budget impose donc un démarrage organique (TikTok, SEO sur les sous-segments dortoir et eau de puits) plutôt que payant.

## 6. Classement (ESTIMATE, grille pondérée sur 5)

| Candidat | Score | Statut |
|---|---:|---|
| Routine eau dure (filtre de douche) | 3,55 | Candidat principal, non validé |
| Oreiller cervical | 3,20 | Alternative faible : achat unique, commodité, retours |
| Harnais anti-traction | 2,85 | Écarté : volume faible |
| Correcteur de posture | 2,80 | Écarté : prix hors fourchette |
| Lumière rouge | 2,50 | Écarté : FDA et prix |

Le détail des notes et leur justification sont dans `research/exports/scores.csv`. L'écart entre les deux premiers est faible et repose sur mon jugement, pas sur une mesure.

## 7. Ce qui manque et décisions attendues

Preuves manquantes pour valider le candidat :

1. Coût unitaire et conditions d'un fournisseur dropship US, avec certificat NSF/ANSI 177.
2. Paysage publicitaire (Meta Ads Library, TikTok Creative Center) : nombre d'annonceurs et angles.
3. Avis négatifs lus à la source (Amazon, Reddit) et prix concurrents vérifiés.
4. Confirmation réglementaire Californie pour un filtre inline.
5. Mots-clés des catégories non couvertes (auto/voyage, bébé), pour s'assurer qu'aucun meilleur candidat n'a été manqué.

Décisions qui vous reviennent :

- **Réseau** : autoriser dans l'environnement les hôtes des sources primaires (Amazon, Reddit, Google Trends, Meta Ads Library, sites fournisseurs, API Perplexity). Sans cela, les points 2 à 4 restent inaccessibles.
- **Quota mots-clés** : attendre le 1er décembre (AdWhispr) ou recharger Semrush. Je n'ai souscrit à rien.
- **Boutique** : la boutique connectée est en EUR et basée en France. Vendre en USD aux États-Unis demande soit une nouvelle boutique, soit Shopify Markets ; cela conditionne aussi l'accès à Shopify Collective. Je n'ai rien modifié.
- **Fournisseurs** : le message ci-dessous est prêt ; je ne l'envoie pas sans votre accord.

## 8. Brouillon de demande fournisseur (non envoyé)

> Subject: Drop-ship / reseller inquiry — inline shower filters
>
> Hello,
>
> I am launching a US-focused Shopify store and am evaluating suppliers for an inline shower filter line. Could you share:
>
> 1. Whether you offer drop-shipping to US consumers, and from which warehouse
> 2. Unit price and shipping cost for your inline shower filter and its replacement cartridge, at 1, 50 and 200 units per month
> 3. Your NSF/ANSI 177 certificate number and the models it covers
> 4. Whether private label or neutral packaging is available, and any MAP policy
> 5. Average handling time, return terms and defect rate
> 6. Whether the product may be shipped to California
>
> Thank you,
> [Name]

## Sources principales

- Google Keyword Planner via AdWhispr, Ubersuggest (volumes, CPC, autocomplétion), consultés le 11/11/2026
- [Fast Company — dorm water panic, données Spate](https://www.fastcompany.com/91391356/the-tiktok-dorm-water-panic-is-officially-here)
- [ClassAction.org — Rusow v. Jolie](https://www.classaction.org/news/class-action-lawsuit-claims-jolie-filtered-showerheads-leave-substantial-amount-of-chlorine-in-water)
- [NSF — avis public Jolie](https://nsf.org/about-nsf/public-notices/jolie)
- [Truth in Advertising — Eskiin](https://truthinadvertising.org/articles/eskiin/)
- [Beauty Independent — Jolie chez Ulta](https://beautyindependent.com/filtered-showerhead-brand-jolie-ulta-beauty)
- [Triple Whale — benchmarks e-commerce](https://www.triplewhale.com/blog/ecommerce-benchmarks)
- [Culligan — limites des filtres de douche](https://www.culligan.com/blog/what-are-shower-filters-and-do-they-really-work)
- [Persistence Market Research — marché des filtres de douche](https://www.persistencemarketresearch.com/market-research/shower-filter-market.asp)
- [Avalara — fin du de minimis](https://www.avalara.com/us/en/blog/de-minimis-exemption-changes-coming.html)
- [Crystal Quest — programme drop-shipping](https://crystalquest.com/pages/drop-shipping)

La liste complète, avec fiabilité et limites par observation, est dans `research/exports/evidence.csv`.
