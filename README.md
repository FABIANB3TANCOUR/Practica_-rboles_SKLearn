# Practica_-rboles_SKLearn

## Actividades:

-Desarrolla el archivo en python que genera el modelo y muestre la precisión que se consiguió  y subelo en un repositorio.

-Cambia el parámetro max_depth de DecisionTreeClassifier y observa cómo cambian las reglas del árbol.

-Prueba a entrenar el modelo sin limitar la profundidad (max_depth=None). ¿Qué notas en las reglas?

-Evalúa la precisión del modelo en los datos de prueba:
print("Precisión en datos de prueba:", tree.score(X_test, y_test))

-Genera un README en  donde coloques:

.Cuales son tus opiniones de los resultados.

.Si crees que tu base de conocimiento cumple con los requerimientos para utilizarse en un modelo de árbol de decisiones.

.Justifica el porqué sí o por qué no.

 De ser tú respuesta sí:
 
 Anota las características que tendría y las clases.
 
 De ser no:
 
 Describe qué cambio se tendrían que hacer para poder utilizarlos o de no ser posible explica si se podría usar el método de regresión. 

## Opiniones de los Resultados

Los resultados demuestran la relación entre la interpretabilidad y la precisión de un Árbol de Decisión.Modelo Superficial (max_depth=2): Es extremadamente interpretable. Podría explicarse fácilmente a un enólogo: "Si la intensidad del color es baja y el contenido de cenizas es alto, es un vino de Clase 0". Sin embargo, su precisión es ligeramente menor, dejando un $13.89\%$ de las muestras de prueba sin clasificar correctamente.Modelo Completo (max_depth=None): Logró una mayor precisión ($94.44\%$), lo cual es excelente para un modelo de producción. Sin embargo, el árbol completo genera cientos de reglas anidadas, volviéndolo casi ininteligible para un humano. Aunque este dataset es pequeño y limpio, en conjuntos de datos más grandes o con ruido, un árbol sin limitación de profundidad podría sobreajustarse fácilmente al ruido de los datos de entrenamiento.

En pocas palabras, se prefiere max_depth=2 si la explicabilidad es más importante que la máxima precisión, y max_depth=None si la precisión es el único objetivo principal.

## ¿Cumple la base de conocimiento con los requerimientos?

Sí, la base de conocimiento (Wine Dataset) cumple completamente con los requerimientos para ser utilizada en un modelo de Árbol de Decisiones (y, en general, en la mayoría de los clasificadores supervisados).

## Justificación

Un Árbol de Decisiones es un clasificador no paramétrico que se basa en la división de un espacio de características en regiones.

Requiere:

Datos Etiquetados: El conjunto de datos debe ser de aprendizaje supervisado (tener características de entrada, X, y etiquetas de salida, y). El Wine Dataset tiene las 13 características químicas (X) y las 3 clases de vino (y).

Características Numéricas (o categóricas ordenadas): Los árboles funcionan excelentemente con datos numéricos, ya que las divisiones se basan en umbrales (ej. alcohol $\le 12.8$). Las 13 características del Wine Dataset son mediciones químicas continuas (numéricas).

Clases Discretas: El objetivo es una clasificación, que requiere una variable de destino categórica o discreta. El Wine Dataset clasifica los vinos en $\mathbf{3}$ clases distintas (Clase 0, Clase 1, Clase 2).
