import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

# 1. Génération de données fictives
n_hours = 24 * 30  # 1 mois horaire

time_index = pd.date_range(start="2024-01-01", periods=n_hours, freq="H")

production = np.abs(np.random.normal(loc=50, scale=10, size=n_hours))

spot_price = np.random.normal(loc=80, scale=20, size=n_hours)
spot_price = np.clip(spot_price, 0, None)  # pas de prix négatifs ici

m0_cre = 78 + np.random.normal(loc=0, scale=2, size=n_hours)

df = pd.DataFrame({
    "datetime": time_index,
    "production_MWh": production,
    "spot_price": spot_price,
    "m0_cre": m0_cre
})

# 2. Calcul du M0_site (prix moyen pondéré par la production)
df["weighted_spot"] = df["spot_price"] * df["production_MWh"]
m0_site = df["weighted_spot"].sum() / df["production_MWh"].sum()

# M0_CRE de référence sur la période (moyenne simple)
m0_cre_mean = df["m0_cre"].mean()

deviation = m0_site - m0_cre_mean

# 3. Résumé numérique
print("=== M0 Pricing Simulator – Demo ===")
print(f"M0_site (pondéré production) : {m0_site:.2f} €/MWh")
print(f"M0_CRE (référence moyenne)  : {m0_cre_mean:.2f} €/MWh")
print(f"Déviation (M0_site – M0_CRE): {deviation:.2f} €/MWh")

if deviation > 0:
    interpretation = (
        "Le prix moyen obtenu sur le site est supérieur à la référence : "
        "potentiellement une opportunité de marge, mais aussi un risque pour l’acheteur."
    )
else:
    interpretation = (
        "Le prix moyen obtenu sur le site est inférieur à la référence : "
        "situation plutôt favorable pour l’acheteur, à analyser au regard du risque."
    )

print("\nInterprétation business :")
print(interpretation)

# 4. Visualisation simple
daily = df.resample("D", on="datetime").agg({
    "spot_price": "mean",
    "m0_cre": "mean"
})

plt.figure()
plt.plot(daily.index, daily["spot_price"], label="M0_site (proxy spot moyen)")
plt.plot(daily.index, daily["m0_cre"], label="M0_CRE (référence)", linestyle="--")
plt.title("Évolution quotidienne des prix – Démo M0")
plt.xlabel("Date")
plt.ylabel("Prix (€/MWh)")
plt.legend()
plt.tight_layout()
plt.show()
