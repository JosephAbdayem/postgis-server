import os
import importlib

models_dir = os.path.dirname(__file__)

for module_name in os.listdir(models_dir):
    if module_name.endswith(".py") and module_name != "__init__.py":
        module_name = module_name[:-3]  # Remove o sufixo '.py'
        try:
            module = importlib.import_module(f"app.models.{module_name}")
            globals()[module_name] = module
        except ImportError as e:
            print(f"Erro ao importar o módulo {module_name}: {e}")
