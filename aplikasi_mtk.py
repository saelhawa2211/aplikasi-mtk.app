import streamlit as st
import matplotlib.pyplot as plt

def mm1_model(lmbda, mu):
    if lmbda >= mu:
        return {"error": "λ harus lebih kecil dari μ agar sistem stabil."}
    
    rho = lmbda / mu
    L = lmbda / (mu - lmbda)
    Lq = (lmbda ** 2) / (mu * (mu - lmbda))
    W = 1 / (mu - lmbda)
    Wq = lmbda / (mu * (mu - lmbda))

    return {
        "rho": round(rho, 4),
        "L": round(L, 4),
        "Lq": round(Lq, 4),
        "W": round(W, 4),
        "Wq": round(Wq, 4)
    }

# Streamlit UI
st.title("Model Antrian M/M/1")

st.markdown("""
Model ini menghitung metrik performa dari sistem antrian **M/M/1** berdasarkan:
- **λ (lambda)** = laju kedatangan
- **μ (mu)** = laju pelayanan

Masukkan nilai untuk melihat hasilnya.
""")

lmbda = st.number_input("Masukkan nilai λ (lambda)", min_value=0.0, format="%.4f")
mu = st.number_input("Masukkan nilai μ (mu)", min_value=0.0, format="%.4f")

if st.button("Hitung"):
    if lmbda == 0 or mu == 0:
        st.warning("λ dan μ harus lebih besar dari 0.")
    else:
        hasil = mm1_model(lmbda, mu)
        if "error" in hasil:
            st.error(hasil["error"])
        else:
            st.subheader("Hasil Perhitungan:")
            st.write(f"**ρ (Utilisasi):** {hasil['rho']}")
            st.write(f"**L (Rata-rata dalam sistem):** {hasil['L']}")
            st.write(f"**Lq (Rata-rata dalam antrian):** {hasil['Lq']}")
            st.write(f"**W (Waktu dalam sistem):** {hasil['W']}")
            st.write(f"**Wq (Waktu dalam antrian):** {hasil['Wq']}")

            # Visualisasi grafik batang
            st.subheader("Visualisasi Grafik")
            labels = ['L', 'Lq', 'W', 'Wq']
            values = [hasil['L'], hasil['Lq'], hasil['W'], hasil['Wq']]

            fig, ax = plt.subplots()
            bars = ax.bar(labels, values, color=['#4CAF50', '#2196F3', '#FF9800', '#E91E63'])
            ax.set_ylabel('Nilai')
            ax.set_title('Grafik Kinerja Sistem Antrian M/M/1')

            # Menampilkan nilai pada tiap batang
            for bar in bars:
                yval = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.05, round(yval, 2), ha='center', va='bottom')

            st.pyplot(fig)
