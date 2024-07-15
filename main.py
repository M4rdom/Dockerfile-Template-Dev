import Docker_Instruction_Placer.DockerfileContent as df 
import Docker_Instruction_Placer.Dockerfile.Dockerfile_Instruction_Driver as ins
import file_manager as fm


def main():
    print(ins.place_FROM(image="node",tag_digest="latest"))
    print(ins.place_WORKDIR("/usr/src/app"))
    print(ins.place_COPY("./Angular_Example/package*.json","/usr/src/app"))
    print(ins.place_RUN_shell_form(["npm","install"]))
    print(ins.place_CMD_exec_form(["ng", "serve","--host", "0.0.0.0"]))




if __name__ == "__main__":
    main()