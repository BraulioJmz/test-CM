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
    return df["Edad"].min(), df["Edad"].max()

if __name__ == "__main__":
    print("Demo CM solo con pandas v1.0.0")
    tabla = crear_tabla()
    print("\nTabla de estudiantes:")
    print(tabla)

    print("\nPromedio de edades:", promedio_edades(tabla))
