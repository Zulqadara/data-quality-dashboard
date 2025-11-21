import polars as pl

async def profile_dataset(file_path: str):
    df = pl.read_csv(file_path)

    results = []

    for col in df.columns:
        series = df[col]

        inferred_type = str(series.dtype)
        missing = series.null_count()
        unique = series.n_unique()

        results.append({
            "column_name": col,
            "inferred_type": inferred_type,
            "missing_count": missing,
            "unique_count": unique,
        })

    return {
        "row_count": df.height,
        "profile": results,
    }
