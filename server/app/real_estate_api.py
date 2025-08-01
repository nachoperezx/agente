# app/real_estate_api.py

import pandas as pd

# Carga los datos una vez al iniciar el módulo
sales_df = pd.read_csv("data/venta.csv")
rental_df = pd.read_csv("data/renta.csv")

def search_properties_for_sale(location: str):
    """Buscar propiedades en venta filtrando por ubicación (case insensitive)."""
    filtered = sales_df[sales_df['SUBURB'].str.contains(location, case=False, na=False)]
    results = filtered.head(5).to_dict(orient="records")
    
    return [
        {
            "id": str(i),
            "title": f"{row['BEDROOMS']}BR house in {row['SUBURB']}",
            "price": f"${row['PRICE']}",
            "neighbourhood": row['SUBURB'],
            "address": row['ADDRESS']
        }
        for i, row in enumerate(results)
    ]

def search_properties_for_rent(location: str):
    """Buscar propiedades en renta filtrando por ubicación (case insensitive)."""
    filtered = rental_df[rental_df['neighbourhood'].str.contains(location, case=False, na=False)]
    results = filtered.head(5).to_dict(orient="records")
    
    cleaned_results = []
    for i, row in enumerate(results):
        title = row['NAME']
        # Detectar NaN en título
        if not title or title != title:
            title = "Sin título"
        cleaned_results.append({
            "id": str(i + len(sales_df)),  # Id único sumando el tamaño de ventas para no solapar
            "title": title,
            "price": row['price'],
            "neighbourhood": row['neighbourhood'],
            "address": None,
        })
    return cleaned_results

def get_property_details(property_id: str):
    """Obtener detalles completos de una propiedad según el id."""
    try:
        index = int(property_id)
    except ValueError:
        return {"error": "ID inválido"}

    if index < len(sales_df):
        row = sales_df.iloc[index]
        return {
            "id": property_id,
            "title": f"{row['BEDROOMS']}BR house at {row['ADDRESS']}",
            "description": f"{row['FLOOR_AREA']} sqm, built in {row['BUILD_YEAR']}",
            "price": f"${row['PRICE']}",
            "address": row['ADDRESS'],
            "neighbourhood": row['SUBURB'],
        }
    elif index - len(sales_df) < len(rental_df):
        rental_index = index - len(sales_df)
        row = rental_df.iloc[rental_index]
        return {
            "id": property_id,
            "title": row['NAME'] if row['NAME'] == row['NAME'] else "Sin título",  # evitar NaN
            "description": f"Room type: {row.get('room type', 'N/A')}, reviews: {row.get('number of reviews', 'N/A')}",
            "price": row['price'],
            "address": row['neighbourhood'],
            "neighbourhood": row['neighbourhood'],
        }
    else:
        return {"error": "Property not found"}

