from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "housepricepred"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedir = filepath.parent

    if filedir != Path('.'):
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(
            f"Creating directory {filedir} for file: {filepath.name}"
        )

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath.name} already exists!")

