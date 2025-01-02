import os
import shutil
from datetime import datetime

# Directorios de origen y destino
source_dir = "/home/usuario/documentos"
backup_dir = "/home/usuario/backup"

# Crear nombre de archivo de respaldo con la fecha actual
fecha = datetime.now().strftime('%Y-%m-%d')
backup_file = os.path.join(backup_dir, f"backup_{fecha}.zip")

# Comprimir el directorio en un archivo ZIP
shutil.make_archive(backup_file, 'zip', source_dir)

print(f"Copia de seguridad completada en {backup_file}")
