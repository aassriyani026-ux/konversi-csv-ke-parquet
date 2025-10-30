import pandas as pd
import os

csv_file = "DATA_PENJUALAN.csv"
parquet_file = "DATA_PENJUALAN.parquet"

df = pd.read_csv(csv_file)

df.to_parquet(parquet_file, index=False)

csv_size = os.path.getsize(csv_file)
parquet_size = os.path.getsize(parquet_file)
ratio = csv_size / parquet_size if parquet_size > 0 else 0

print(f"Ukuran CSV: {csv_size/1024:.2f} KB")
print(f"Ukuran Parquet: {parquet_size/1024:.2f} KB")
print(f"Parquet lebih kecil sekitar: {ratio:.1f}x")
