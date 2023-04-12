# Todo

## Reunión Bobi (03/02/2023)

### Cosas Previas mias

* [X] Poner versión de datos tratados
* [X] Borrar filas si son pocos y son pocas columnas (<8)

### Cosas a Desarrollar

1. [X] Crear pipeline para tratar los datos (one hot encoding y normalizar)
2. [X] Crear pipeline para cada tipo de modelo (uno con OHE y otro sin), y añadir el predecir dentro del pipeline
3. [X] Poder avisar que tarda en entrenar modelos más complejos
4. [X] Para hyperparameters tuning utilizar optuna o GridSearch

## Reunión Bobi (08/03/2023)

* [X] Quitar 1 en OHE
* [X] Añadir el flujo de tontos que te entrene todos los modelos con esos datos y te haga solo la partición
* [X] Si no se está en el flujo de los tontos, poner en "Entrenar con mis parámetros", "MODO EXPERTO"
* [X] Añadir explicaciones a la matriz de confusión (qué es)
* [X] Partir las visualizaciones en 3 (dejar las de optuna, y 1) poner una normal (matriz de confusión explicada, plot dinámico y métricas del modelo en formato tabla), y 2) otra modo experto (ROC-AUC y Regiones de decisión))
* [X] En Visualizar Modelo, cambiar por Modelo Resultante
* [X] En Regresión, utilizar como mejor métrica MSE
* [X] Añadir en clasificación Random Forest y Regresión Lineal Multivariable (3 modelos)
* [X] En Regresión añadir (KNN, Elastic Net, Perceptrón Multicapa, Random Forest)
* [X] En las visualizaciones de Regresión, poner la distribución de error y encima de esa, una normal para demostrar que más o menos es una normal

## Cosas a trabajar

* [X] En visualización hay que poner 2 tipos de visualización. Primero visualizar importancia de hiperparámetros si se han elegido con optuna. En segundo lugar, cosas como auc y classification report
* [X] En tratar NAs tengo que recomendar eliminar columnas si el valor máximo es inferior al 15%
* [X] En tratar NAs tengo que eliminar columnas si solo hay 1 valor
* [X] En la parte de visualizar el modelo de clasificación, en la gráfica de abajo izq, tengo que modificarlo para: A) Si la variable cat es la misma, que sean pie plots tantos como tipos de predicción haya, B) Si son dos las mismas numéricas, Subplot de histogramas por cada categoría
* [X] Cambiar tanto en el A) entrenamiento del modelo, como en B) la parte de predicción y visualización tanto el obtener los datos, como el predecir
* [X] En predicción poner en el confussion matrix ejes
* [X] Cambiar tipos de datos a forma más entendible
* [X] Añadir en visualización: Modelo 1: SVC y demás
* [X] Matriz de confusión en función de si está en la diagonal o no
* [X] Subir a arriba los botones de siguiente
* [X] Asumir clasificacion si son valores int y repetidos
* [X] Añadir Red Neuronal (con optuna ) y Regresion Lineal, y SVR
* [X] Poner colores distintos para clasificacion y regresion
* [X] Unificar los valores en los plots de error
* [X] Posibilidad de crear los modelos con los parámetros preestablecidos
* [ ] En redes neuronales guardar el plot del history
