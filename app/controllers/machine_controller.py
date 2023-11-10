
import sklearn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from app.helpers.conexion_database import conexionSQLServer



class MachineL:
    def actualizarDatabase(self):
        '''
        return: Json: {indicar}
        '''
        try:
            # Importando funcion
            data, codigo = conexionSQLServer()
            if not data.empty:
                ruta = "./Data/data.xlsx"
                data.to_excel(ruta)

                # Trabajando con la data para actualizar el archivo de predicciones
                df = data
        
                # Define un diccionario de mapeo para los reemplazos
                mapeo_sentimientos = {'Negativo': 1, 'Neutral': 0, 'Positivo': 2}

                # Aplica el reemplazo en la columna "sentiment_analysis"
                df['num'] = df['sentiment'].replace(mapeo_sentimientos)

                data_prediccion = df[['name_categorie', 'state', 'num','business']]
                
                tuplas_unicas = data_prediccion[['name_categorie','state','num']].drop_duplicates()

                data_unicas = tuplas_unicas.reset_index(drop=True)

                # Iniciando el proceso para prediccion
                df_matrix = pd.pivot_table(data_unicas, values='num', index='name_categorie', columns='state').fillna(0)

                ratings = df_matrix.values

                ratings_train, ratings_test = train_test_split(ratings, test_size = 0.1, random_state=42)

                tmx , tmy = ratings_train.shape
                
                sim_matrix = 1 - sklearn.metrics.pairwise.cosine_distances(ratings)

                tsimx, tsimy = sim_matrix.shape
                
                print(tmx, tsimy)


                #separar las filas y columnas de train y test
                sim_matrix_train = sim_matrix[0:tmx,0:tmx]
                sim_matrix_test = sim_matrix[tmx:tsimx,tmx:tsimx]
                
                users_predictions = sim_matrix_train.dot(ratings_train) / np.array([np.abs(sim_matrix_train).sum(axis=1)]).T

                
                # Guardar el archivo .npy y df_matriz
                np.save('./Data/users_predictions.npy', users_predictions)

                df_matrix.to_pickle('./Data/df_matrix.pkl')
                return {
                    "Result": "Se realizo la actualización correctamente"
                }, codigo
            else:
                return {
                    "Result":"Error en actualización"
                }, codigo
        except Exception as e:
            return {
                "Result":f"{e}"
            }, 400

    def Recomendacion(self,categoria):
        '''
        input: Categoria
        output: Los estados recomendados segun la valoracion indicada
        '''
        try:
            # Importando datos
            
            
            valor_buscar = categoria
            
            df_matrix = pd.read_pickle('./Data/df_matrix.pkl')
            
            print(df_matrix)

            print(df_matrix)


            business_prediccion =  np.load("./Data/users_predictions.npy")

            print(business_prediccion)

            # Realizando el proceso de recomendación

            
            indice_fila = df_matrix.index.get_loc(valor_buscar)

           
            
            busines_one=business_prediccion.argsort()[indice_fila]

            
            

            nombre = []
            for i, aRepo in enumerate(busines_one[-3:]):
                
                nombre.append(df_matrix.columns[aRepo])
                
           # Ruta del archivo JSON
            ruta_json = './Data/estados.json'

            # Leer el archivo JSON
            with open(ruta_json, 'r') as archivo:
                estados = json.load(archivo)

            
            
                

            return {
                "Result": {
                            "Estado 1": estados[f"{nombre[0]}"],
                            "Estado 2": estados[f"{nombre[1]}"]
                }
            }, 200

        except Exception as e:
            return {
                "Result": f"Todavia no es posible predecir"
            },400




