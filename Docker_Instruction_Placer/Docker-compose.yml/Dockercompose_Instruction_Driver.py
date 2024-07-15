import Docker_Instruction_Placer.DockerfileContent as df

def place_name(name:str):
    df.yamlfile+=name+":"
    df.yamlfile+="\n"

def place_service():
    df.yamlfile+="service:"
    df.yamlfile+="\n"

def place_image(image:str):
    df.yamlfile+="\t\timage: "+image
    df.yamlfile+="\n"

def place_build():
    df.yamlfile+="\t\tbuild: "
    df.yamlfile+="\n"

def place_network(networks:str):
    df.yamlfile+="\t\tnetworks:"
    df.yamlfile+="\n"
    for network in networks:
        df.yamlfile+="\t\t\t- "+network
        df.yamlfile+="\n"

def place_ports(ports:str):
    df.yamlfile+="\t\tports:"
    df.yamlfile+="\n"
    for port in ports:
        df.yamlfile+="\t\t\t- "+port
        df.yamlfile+="\n"

def place_env_file(path:str,required:str):
    df.yamlfile+="env_file: "
    df.yamlfile+="\n"
    df.yamlfile+="\t\t - path: " + path
    df.yamlfile+="\n"
    
    if required:
        df.yamlfile+="\t\t - required: true"
        df.yamlfile+="\n"
    else:
        df.yamlfile+="\t\t - required: false"
        df.yamlfile+="\n"

def place_version(version:str):
    df.yamlfile+="version: "+version
    df.yamlfile+="\n"

def place_context(path:str):
    df.yamlfile+="\t\tcontext: "+path
    df.yamlfile+="\n"

def place_dockerfile(path:str):
    df.yamlfile+="\t\tdockerfile: "+path
    df.yamlfile+="\n"

def place_dockerfile_inline(content:str):
    df.yamlfile+="\t\tdockerfile: \n"+content
    df.yamlfile+="\n"

def place_args(args:str):
    df.yamlfile+="\t\targs:"
    df.yamlfile+="\n"
    for arg in args:
        df.yamlfile+="\t\t\t- "+arg
        df.yamlfile+="\n"

def place_ssh(id:str,path:str):
    df.yamlfile+="\t\tssh: \n"
    if id is not None and path is not None:
        df.yamlfile+="\t\t\t- " + id
        df.yamlfile+="\n"
    else: 
        df.yamlfile+="\t\t\t- " + "default"
        df.yamlfile+="\n"

def place_cache_from(images:str):
    df.yamlfile+="\t\tcache_from: \n"
    for image in images:
        df.yamlfile+="\t\t\t- "+image
        df.yamlfile+="\n"

def place_extra_hosts(hostnames:str,ip_addresses:str):
    df.yamlfile+="\t\textra_hosts: \n"
    if len(hostnames)!=len(ip_addresses):
        print("Error: Number of hostnames and ip addresses do not match")
        return
    for i in range(len(hostnames)):
        df.yamlfile+="\t\t\t- "+hostnames[i]+":"+ip_addresses[i]
        df.yamlfile+="\n"

def place_privileged(privileged:str):
    df.yamlfile+="\t\tprivileged: "
    if privileged:
        df.yamlfile+="true"
    else:
        df.yamlfile+="false"
    df.yamlfile+="\n"

def place_network(network:str):
    df.yamlfile+="\t\tnetwork: "+network
    df.yamlfile+="\n"

def place_target(stage:str): #to do
    df.yamlfile+="\t\ttarget: "+stage
    df.yamlfile+="\n"

def place_secrets(path:str): #to do 
    df.yamlfile+="\t\tsecrets: \n"
    df.yamlfile+="\t\t\t- "+path
    df.yamlfile+="\n"

def place_tags(tags:str):
    df.yamlfile+="\t\ttags: \n"
    for tag in tags:
        df.yamlfile+="\t\t\t- "+tag
        df.yamlfile+="\n"