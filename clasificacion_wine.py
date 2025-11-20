
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

# Carga del dataset
wine = load_wine()
X, y = wine.data, wine.target

# Se dividen los datos (80% entrenamiento, 20% prueba)
# Se usa random_state=42 y stratify=y para reproducibilidad y equilibrio de clases
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Clasificador con max_depth=2 (para reglas interpretables)
tree = DecisionTreeClassifier(max_depth=2, random_state=42)
tree.fit(X_train, y_train)

# 1. Mostrar las reglas simbólicas aprendidas
print("--- Reglas del Árbol de Decisión (max_depth=2) ---")
# Usamos class_names para que las clases sean más legibles
rules = export_text(tree, feature_names=wine.feature_names, class_names=wine.target_names)
print(rules)

# 2. Evaluar la precisión del modelo en los datos de prueba
accuracy = tree.score(X_test, y_test)
print(f"\nPrecisión en datos de prueba: {accuracy:.4f}")
