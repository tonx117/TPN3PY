import pandas as pd

# Carga de datos
data =  [19, 29, 19, 22, 23, 19, 30, 19, 19, 19, 20, 20, 20, 18, 22, 19, 34, 34, 21, 21, 22, 28, 29, 19, 20, 19, 25, 28, 21, 22]


# Función de análisis matemático
def analisis_estadistico(data):
    
    # Crea un DataFrame a partir de la lista de datos
    data_frame = pd.DataFrame(data, columns=['Edad'])
    # Verifica si el DataFrame está vacío
    if data_frame.empty:
        print("No se encontraron edades para realizar el análisis.")
        return None
    
    # Calcula la frecuencia absoluta (fi) de cada valor en el DataFrame
    fi = data_frame['Edad'].value_counts().sort_index().tolist()

    # Realiza los cálculos si 'fi' no está vacía
    if fi:
        # Creación de un nuevo DataFrame para los cálculos
        calculations_df = pd.DataFrame({
            'Edad': range(min(data_frame['Edad']), min(data_frame['Edad']) + len(fi)),
            'fi': fi
        })

        
        # Realiza los cálculos estadísticos
        calculations_df["Fi"] = calculations_df["fi"].cumsum()
        calculations_df["ri"] = calculations_df["fi"] / calculations_df["fi"].sum()
        calculations_df["Ri"] = calculations_df["ri"].cumsum()
        calculations_df["pi%"] = calculations_df["ri"] * 100
        calculations_df["Pi%"] = calculations_df["pi%"].cumsum()

        # Print de los cálculos hechos
        print(calculations_df)

        # Copia al portapapeles los cálculos
        calculations_df.to_clipboard()
    else:
        print("No se encontraron edades para realizar el análisis.")
# Llamada a la función
analisis_estadistico(data)