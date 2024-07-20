#!/usr/bin/env python3
import os

def create_launcher(name, exec_path, icon_path, launcher_path, comment, terminal, categories, keywords, actions=None, mime_type=None):
    if os.path.isdir(launcher_path):
        raise ValueError(f"La ruta proporcionada ({launcher_path}) es un directorio. Debes proporcionar una ruta completa incluyendo el nombre del archivo .desktop.")
    
    # Agregar la extensión .desktop si no está presente
    if not launcher_path.endswith(".desktop"):
        launcher_path += ".desktop"
    
    # Verificar si el archivo ya existe
    if os.path.exists(launcher_path):
        print(f"El archivo {launcher_path} ya existe.")
        overwrite = input("¿Deseas sobrescribir el archivo? (s/n): ").strip().lower()
        if overwrite == 'n':
            new_launcher_path = input("Ingrese una nueva ruta para el archivo .desktop (incluya el nombre del archivo, la extensión .desktop se agregará automáticamente si no está presente): ")
            if not new_launcher_path.endswith(".desktop"):
                new_launcher_path += ".desktop"
            return create_launcher(name, exec_path, icon_path, new_launcher_path, comment, terminal, categories, keywords, actions, mime_type)
        elif overwrite != 's':
            print("Opción no válida. El script se cerrará.")
            return

    # Crear el contenido del archivo .desktop
    content = f"""
    [Desktop Entry]
    Version=1.0
    Type=Application
    Name={name}
    Exec={exec_path}
    Icon={icon_path}
    Comment={comment}
    Terminal={terminal}
    Categories={categories}
    Keywords={keywords}
    """
    
    if actions:
        content += f"Actions={actions}\n"
    
    if mime_type:
        content += f"MimeType={mime_type}\n"
    
    content += """
    # Para todos los usuarios, coloca el archivo en:
    # /usr/share/applications/

    # Para el usuario actual, coloca el archivo en:
    # ~/.local/share/applications/
    """
    
    with open(launcher_path, 'w') as file:
        file.write(content.strip())
    
    # Asegurar que el archivo .desktop sea ejecutable
    os.chmod(launcher_path, 0o755)

print("name: El nombre del lanzador.")
name = input("Ingrese el nombre de la aplicación: ")
print("exec_path: La ruta al ejecutable.")
exec_path = input("Ingrese la ruta al ejecutable: ")
print("icon_path: La ruta al icono.")
icon_path = input("Ingrese la ruta al icono: ")
print("launcher_path: La ruta donde se guardará el archivo .desktop que corresponde a la aplicacion, RESPETE la mayuscula si contiene (incluya el nombre del archivo, la extensión .desktop se agregará automáticamente si no está presente).")
launcher_path = input("Ingrese la ruta donde se guardará el archivo .desktop: ")
print("comment: Una breve descripción de la aplicación.")
comment = input("Ingrese una breve descripción de la aplicación: ")
print("terminal: ¿Debe ejecutarse en un terminal? (true/false)")
terminal = input("¿Debe ejecutarse en un terminal? (true/false): ")
print("categories: Categorías a las que pertenece la aplicación, separadas por punto y coma (;).")
categories = input("Ingrese las categorías, separadas por punto y coma (;): ")
print("keywords: Palabras clave para la búsqueda, separadas por punto y coma (;).")
keywords = input("Ingrese las palabras clave, separadas por punto y coma (;): ")

print("actions: Acciones adicionales para la aplicación, separadas por punto y coma (;). (Opcional)")
actions = input("Ingrese las acciones adicionales (deje vacío si no aplica): ")

print("mime_type: Tipo MIME que la aplicación maneja, separada por punto y coma (;). (Opcional)")
mime_type = input("Ingrese el tipo MIME (deje vacío si no aplica): ")

try:
    create_launcher(name, exec_path, icon_path, launcher_path, comment, terminal, categories, keywords, actions, mime_type)
    print(f"Lanzador creado exitosamente en {launcher_path}")
    print("\nPara todos los usuarios, coloca el archivo en:")
    print("/usr/share/applications/")
    print("\nPara el usuario actual, coloca el archivo en:")
    print("~/.local/share/applications/")
    print("\nPara agregar el lanzador al bash profile, agrega la siguiente línea a tu archivo ~/.bashrc o ~/.bash_profile:")
    print(f'export PATH="$PATH:{os.path.dirname(launcher_path)}"')
except ValueError as e:
    print(e)

