import polars as pl

async def extract_columns(file_path: str):
    df = pl.read_csv(file_path, n_rows=0)
    return df.columns
