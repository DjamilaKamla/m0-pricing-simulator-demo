# M0 Pricing Simulator – Demo

Ce projet est une **démonstration simplifiée** d’un outil de simulation de prix énergétique,
inspiré des mécanismes utilisés sur les marchés de l’électricité.

L’objectif est de montrer la capacité à :
- modéliser un **prix moyen pondéré M0_site** à partir de données de production,
- comparer ce prix à un **M0_CRE** de référence,
- analyser la **déviation** entre les deux,
- produire un **output exploitable pour une réflexion business** (risque, marge, stratégie).

⚠️ Toutes les données sont **fictives**.  
Ce projet ne reproduit aucun outil ni script d’entreprise.

---

## 1. Contexte

Sur le marché de l’électricité, on compare souvent :
- un prix de référence réglementaire (ex : M0_CRE),
- un prix moyen pondéré par la production réelle (M0_site),

afin d’évaluer :
- les **écarts de prix**,
- les **risques d’équilibrage**,
- les **opportunités de marge**.

---

## 2. Contenu

Le script `m0_pricing_demo.py` :

1. Génère des séries temporelles fictives :
   - production (MWh),
   - prix spot (€/MWh),
   - M0_CRE (référence constante ou légèrement variable).

2. Calcule :
   - le **M0_site** (prix spot pondéré par la production),
   - la **déviation = M0_site – M0_CRE**.

3. Affiche :
   - un résumé numérique,
   - une visualisation simple (évolution M0_site vs M0_CRE),
   - une interprétation business;

---

## 3. Usage

```bash
python m0_pricing_demo.py

