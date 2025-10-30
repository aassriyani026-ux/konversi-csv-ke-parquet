import pandas as pd
import numpy as np


jumlah_baris = 1_000_000

data = {
    "ID": np.arange(1, jumlah_baris + 1),
    "Nama_Produk": np.random.choice(["Bead RG", "Bead MS", "Bead Fines", "Bead Regrind"], jumlah_baris),
    "Bulan": np.random.choice(["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"], jumlah_baris),
    "Tahun": np.random.choice([2021, 2022, 2023, 2024, 2025], jumlah_baris),
    "Kuantitas": np.random.randint(1, 500, jumlah_baris),
    "Harga": np.random.randint(50000, 60000, jumlah_baris),
}

df = pd.DataFrame(data)

nama_file = "DATA_PENJUALAN.csv"
df.to_csv(nama_file, index=False)

print(f"File '{nama_file}' berhasil dibuat dengan {jumlah_baris:,} baris.")
