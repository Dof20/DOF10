# LYRA V2.3 — Trending Product Hunter (12 novembre 2026)

**Verdict : pas de GO.** Le moteur de croissance a trouvé des produits dont les recherches progressent réellement, mais aucun ne dégage une marge suffisante en dropshipping sans stock au coût d'acquisition médian. Un candidat mérite une instruction complète avant toute décision : le matelas de sol japonais.

Rejouable : `python3 research/build_db.py` (tables `growth` et `sourcing` ajoutées, exports CSV dans `research/exports/`).

## 1. Audit des données existantes

La base V2.1/V2.2 contenait 34 preuves et 8 candidats, tous choisis par volume de recherche et non par croissance. Elle ne mesurait aucune tendance. Le filtre de douche y reste « demande validée, offre non validée ».

## 2. Moteur de détection de croissance

| Source | Ce qu'elle mesure | État |
|---|---|---|
| Exploding Topics, 12 catégories | Volume mensuel avant/après sur 2 ans, par sujet | Lu : 267 sujets |
| Exploding Topics, 44 produits et 11 produits animaux | Croissance sur 5 ans, volume, prix | Lu |
| Glimpse (Google Trends) | Croissance sur un an de 12 produits | Lu |
| Pinterest Trends US | Catégories shopping, variation mensuelle | Lu (saisonnier) |
| Ubersuggest | Volume US, CPC, 4 derniers mois | 3 rapports utilisés |
| Google Trends | Courbe sur 5 ans | Refusé (429) à chaque tentative |
| Amazon, Target, Chewy, eBay, Etsy | Ventes, prix, avis | Refusent les accès automatisés ; non contournés |
| TikTok Creative Center | Produits en tête | Détail derrière connexion |

Limite principale : la croissance de chaque sujet repose sur une seule source. Le périmètre géographique des volumes Exploding Topics n'est pas précisé ; ils dépassent les volumes américains d'Ubersuggest.

## 3. Ce qui croît réellement

Sur 267 sujets, la majorité sont des cosmétiques, des compléments, des aliments, des vêtements ou des noms de marque. Les produits physiques non consommables les plus dynamiques :

| Produit | Recherches/mois avant → après | Croissance 2 ans | Prix de vente usuel | Lecture |
|---|---|---:|---|---|
| Magnetic shelf | 609 → 6 600 | +984 % | 20–40 $ | Sous la fourchette |
| Twin floor bed | 1 286 → 9 900 | +670 % | > 90 $ | Mobilier enfant, normes de sécurité |
| Shoe bag | 7 279 → 49 500 | +580 % | < 25 $ | Sous la fourchette |
| Japanese floor mattress | 3 837 → 22 200 | +479 % | 60–150 $ | Dans la fourchette, volumineux |
| Mini rice cooker | 6 147 → 33 100 | +438 % | 25–50 $ | Électrique, sous la fourchette |
| Dual shower head | 2 283 → 12 100 | +430 % | 30–80 $ | Réglementation californienne |
| Monitor light | 3 620 → 18 100 | +400 % | 30–60 $ | Dominé par des marques |
| Label printer | 38 232 → 165 000 | +332 % | 30–100 $ | Dominé par des marques |
| Acoustic wall panels | 46 343 → 135 000 | +191 % | 40–150 $ | Volumineux, non approfondi |
| Dog stroller | 21 780 → 60 500 | +178 % | 60–150 $ | Dans la fourchette |
| Heated eye mask | 8 222 → 22 200 | +170 % | 20–50 $ | Bas de fourchette |
| Dog bed stairs | 22 140 → 40 500 | +83 % | 40–70 $ | Dans la fourchette |

Glimpse confirme par ailleurs le filtre de douche eau dure à +20 % sur un an, cohérent avec la V2.1.

## 4. Groupe instruit : mobilité du chien

Trois produits liés croissent ensemble, portés par le vieillissement des chiens et les petites races : poussette, escalier de lit, siège auto.

| Mot-clé (Ubersuggest, États-Unis) | Recherches/mois | CPC | 4 derniers mois |
|---|---:|---:|---|
| dog stroller | 40 500 | 0,67 $ | Plat (série datée de 2025 par l'outil) |
| dog car seat | 40 500 | 1,35 $ | Plat |
| dog stairs for bed | 22 200 | 0,93 $ | 18 100 en juillet, puis 22 200 |

Le CPC est trois à sept fois plus bas que celui du filtre de douche (4,67 $). En revanche, la série courte d'Ubersuggest ne confirme pas la hausse : elle est plate sur quatre mois.

**Sourcing (AliExpress, expédition depuis les États-Unis, prix public port inclus)**

| Produit | Coût | Prix de vente testé | Marge avant publicité | Après CPA médian de 38,99 $ |
|---|---|---:|---|---|
| Poussette | 64–99 $ | 89 $ | −13 à +22 $ | −52 à −17 $ |
| Escalier de lit en mousse | 20–51 $ | 59 $ | +6 à +37 $ | −33 à −2 $ |
| Siège auto mousse à mémoire | 39–59 $ | 79 $ | +17 à +37 $ | −22 à −2 $ |

Aucun des trois ne couvre le coût d'acquisition médian, et aucun n'a de réachat. Les sièges auto posent en plus un problème d'allégation : les essais du Center for Pet Safety montrent que la plupart échouent, et il n'existe pas de norme obligatoire.

Ces marges sont des estimations sur prix de détail AliExpress ; un tarif négocié les améliorerait, sans que je puisse dire de combien.

## 5. Candidat à instruire : matelas de sol japonais

C'est le seul produit examiné dont la marge peut rester positive après publicité : coût relevé de 25 à 83 $, soit de −36 à +22 $ par commande à 89 $. La croissance est la plus forte des produits dans la fourchette (+479 %, 22 200 recherches/mois).

Rien n'est validé à ce stade : pas de volume américain, pas de CPC, pas de lecture des concurrents ni des avis, et le produit est volumineux, ce qui pèse sur le port et les retours.

## 6. Ce que je ferais ensuite

1. Instruire le matelas de sol japonais : volume et CPC américains, concurrents, avis, coût de port réel, taux de retour.
2. Recouper la croissance sur Google Trends dès que l'accès revient, pour ce produit et pour la mobilité du chien.
3. Obtenir un vrai tarif dropship (CJ Dropshipping, Spocket ou Zendrop demandent un compte), car toutes les marges ci-dessus reposent sur des prix de détail.

## Sources

Lues directement le 12 novembre 2026 :

- [Exploding Topics — 44 produits tendance](https://explodingtopics.com/blog/trending-products)
- [Exploding Topics — sujets maison par croissance](https://explodingtopics.com/home-topics-by-growth)
- [Exploding Topics — sujets animaux par croissance](https://explodingtopics.com/pets-topics-by-growth)
- [Exploding Topics — produits animaux](https://explodingtopics.com/blog/pet-products)
- [Glimpse — produits Google Trends](https://meetglimpse.com/google-trends/products/)
- [Pinterest Trends](https://trends.pinterest.com/)
- [AliExpress — poussettes expédiées des États-Unis](https://www.aliexpress.us/w/wholesale-dog-stroller.html?shipFromCountry=US)

Connues par résumé de recherche, pages non ouvertes :

- [SaleHoo — tendance poussette pour animaux](https://www.salehoo.com/trends/pet-stroller)
- [Center for Pet Safety — essais de sièges](https://www.centerforpetsafety.org/?p=1152)
- [Triple Whale — benchmarks](https://www.triplewhale.com/blog/ecommerce-benchmarks)
