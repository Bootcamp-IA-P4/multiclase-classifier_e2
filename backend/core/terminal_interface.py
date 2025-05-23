from models.schemas import PredictionInput
from services.translations_service import get_feature_descriptions, get_feature_translations

class TerminalInterface:
    def __init__(self, model):
        self.model = model
        self.translations = get_feature_translations()
        self.descriptions = get_feature_descriptions()

    def collect_input(self):
        print("\n=== Evaluación de Riesgo Cardiovascular ===")
        user_data = {}
        
        for feature in self.model.feature_names_in_:
            esp_name = self.translations.get(feature, feature)
            desc = self.descriptions[feature]
            
            print(f"\n{esp_name}: {desc['description']}")
            
            if desc["type"] == "categorical":
                print("Opciones válidas:")
                for val, label in desc["values"].items():
                    print(f"  {val}: {label}")
                value = input("Seleccione: ")
                while value not in desc["values"]:
                    print("¡Opción inválida!")
                    value = input("Seleccione: ")
            else:
                value = input(f"Ingrese valor ({desc['range'][0]} a {desc['range'][1]}): ")
                while not desc['range'][0] <= float(value) <= desc['range'][1]:
                    print("¡Valor fuera de rango!")
                    value = input(f"Ingrese valor ({desc['range'][0]} a {desc['range'][1]}): ")
            
            user_data[feature] = float(value) if desc["type"] == "float" else value
        
        return PredictionInput(**user_data)

    def run(self):
        from services.model_service import make_prediction
        user_input = self.collect_input()
        result = make_prediction(user_input)
        
        print("\n=== Resultado ===")
        print(f"Riesgo: {'ALTO' if result['prediction'] else 'BAJO'}")
        print(f"Probabilidad: {result['probability']:.1%}")
