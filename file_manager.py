import os
import Docker_Instruction_Placer.DockerfileContent as df

Dockerfile_PATH = "Dockerfile" 


def write_file():
    try:
        with open(Dockerfile_PATH, 'w') as file:
            file.write(df.Dockerfile)
            file.close
    except IOError as error:
        print("Error: No se pudo escribir en el archivo:", Dockerfile_PATH , error.args)

def create_file():
    try:
        with open(Dockerfile_PATH, 'w') as file:
            file.close
    except IOError as error:
        print("Error: No se puedo crear el archivo", error.args)

def check_file():
    try:
        if os.path.exists(Dockerfile_PATH): # Verificar si el archivo existe
            pass
        else:
            raise ValueError("El programa no encuentra el archivo especificado")
        if os.access(Dockerfile_PATH, os.R_OK): # Verificar si el archivo tiene permisos de lectura
            pass
        else:
            raise ValueError("El programa no tiene permisos de lectura para el archivo especificado")
        if os.access(Dockerfile_PATH, os.W_OK): # Verificar si el archivo tiene permisos de escritura
            pass
        else:
            raise ValueError("El programa no tiene permisos de escritura para el archivo especificado")
        return
    except IOError as error:
        print(error.args)
    

def remove_dockerfile():
    try:
        if os.path.exists(Dockerfile_PATH): # Check if the file exists
            os.remove(Dockerfile_PATH) # Remove the file
            print(f"The Dockerfile {Dockerfile_PATH} has been successfully removed.")
        else:
            print(f"The Dockerfile {Dockerfile_PATH} does not exist.")
    except PermissionError:
        print(f"You do not have permission to delete the file {Dockerfile_PATH}.")
    except Exception as e:
        print(f"An error occurred while trying to delete the file: {e}")