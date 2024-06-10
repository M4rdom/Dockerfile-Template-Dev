import Docker_Instruction_Placer.DockerfileContent as df

def place_FROM(image:str,platform:str,tag_digest:str,as_name:str):

    """
    Esta función coloca la instrucción FROM en el Dockerfile.
    FROM Description:
        Create a new build stage from a base image.
    Parámetros:
        image: Nombre de la imagen base.
        platform: Plataforma de la imagen.
        tag_digest: Etiqueta o hash de la imagen.
        as_name: Nombre de la imagen.
    """
    df.Dockerfile +=  "FROM "
    if platform is not None:
        df.Dockerfile += "--platform=" + platform + " "
    df.Dockerfile += image 
    if tag_digest is not None:
        df.Dockerfile += ":" + tag_digest + " "
    else:
        df.Dockerfile += " "
    if as_name is not None:
        df.Dockerfile += "AS " + as_name
    df.Dockerfile +="\n"

def place_LABEL(keys:str,values:str):
    """
    Esta función coloca la instrucción LABEL en el Dockerfile.
    EXPOSE Description:
        Add metadata to an image.
    Parámetros:
        keys: Lista de claves.
        values: Lista de valores.
    """
    df.Dockerfile += "LABEL "
    for key,value in zip(keys,values):
        df.Dockerfile += key + "=" + value + " "
    df.Dockerfile +="\n"

def place_EXPOSE(port:str,protocol:str):
    """
    Esta función coloca la instrucción EXPOSE en el Dockerfile.
    EXPOSE Description:
        Add metadata to an image.
    Parámetros:
        port: Puerto informativo a exponer.
        protocol: Protocolo del puerto.
    """
    df.Dockerfile += "EXPOSE " + port + "/" + protocol
    df.Dockerfile +="\n"
    
def place_ENV(keys:str,values:str):

    """
    Esta función coloca la instrucción ENV en el Dockerfile.
    ENV Description:
        Set environment variables.
    Parámetros:
        keys: Lista de claves.
        values: Lista de valores.
    """
    df.Dockerfile += "ENV " + keys[0] + "=" + values[0] + "\n"
    for key,value in zip(keys[1:],values[1:]):
        df.Dockerfile +=  "    " + key + "=" + value
        df.Dockerfile +="\n"

def place_MAINTAINER(name:str):
    df.Dockerfile += "MAINTAINER " + name
    df.Dockerfile +="\n"

def place_WORKDIR(path:str):
    """
    Esta función coloca la instrucción WORKDIR en el Dockerfile.
    WORKDIR Description:
        Change working directory.
    Parámetros:
        path: Directorio de trabajo.
    """
    df.Dockerfile += "WORKDIR " + path
    df.Dockerfile +="\n"

def place_ARG(name:str,default_value:str):
    """
    Esta función coloca la instrucción ARG en el Dockerfile.
    ARG Description:
        Set a variable in the build stage.
    Parámetros:
        name: Nombre de la variable.
        default_value: Valor por defecto de la variable.
    """
    if default_value is None:
        df.Dockerfile += "ARG " + name + "\n"
    else:
        df.Dockerfile += "ARG " + name + "=" +default_value
    df.Dockerfile +="\n"

def place_CMD_exec_form(executable:str,parameters:str):
    """
    Esta función coloca la instrucción CMD en el Dockerfile bajo la forma Exec Form.
    CMD Description:
        Specify default commands.
    Parámetros:
        executable: Ejecutable a correr.
        parameters: Lista de parámetros.
    """
    if executable is None: #(exec form, as default parameters to ENTRYPOINT)
        df.Dockerfile += "CMD " + '['
        for parameter in parameters[:-1]:
            df.Dockerfile += '"' + parameter + '",'
        df.Dockerfile += '"' + parameters[-1] + '"]' 
    else: #Most Cases
        df.Dockerfile += "CMD " + '["' + executable + '",'
        for parameter in parameters[:-1]:
            df.Dockerfile += '"' + parameter + '",'
        df.Dockerfile += '"' + parameters[-1] + '"]'
    df.Dockerfile +="\n"

def place_CMD_shell_form(command:str,parameters:str):
    """
    Esta función coloca la instrucción CMD en el Dockerfile bajo la forma Shell Form.
    CMD Description:
        Specify default commands.
    Parámetros:
        command: Comando a correr.
        parameters: Lista de parámetros.
    """
    df.Dockerfile += "CMD " + command + " "
    for parameter in parameters:
        df.Dockerfile += parameter + " "
    df.Dockerfile +="\n"         

def place_COPY(options:str,src:str,dst:str):
    """
    Esta función coloca la instrucción COPY en el Dockerfile.
    COPY Description:
        Copy files and directories.
    Parámetros:
        options: Lista de opciones.
        src: Archivo o directorio de origen.
        dst: Directorio de destino.
    """
    df.Dockerfile += "COPY "
    for option in options:
        df.Dockerfile += option + " "
    df.Dockerfile += src + " " + dst
    df.Dockerfile +="\n"

def place_ADD(options:str,srcs:str,dst:str):
    """
    Esta función coloca la instrucción ADD en el Dockerfile sin espacios en srcs y dst.
    ADD Description:
        Copy files and directories.
    Parámetros:
        options: Lista de opciones.
        srcs: Lista de archivos o directorios de origen.
        dst: Directorio de destino.
    """
    df.Dockerfile += "ADD "
    if options is None:
        pass
    else:
        for option in options:
            df.Dockerfile += option + " "
    for src in srcs:
        df.Dockerfile += src + " "
    df.Dockerfile += dst
    df.Dockerfile +="\n"

