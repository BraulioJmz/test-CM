import pandas as pd

def crear_tabla():
    # Creamos una tabla simple con datos ficticios
    data = {
        "Nombre": ["Ana", "Braulio", "Carlos", "Diana"],
        "Edad": [23, 21, 25, 22],
        "Carrera": ["Informática", "Informática", "Civil", "Industrial"]
    }
    return pd.DataFrame(data)

def promedio_edades(df):
    # Calcula el promedio de la columna "Edad"
    return df["Edad"].mean()

def estadisticas_edades(df):
    # Devuelve la edad mínima y máxima
    return df["Edad"].min(), df["Edad"].max()

def ordenar_por_edad(df):
    # Ordena el DataFrame por la columna "Edad"
    return df.sort_values(by="Edad")

if __name__ == "__main__":
    print("Demo CM solo con pandas v1.2.0")
    tabla = crear_tabla()
    print("\nTabla de estudiantes:")
    print(tabla)

    print("\nPromedio de edades:", promedio_edades(tabla))

    edad_min, edad_max = estadisticas_edades(tabla)
    print(f"\nEdad mínima: {edad_min}, Edad máxima: {edad_max}")

    print("\nTabla ordenada por edad:")
    print(ordenar_por_edad(tabla))
