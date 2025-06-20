# %%
import pandas as pd
# Nombre del Archvivo de excel de entrada y salida
Archivo_entrada = '1_BaseDatos_SRI.xlsx'
Hoja_entrada_1 = 'Hoja1'
df_data = pd.read_excel(Archivo_entrada, sheet_name=Hoja_entrada_1)
# Limpiar nombres de columnas
df_data.columns = df_data.columns.str.replace('\n', '').str.strip()
# Definir variables
df_data['RUC'] = pd.to_numeric(df_data['RUC'], errors='coerce').fillna(0).astype(int)
df_data['RAZON SOCIAL'] = df_data['RAZON SOCIAL'].astype(str)
df_data['CALIFICACION'] = df_data['CALIFICACION'].astype(str)
# Quitar los saltos de linea
df_data['CALIFICACION'] = df_data['CALIFICACION'].str.replace(r'[\n\r]+', ' ', regex=True)
#df_data.head(5)

# %%
# Solicitar el RUC al usuario y seguir solicitando hasta que ingrese 'fin'
while True:
    print('\n**************************************************************')
    RUC = input("Ingrese un RUC o 'fin' para terminar: ")

    # Verificar si el usuario quiere terminar el programa
    if RUC.lower() == 'fin':
        break

    # Verificar si el RUC ingresado tiene 12 o 13 dígitos
    if (RUC.isdigit() and len(RUC) == 12) or (RUC.isdigit() and len(RUC) == 13):
        # Buscar el RUC en el DataFrame
        resultado = df_data[df_data['RUC'] == int(RUC)]
        
        if not resultado.empty:
            # Imprimir solo los valores de las columnas 'RAZON SOCIAL' y 'CALIFICACION'
            for idx, fila in resultado.iterrows():
                print(f"RAZON SOCIAL: {fila['RAZON SOCIAL']}, \nCALIFICACION: {fila['CALIFICACION']}")
        else:
            print(f"El RUC: {RUC}, no pertenece a ninguna calificación.")
    else:
        print("El RUC ingresado no es válido. Asegúrese que ingresó correctamente.")




