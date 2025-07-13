import matplotlib.pyplot as plt
import numpy as np
import math

# Fungsi menghitung EOQ
def hitung_eoq(D, S, H):
    return math.sqrt((2 * D * S) / H)

# Input data
D = 10000  # Permintaan tahunan
S = 100    # Biaya pemesanan
H = 2      # Biaya penyimpanan per unit per tahun

# Hitung EOQ
eoq = hitung_eoq(D, S, H)

# Rentang jumlah pemesanan (Q)
Q = np.arange(100, 5000, 50)

# Hitung biaya
ordering_cost = (D / Q) * S
holding_cost = (Q / 2) * H
total_cost = ordering_cost + holding_cost

# Plot
plt.figure(figsize=(10, 6))
plt.plot(Q, ordering_cost, label="Biaya Pemesanan", linestyle="--")
plt.plot(Q, holding_cost, label="Biaya Penyimpanan", linestyle="--")
plt.plot(Q, total_cost, label="Total Biaya", linewidth=2)

# Garis EOQ
plt.axvline(eoq, color='red', linestyle=':', label=f"EOQ = {eoq:.0f} unit")

# Label dan judul
plt.title("Model EOQ - Grafik Biaya vs Jumlah Pemesanan")
plt.xlabel("Jumlah Pemesanan (Q)")
plt.ylabel("Biaya (dalam satuan biaya)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
