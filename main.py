#import Docker_Instruction_Placer.DockerfileContent as df 
#import Docker_Instruction_Placer.Dockerfile.Dockerfile_Instruction_Driver as ins
#import file_manager as fm

from jinja2 import Environment, FileSystemLoader
import json

def main():
    
    # Configurar Jinja2 para cargar la plantilla desde la carpeta de plantillas
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    
    # Cargar la plantilla desde la carpeta de plantillas
    Dockerfile_Template = env.get_template('Frontend/Frontend.jinja') # <-----------------------------------Para cambiar plantilla

    # Definir el contexto para la plantilla, El fichero JSON para la configuración de la plantilla
    #with open('configurations/FrontEnd/Angular_Nginx.json') as f: # <----------------------------------------Para cambiar configuración
    with open('configurations/FrontEnd/Angular_Node_js.json') as f: # <----------------------------------------Para cambiar configuración
      Configuracion = json.load(f)
      Configuracion = Configuracion.get('config') # Se obtiene el diccionario de configuración
      #print(Configuracion)

    # Renderizar la plantilla con el contexto
    output = Dockerfile_Template.render(Configuracion)

    # Mostrar la salida
    print(output)


if __name__ == "__main__":
    main()