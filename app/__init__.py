import os
import importlib

# Carrega automaticamente todos os módulos na pasta models
models_dir = os.path.dirname(__file__)
for module_name in os.listdir(models_dir):
    if module_name.endswith(".py") and module_name != "__init__.py":
        module_name = module_name[:-3]  # Remove o sufixo '.py'
        try:
            importlib.import_module(f"app.models.{module_name}")
        except ModuleNotFoundError as e:
            print(f"Erro ao importar o módulo {module_name}: {e}")
