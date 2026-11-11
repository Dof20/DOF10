"""LYRA V2.1 - base de recherche. Relancer: python3 research/build_db.py (recrée lyra.db + exports CSV).
Statuts: FACT (observé), ESTIMATE (calculé/jugé), HYPOTHESIS (non vérifié), UNAVAILABLE (inaccessible)."""
import sqlite3, csv, os
H = os.path.dirname(os.path.abspath(__file__))
D = "2026-11-11"
db = os.path.join(H, "lyra.db")
if os.path.exists(db): os.remove(db)
c = sqlite3.connect(db)
c.executescript("""
CREATE TABLE products(id TEXT PRIMARY KEY, name TEXT, price_band TEXT, verdict TEXT);
CREATE TABLE keywords(kw TEXT, product_id TEXT, vol INTEGER, competition TEXT, cpc_low REAL, cpc_high REAL, source TEXT, date TEXT, status TEXT);
CREATE TABLE evidence(id INTEGER PRIMARY KEY, product_id TEXT, agent TEXT, status TEXT, observation TEXT, source TEXT, url TEXT, date TEXT, method TEXT, reliability TEXT, limits TEXT);
CREATE TABLE competitors(product_id TEXT, brand TEXT, price TEXT, note TEXT, source TEXT, status TEXT);
CREATE TABLE suppliers(product_id TEXT, name TEXT, type TEXT, note TEXT, url TEXT, status TEXT);
CREATE TABLE scores(product_id TEXT, criterion TEXT, weight REAL, score INTEGER, rationale TEXT);
CREATE TABLE tools(tool TEXT, state TEXT, note TEXT);
""")
P = [("SHOWER","Routine eau dure : filtre de douche + cartouches","$40-90 (héros) + recharge récurrente","CANDIDAT PRINCIPAL - NON VALIDÉ"),
("PILLOW","Oreiller cervical ergonomique","$40-90","ALTERNATIVE - faible"),
("REDLIGHT","Luminothérapie rouge à domicile",">$90 typique","ÉCARTÉ (prix, FDA)"),
("POSTURE","Correcteur de posture","<$40","ÉCARTÉ (prix, commodité)"),
("DOGPULL","Harnais anti-traction chien","$36-40","ÉCARTÉ (volume faible, bas de fourchette)"),
("CATSCRATCH","Protection canapé / griffoir chat","<$40","ÉCARTÉ (prix)"),
("DESK","Accessoires bureau (repose-pieds, rehausseur)","<$45","ÉCARTÉ (prix, commodité)"),
("HEATPAD","Coussin chauffant nuque/épaules","$30-60","RÉSERVE (non approfondi)")]
c.executemany("INSERT INTO products VALUES(?,?,?,?)", P)
GKP = "Google Keyword Planner via AdWhispr MCP (US, geo 2840)"
K = [("hard water shower filter","SHOWER",22200,"High",.55,3.70),("shower head filter for hard water","SHOWER",12100,"High",.60,3.63),
("water softener shower head","SHOWER",9900,"High",.58,3.29),("hair loss treatment for women","SHOWER",27100,"High",2.16,12.70),
("cervical pillow","PILLOW",40500,"High",.47,2.23),("pillow for neck pain","PILLOW",33100,"High",.50,2.76),
("best pillow for neck pain","PILLOW",27100,"High",.58,2.93),("best side sleeper pillow for neck pain","PILLOW",12100,"High",.56,3.11),
("anti snoring devices","PILLOW",9900,"High",1.27,5.67),("snoring nose strip","PILLOW",40500,"High",.30,3.17),
("red light therapy at home","REDLIGHT",33100,"High",.48,2.82),("posture corrector","POSTURE",49500,"High",.27,2.82),
("back brace for posture","POSTURE",12100,"High",.21,1.08),("posture corrector for women","POSTURE",5400,"High",.29,3.21),
("best dog no pull harness","DOGPULL",6600,"High",.45,2.04),("dog pulling on leash","DOGPULL",1900,"High",.32,2.34),
("dog anxiety","DOGPULL",18100,"High",.38,2.54),("thundershirt for dogs","DOGPULL",27100,"High",.31,1.28),
("cat scratching post","CATSCRATCH",60500,"High",.36,1.37),("cat scratcher couch","CATSCRATCH",6600,"High",.38,1.50),
("protect couch from cat","CATSCRATCH",5400,"High",.39,1.16),("foot rest under desk","DESK",12100,"High",.27,1.45),
("monitor riser","DESK",12100,"High",.38,3.50),("laptop stand for desk","DESK",14800,"High",.33,1.66),
("anti fatigue mat for standing desk","DESK",5400,"High",.56,6.91),("neck and shoulder heating pad","HEATPAD",6600,"High",.22,.89),
("back pain relief","HEATPAD",165000,"Low",.90,4.74),("sciatica relief","HEATPAD",74000,"High",.05,3.35),
("lower back pain relief","HEATPAD",60500,"Medium",.06,3.57),("chirp wheel+","HEATPAD",27100,"High",.22,.82),
("closet organization",None,135000,"High",.67,9.11),("shoe organizer for closet",None,49500,"High",.24,1.30),
("car trunk organizer",None,18100,None,.23,.65)]
c.executemany("INSERT INTO keywords VALUES(?,?,?,?,?,?,?,?,?)", [k+(GKP,D,"FACT") for k in K])
c.executemany("INSERT INTO keywords VALUES(?,?,?,?,?,?,?,?,?)", [
("shower filter","SHOWER",33100,"paid difficulty 100/100, SEO 35",4.67,4.67,"Ubersuggest MCP (US) - mensuel: 07/26 27100, 08-10/26 33100",D,"FACT"),
("cervical pillow","PILLOW",33100,"paid difficulty 100/100, SEO 33",1.75,1.75,"Ubersuggest MCP (US) - mensuel: 07/26 33100, 08-09/26 40500, 10/26 33100",D,"FACT")])
WS="WebSearch (résumé de résultats, page non ouverte)"
E = [
("SHOWER","A1","FACT","Autocomplétion Google: 'shower filter for hard water / for hair / for well water / for dorm / for college dorm / for communal bathrooms / for eczema / baby / and hair loss / reddit / that actually work / causing rash'","Ubersuggest google_suggestions","",D,"MCP","Haute","Pas de volumes associés"),
("SHOWER","A1","FACT","Autocomplétion 'hard water hair': hair loss, hair color, blonde, curly, hair extensions, 'how to fix hard water hair', nombreuses variantes 'reddit'","Ubersuggest google_suggestions","",D,"MCP","Haute","Pas de volumes"),
("SHOWER","A2","FACT","Spate (cité par Fast Company): filtres de douche +33,4% sur un an toutes plateformes, +10,8% sur TikTok; '55,3 M de vidéos' TikTok sur l'installation; Amazon a une section 'Shower Heads for College Dorms' ($10-150)","Fast Company","https://www.fastcompany.com/91391356/the-tiktok-dorm-water-panic-is-officially-here",D,WS,"Moyenne","Date de l'article non confirmée; chiffres de seconde main"),
("SHOWER","A4","FACT","Jolie: >$28M de CA en 2023 (Shopify); ~$50M en 2025 selon le fondateur (non recoupé); objectif >$100M en 2027; entrée chez Ulta","Shopify / Beauty Independent","https://beautyindependent.com/filtered-showerhead-brand-jolie-ulta-beauty",D,WS,"Moyenne","2025 = déclaration du fondateur"),
("SHOWER","A4","FACT","Jolie: pommeau $165 ($148 avec abonnement), recharge $33/90 jours (abonnement) ou $38 (Ulta)","jolieskinco.com / Ulta via recherche","https://jolieskinco.com/pages/faq",D,WS,"Moyenne","Prix à revérifier sur site"),
("SHOWER","A4","FACT","~80% des clients Jolie abonnés, churn 3% (Modern Retail, 2023) - source Smartrr contradictoire (abonnement >15% du CA)","Modern Retail","https://www.modernretail.co/marketing/dtc-briefing-how-jolie-reached-4-2m-in-sales-its-first-year-while-staying-profitable/",D,WS,"Faible","Deux sources en conflit, anciennes"),
("SHOWER","A3","FACT","Entrée de gamme: 15-stage ~$18-35 (Walmart, Stone Stream $34.99, cartouche $19.95); AquaBliss SF100 décrit comme best-seller Amazon (note 4.4) par des sites affiliés","Walmart / stone-stream.com / sites affiliés","https://us.stone-stream.com/products/wall-fixed-shower-head-15-stage-filtration-system-ecolux",D,WS,"Moyenne","Amazon non consultable directement; 'best-seller' non prouvé"),
("SHOWER","A5","FACT","Frustrations: les filtres réduisent surtout le chlore et n'adoucissent PAS l'eau dure; pas d'effet sur le fer (cheveux orange, eau de puits); coût des recharges; 'pas de différence notable'; durée de vie courte","Culligan, Kinetico, snapshot Reddit 04/2026, WhoWhatWear, Thingtesting","https://www.culligan.com/blog/what-are-shower-filters-and-do-they-really-work",D,WS,"Moyenne","Culligan/Kinetico vendent des adoucisseurs (biais); fils Reddit non lus en direct"),
("SHOWER","A8","FACT","Class action Rusow v. Jolie Skin Co (déposée 19/03/2026, 3:26-cv-02411): réduction du chlore ~66% vs 'removes'; 2e action Clifft v. Jolie; avis public NSF (10/04/2024) sur allégations NSF-177 non autorisées","classaction.org / NSF / truthinadvertising.org","https://www.classaction.org/news/class-action-lawsuit-claims-jolie-filtered-showerheads-leave-substantial-amount-of-chlorine-in-water",D,WS,"Haute","Stade des plaidoiries, pas de décision"),
("SHOWER","A8","FACT","TINA.org a épinglé Eskiin pour allégations acné/eczéma/chute de cheveux; les allégations eczéma sont des allégations de médicament; FTC exige une preuve scientifique compétente","truthinadvertising.org","https://truthinadvertising.org/articles/eskiin/",D,WS,"Haute","Pas d'action FTC/FDA directe trouvée"),
("SHOWER","A8","FACT","Californie Title 20 (CEC): pommeaux de douche max 1,8 gpm et certification requise pour vendre/expédier en CA","Détaillants / CEC","https://help.theshowerheadstore.com/en-US/shipping-to-california-140120",D,WS,"Moyenne","Texte réglementaire non lu"),
("SHOWER","A8","HYPOTHESIS","Un filtre 'inline' (sans pommeau) échapperait à l'obligation Title 20 - NON VÉRIFIÉ","","",D,"Raisonnement","Faible","À confirmer auprès de la CEC avant tout lancement"),
("SHOWER","A7","FACT","Crystal Quest (fabricant US) annonce un programme de drop-shipping avec remises par paliers; Sprite Industries (Corona, CA, NSF/ANSI 177, fabriqué USA) - programme revendeur inconnu; Fresh Water Systems a un programme wholesale","crystalquest.com / résultats de recherche","https://crystalquest.com/pages/drop-shipping",D,WS,"Faible","Page inaccessible depuis l'environnement: conditions, prix, MAP inconnus"),
("SHOWER","A7","UNAVAILABLE","Coût unitaire dropship (CJ, Zendrop, Spocket) et prix Alibaba: aucun prix lisible. Seule référence: Alibaba MOQ 100 pcs sans prix","","",D,WS,"-","Sites fournisseurs bloqués par la politique réseau"),
("SHOWER","A8","FACT","Marché mondial des filtres de douche 2026: $497M (FMI) à $639M (Persistence), CAGR 6,9-8,7%","Persistence MR / Future Market Insights","https://www.persistencemarketresearch.com/market-research/shower-filter-market.asp",D,WS,"Faible","Cabinets d'études payants, périmètres divergents"),
("PILLOW","A1","FACT","Autocomplétion 'cervical pillow': for side sleepers, sleep apnea/CPAP, after neck surgery, 'causing neck pain', 'adjustment period', 'do they work', 'ear hole', 'HSA/FSA eligible'","Ubersuggest google_suggestions","",D,"MCP","Haute","Pas de volumes"),
("PILLOW","A3","FACT","SERP saturée de comparatifs affiliés (Osteo, Cozyplayer, UTTU, EPABO, Derila, Cushion Lab); critique dominante: fermeté","Sites comparatifs","https://findingdulcinea.com/best-cervical-pillows-for-neck-pain/",D,WS,"Faible","Prix concurrents non obtenus = UNAVAILABLE"),
("PILLOW","A8","FACT","Orthèse cervicale = code FDA IQK, classe I; les allégations 'guérit/traite' sortent du cadre","Bases 510(k) tierces","https://fda.innolitics.com/productcode/IQK",D,WS,"Moyenne","Base FDA officielle non consultée"),
(None,"A8","FACT","Benchmark Meta (Triple Whale, >40 000 marques, 08/2025-07/2026): CPA médian $38.99, CPM $15.06, ROAS 1.88, conversion 1,53%","Triple Whale","https://www.triplewhale.com/blog/ecommerce-benchmarks",D,WS,"Moyenne","Toutes catégories; pas spécifique petits budgets"),
(None,"A8","FACT","Marge nette moyenne dropshipping 5-20% après pub, frais et remboursements (TrueProfit, 1 200 boutiques, cité par Shopify); conversion Shopify moyenne 1,2-1,8%","Shopify / Littledata","https://www.shopify.com/blog/dropshipping-suppliers",D,WS,"Moyenne",""),
(None,"A8","FACT","De minimis US supprimé (Chine 02/05/2025, tous pays 29/08/2025): les colis directs de Chine paient droits + dédouanement","Avalara, STR Trade","https://www.avalara.com/us/en/blog/de-minimis-exemption-changes-coming.html",D,WS,"Haute","Taux exact par produit non vérifié (HTSUS)"),
(None,"A2","FACT","TikTok Shop US: beauté/soin n°1 (18-22% selon les outils); prix médian des top produits ~$40, 2/3 sous $50","FastMoss, DemandSage, Marketplace Pulse via GeekSeller","https://www.fastmoss.com/blog/best-selling-tiktok-shop-products-us-q2-2026/",D,WS,"Faible","Estimations d'outils tiers"),
(None,"A1","FACT","Google Holiday 100 2026: 'lymphatic sculpting face brush' +400%, 'adjustable roller skates' +180%, 'podcast microphone' +115%","Google blog","https://blog.google/products-and-platforms/products/shopping/holiday-100-gift-guide-2026/",D,WS,"Haute","Signaux cadeaux saisonniers"),
(None,"A1","UNAVAILABLE","Google Trends, Amazon, Reddit, YouTube, TikTok Creative Center, Meta Ads Library, Pinterest Trends, Walmart, Etsy en accès direct: bloqués (403 proxy). Semrush: 0 unité API. Perplexity: échec réseau. AdWhispr: quota 15/15 épuisé jusqu'au 1er déc.","Audit environnement","",D,"curl / MCP","Haute","")]
c.executemany("INSERT INTO evidence(product_id,agent,status,observation,source,url,date,method,reliability,limits) VALUES(?,?,?,?,?,?,?,?,?,?)", E)
c.executemany("INSERT INTO competitors VALUES(?,?,?,?,?,?)", [
("SHOWER","Jolie","$165 / recharge $33-38","Leader DTC, Ulta, 2 class actions 2026",WS,"FACT"),
("SHOWER","AquaBliss SF100","~$30-35 (à vérifier)","Entrée de gamme Amazon",WS,"ESTIMATE"),
("SHOWER","Stone Stream EcoLux","$34.99 / cartouche $19.95","15-stage, positionnement eau dure",WS,"FACT"),
("SHOWER","Afina, Canopy, Hello Klean, Act+Acre, Eskiin, Weddell, Aquasana, Sprite","UNAVAILABLE","Présents dans l'autocomplétion/SERP; prix non obtenus",WS,"UNAVAILABLE"),
("PILLOW","Osteo, Cozyplayer, UTTU, EPABO, Derila, Cushion Lab, Groove","UNAVAILABLE","Commodité Amazon + DTC; prix non obtenus",WS,"UNAVAILABLE"),
("DOGPULL","Dog Friendly Co. $36-39; Spark Paws $39.99; PetSafe $20-25","voir note","Google Shopping page 1",GKP,"FACT")])
c.executemany("INSERT INTO suppliers VALUES(?,?,?,?,?,?)", [
("SHOWER","Crystal Quest","Fabricant US, programme dropship annoncé","Conditions inconnues - à demander","https://crystalquest.com/pages/drop-shipping","HYPOTHESIS"),
("SHOWER","Sprite Industries","Fabricant US (Corona, CA), NSF/ANSI 177","Programme revendeur/dropship non confirmé","https://spritewater.com","HYPOTHESIS"),
("SHOWER","Fresh Water Systems","Distributeur US, programme wholesale","Dropship non confirmé","https://www.freshwatersystems.com/pages/wholesale_program","HYPOTHESIS"),
("SHOWER","Spocket / Zendrop / Syncee / DropCommerce","Plateformes dropship avec entrepôts US","Catalogue filtre de douche non vérifié; Spocket $39.99/mois, Zendrop dès $49/mois","https://apps.shopify.com/categories/finding-products","HYPOTHESIS"),
("SHOWER","Shopify Collective","Indisponible","Boutique connectée en France/EUR: Collective refuse","", "UNAVAILABLE")])
W = [("Demande documentée",.20),("Tendance",.10),("Adéquation prix $40-90",.10),("Récurrence / LTV",.15),("Coût d'acquisition abordable",.15),("Différenciation possible",.10),("Risque réglementaire (5=faible)",.10),("Faisabilité dropship US",.10)]
S = {"SHOWER":[(5,"33 100/mois + 22 200 'hard water'"),(4,"Spate +33% a/a"),(4,"Héros $49-79 crédible entre $35 et $165"),(5,"Cartouche tous les 90 j"),(2,"CPC $4.67, difficulté payante 100"),(3,"Angles dortoir/puits/extensions; promesse 'eau dure' fragile"),(2,"Class actions Jolie, NSF, Title 20, allégations santé"),(2,"Pistes US non confirmées, coûts inconnus")],
"PILLOW":[(5,"33-40 000/mois"),(3,"Stable, pas de signal de hausse"),(5,"$40-90 naturel"),(1,"Achat unique"),(3,"CPC $1.75 mais difficulté payante 100"),(2,"Commodité, SERP affiliée"),(3,"Classe I si allégations médicales"),(3,"Volumineux, retours élevés (HYPOTHESIS)")],
"DOGPULL":[(2,"6 600/mois"),(3,"Inconnu"),(3,"$36-40, bas de fourchette"),(2,"Faible"),(3,"CPC $0.45-2.04"),(3,"DTC déjà présents"),(5,"Faible"),(3,"Non vérifié")],
"POSTURE":[(5,"49 500/mois"),(3,"Inconnu"),(1,"$15-25"),(1,"Unique"),(3,"CPC bas"),(1,"Commodité"),(3,"Allégations"),(4,"Léger")],
"REDLIGHT":[(5,"33 100/mois"),(3,"Inconnu"),(1,">$90 pour produit sérieux"),(1,"Unique"),(3,"CPC $0.48-2.82"),(2,"Nombreux acteurs"),(1,"Dispositif FDA"),(2,"Électronique, retours")]}
for p,rows in S.items():
    for (crit,w),(s,r) in zip(W,rows): c.execute("INSERT INTO scores VALUES(?,?,?,?,?)",(p,crit,w,s,r))
