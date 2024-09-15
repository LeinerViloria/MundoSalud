import os
from typing import List

# Obtener la ruta del directorio actual
current_directory = os.path.dirname(os.path.abspath(__file__))

def getFiles() -> List[str]:
    all_files = os.listdir(current_directory+'/source')
    xlsx_files = [f for f in all_files if f.endswith('.xlsx')]
    return xlsx_files