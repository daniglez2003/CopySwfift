import shutil
import os
from datetime import datetime

def cSeguridad():
    # Verificar si la carpeta de destino existe, si no, crearla
    rutaAccess = r"\\192.168.1.251\Publica\Espera\backup"
    
    copia_destino = r"\\192.168.1.251\Publica\Espera\backup\copiaseguridad" #preguntar
    
    rutaAccess = os.path.join(rutaAccess, "Stammdaten.mdb")

    if not os.path.exists(copia_destino):
        os.makedirs(copia_destino)

    # Generar un nombre único para la copia de seguridad basado en la fecha y hora actual, basicamente se usa de hash
    fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Construir las rutas de destino para las copias de seguridad
    newAccess = os.path.join(copia_destino, f"AccessCopiaSeguridad_{fecha_actual}")

    try:
        # Realizar copia de seguridad
        shutil.copy2(rutaAccess, newAccess)
        return True
    except Exception as e:
        return False
  