c.executemany("INSERT INTO tools VALUES(?,?,?)", [
("WebSearch","OK","Seul accès web fonctionnel; résumés, pas de lecture de page"),("AdWhispr (Keyword Planner + Google Shopping)","ÉPUISÉ","7 requêtes complètes, quota 15/15, reset 1er déc."),
("Ubersuggest","LIMITÉ","3 rapports/jour; 2 overview + autocomplétion utilisés"),("Semrush","BLOQUÉ","0 unité API"),("Perplexity","ÉCHEC","fetch failed (hôte non autorisé probable)"),
("Ahrefs, Similarweb, Klaviyo, AdsAgent, AdCopilot...","ÉCHEC","403 proxy à la connexion"),("HTTP direct / Playwright / web-fetch","BLOQUÉ","Politique réseau: Amazon, Reddit, Google Trends, TikTok, Meta Ads Library, fournisseurs inaccessibles"),
("Shopify","OK partiel","Boutique France/EUR/Basic; Collective indisponible"),("Python 3.13, pandas, sqlite3, openpyxl, Node 22","OK","matplotlib absent"),("Gmail, Drive, Sheets, Calendar, Gamma, Linear, ElevenLabs","OK","Non utilisés (hors périmètre recherche)")])

# ---- Phase 2 (réseau ouvert, lecture directe via navigateur) ----
PW="Playwright, lecture directe de la page"
E2 = [
("SHOWER","A3","FACT","Amazon 'shower filter for hard water' (48 résultats p.1): prix médian $26.98 (min $8.79, max $136); 11/48 entre $40 et $90; ventes mensuelles affichées cumulées >= 94 000 sur 43 listings","Amazon.com","https://www.amazon.com/s?k=shower+filter+for+hard+water",D,PW,"Haute","'bought in past month' = paliers planchers Amazon; une seule page"),
("SHOWER","A3","FACT","AquaBliss SF100: $36.99 ($33.29 en Subscribe & Save), 4.4/5 sur 70 351 avis (8% de 1-2 étoiles), 10K+ achetés/mois, n°1 'Showerhead Filters', n°77 Tools & Home Improvement, en vente depuis 01/2017, expédié par Amazon, avertissement Prop 65","Amazon.com","https://www.amazon.com/dp/B01MUBU0YC",D,PW,"Haute",""),
("SHOWER","A3","FACT","Récurrence prouvée: cartouche AquaBliss SFC100 $17.99 (10K+/mois) et pack de 3 $42.99 (8K+/mois)","Amazon.com","https://www.amazon.com/s?k=shower+filter+for+hard+water",D,PW,"Haute",""),
("SHOWER","A3","FACT","La fourchette $40-90 se vend: Weddell Duo $89.98 (certifié NSF, 2K+/mois), MyHalos $74.99 (2K+/mois), AquaHomeGroup $49.95 (1K+/mois), AquaBliss SF500 $45.99 (1K+/mois)","Amazon.com","https://www.amazon.com/s?k=shower+filter+for+hard+water",D,PW,"Haute",""),
("SHOWER","A5","UNAVAILABLE","Texte des avis négatifs Amazon (connexion requise), Reddit (403 aux robots), Walmart (contrôle anti-robot): non lus, non contournés","","",D,PW,"-",""),
("SHOWER","A7","FACT","Crystal Quest dropship: gratuit, sans minimum, remises par paliers, fabriqué aux USA, expédition par leurs soins. MAIS: pas de programme pour vendeurs internationaux; vente sous la marque Crystal Quest (pas de marque propre); interdit sur Amazon/eBay/Walmart. Prix publics: filtre dès $40.95, cartouche $29.50","crystalquest.com","https://crystalquest.com/pages/drop-shipping",D,PW,"Haute","Taux de remise non publié"),
("SHOWER","A7","FACT","AliExpress, expédié depuis les USA: filtres génériques 15/20 étages $11.29-24.49, lots avec 3-4 cartouches $23-36; annonces avec allégations 'softens', 'eczema', 'acne'; aucune mention NSF/ANSI 177","aliexpress.us","https://www.aliexpress.us/w/wholesale-15-stage-shower-filter.html?shipFromCountry=US",D,PW,"Moyenne","Prix promotionnels 11.11; prix à $1.09 = offres d'appel exclues"),
("SHOWER","A7","UNAVAILABLE","CJ Dropshipping et Alibaba: contrôle anti-robot; Spocket, Syncee: catalogue derrière connexion; Sprite: aucune page revendeur publique","","",D,PW,"-",""),
("SHOWER","A4","UNAVAILABLE","Meta Ads Library (403), TikTok Creative Center (détail derrière connexion), Google Trends (429): paysage publicitaire et courbe de tendance non obtenus","","",D,PW,"-",""),
(None,"A1","UNAVAILABLE","Perplexity: l'API répond désormais mais la clé est invalide (401)","","",D,"MCP","Haute","Clé à remplacer dans la configuration")]
c.executemany("INSERT INTO evidence(product_id,agent,status,observation,source,url,date,method,reliability,limits) VALUES(?,?,?,?,?,?,?,?,?,?)", E2)
c.execute("UPDATE products SET verdict='DEMANDE VALIDÉE - OFFRE NON VALIDÉE (blocage fournisseur)' WHERE id='SHOWER'")
c.execute("UPDATE scores SET score=1, rationale='Seul fournisseur US certifié trouvé exclut les vendeurs internationaux et la marque propre; génériques non certifiés' WHERE product_id='SHOWER' AND criterion LIKE 'Faisabilité%'")
c.execute("UPDATE scores SET score=2, rationale='AquaBliss n°1 à $36.99 avec 70 351 avis; un générique à $59 sans stock n a pas d avantage' WHERE product_id='SHOWER' AND criterion LIKE 'Différenciation%'")
c.commit()
os.makedirs(os.path.join(H,"exports"),exist_ok=True)
for t in ["products","keywords","evidence","competitors","suppliers","scores","tools"]:
    cur=c.execute(f"SELECT * FROM {t}")
    with open(os.path.join(H,"exports",t+".csv"),"w",newline="") as f:
        w=csv.writer(f); w.writerow([d[0] for d in cur.description]); w.writerows(cur)
print("Scores pondérés /5 (ESTIMATE):")
for p,s in c.execute("SELECT product_id, ROUND(SUM(weight*score),2) FROM scores GROUP BY 1 ORDER BY 2 DESC"): print(f"  {p:10s} {s}")
print("Preuves:",dict(c.execute("SELECT status,COUNT(*) FROM evidence GROUP BY 1").fetchall()))
print("\nÉconomie unitaire SHOWER (ESTIMATE; CPA=$38.99 médiane Triple Whale; frais Shopify 2.9%+$0.30; COGS+port = HYPOTHESIS):")
for price in (49,59,69):
    for cogs in (15,20,25):
        fee=price*.029+.30; m1=price-fee-cogs-38.99
        r=25; rm=r-(r*.029+.30)-8  # recharge $25, COGS+port $8 HYPOTHESIS
        print(f"  prix ${price} coût ${cogs}: 1re commande {m1:+.2f} | +2 recharges {m1+2*rm:+.2f} | seuil CPA ${price-fee-cogs:.2f}")