def place_ADD_whitespace_form(options:str,srcs:str,dst:str):
    """
    Esta función coloca la instrucción ADD en el Dockerfile con espacios en srcs y dst.
    ADD Description:
        Add local or remote files and directories.
    Parámetros:
        options: Lista de opciones.
        srcs: Lista de archivos o directorios de origen.
        dst: Directorio de destino.
    """
    df.Dockerfile += "ADD "
    if options is None:
        pass
    else:
        for option in options:
            df.Dockerfile += option + " "
    for src in srcs:
        df.Dockerfile += '"' + src + '"' + " "
    df.Dockerfile += '"'+dst+'"'
    df.Dockerfile +="\n"

def place_HEALTHCHECK(options:str,command:str):
    """
    Esta función coloca la instrucción HEALTHCHECK en el Dockerfile.
    HEALTHCHECK Description:
        Set a health check instruction.
    Parámetros:
        options: Lista de opciones.
        command: Comando a correr.
    """
    if options is None or command is None:
        df.Dockerfile += "HEALTHCHECK NONE"
    else:
        df.Dockerfile += "HEALTHCHECK "
        for option in options:
            df.Dockerfile += option + " "
        df.Dockerfile += "CMD "+command 
    df.Dockerfile +="\n"
        
def place_ENTRYPOINT_exec_form(executable:str,parameters:str):
    """
    Esta función coloca la instrucción ENTRYPOINT en el Dockerfile bajo la forma Exec Form.
    ENTRYPOINT Description:
        Configure a container that will run as an executable.
    Parámetros:
        executable: Ejecutable a correr.
        parameters: Lista de parámetros.
    """
    df.Dockerfile += 'ENTRYPOINT ["'+executable+'", '
    for parameter in parameters[:-1]:
        df.Dockerfile += '"' + parameter + '", '
    df.Dockerfile += '"' + parameters[-1] + '"]'
    df.Dockerfile +="\n"

def place_ENTRYPOINT_shell_form(command:str,params:str):
    """
    Esta función coloca la instrucción ENTRYPOINT en el Dockerfile bajo la forma Shell Form.
    ENTRYPOINT Description:
        Configure a container that will run as an executable.
    Parámetros:
        command: Comando a correr.
        params: Lista de parámetros.
    """
    df.Dockerfile += "ENTRYPOINT " + command + " "
    for param in params:
        df.Dockerfile += param + " "
    df.Dockerfile +="\n"

def place_ONBUILD(instruction:str):
    """
    Esta función coloca la instrucción ONBUILD en el Dockerfile.
    ONBUILD Description:
        Add a trigger instruction.
    Parámetros:
        instruction: Instrucción a ejecutar.
    """
    df.Dockerfile += "ONBUILD " + instruction
    df.Dockerfile +="\n"

def place_STOPSIGNAL(signal:str):
    """
    Esta función coloca la instrucción STOPSIGNAL en el Dockerfile.
    STOPSIGNAL Description:
        Specify the system call signal for exiting a container.
    Parámetros:
        signal: Señal a enviar.
    """
    df.Dockerfile += "STOPSIGNAL " + signal
    df.Dockerfile +="\n"

def place_SHELL(shell:str,parameters:str):
    """
    Esta función coloca la instrucción SHELL en el Dockerfile.
    SHELL Description:
        Set the default shell of an image.
    Parámetros:
        shell: shell a definir ej:powershell,sh,cmd... .
        parameters: Lista de parámetros.
    """
    df.Dockerfile += 'SHELL ["'+shell+'", '
    for parameter in parameters[:-1]:  
        df.Dockerfile += '"' + parameter + '", '
    df.Dockerfile += '"' + parameters[-1] + '"]'
    df.Dockerfile +="\n"

def place_RUN_exec_form(options:str,commands:str):
    """
    Esta función coloca la instrucción RUN en el Dockerfile bajo la forma Exec Form.
    RUN Description:
        Execute build commands.
    Parámetros:
        options: Lista de opciones.
        commands: Lista de comandos.

    """
    df.Dockerfile += "RUN "
    if options is None:
        df.Dockerfile += "["
    else:
        for option in options:
                df.Dockerfile += option + " ["
    for command in commands[:-1]:
        df.Dockerfile +='"'+ command +'",'
    df.Dockerfile += '"'+ commands[-1] + '"]'
    df.Dockerfile +="\n"

def place_RUN_shell_form(options:str,commands:str):
    """
    Esta función coloca la instrucción RUN en el Dockerfile bajo la forma Shell Form.
    RUN Description:
        Execute build commands.
    Parámetros:
        options: Lista de opciones.
        commands: Lista de comandos.
    """
    df.Dockerfile += "RUN "
    if options is None:
        pass
    else:
        for option in options:
                df.Dockerfile += option + " "
    for command in commands:
        df.Dockerfile +=command +' '
    df.Dockerfile +="\n"
    
def place_USER(user:str,group:str):
    """
    Esta función coloca la instrucción USER en el Dockerfile.
    USER Description:
        Set the user or UID to use when running the image.
    Parámetros:
        user: Usuario.
        group: Grupo.
    """
    df.Dockerfile += "USER " + user
    if group is not None:
        df.Dockerfile += ":" + group
    else:
        pass
    df.Dockerfile +="\n"

def place_VOLUME(mount_points:str):
    """
    Esta función coloca la instrucción VOLUME en el Dockerfile.
    VOLUME Description:
        Create volume mounts.
    Parámetros:
        mount_points: Lista de puntos de montaje.
    """
    df.Dockerfile += "VOLUME " 
    for mount_point in mount_points:
        df.Dockerfile += mount_point + " "
    df.Dockerfile +="\n"
