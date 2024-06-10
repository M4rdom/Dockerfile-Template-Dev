import Docker_Instruction_Placer.DockerfileContent as df 
import Dockerfile_Instruction_Driver as ins
import file_manager as fm


def main():
    #ins.place_FROM("ubuntu",None,None,None,None)
    #ins.place_EXPOSE("80","tcp")
    #ins.place_ENV(["hello","hi"],["hello","hi"])
    #ins.place_HEALTHCHECK(["--interval=DURATION","--start-period=DURATION"],"pwd")
    #ins.place_ENTRYPOINT_exec_form("ls",["-a","-d"])
    #ins.place_ENTRYPOINT_shell_form("ls",["-a","-d"])
    #ins.place_LABEL(["hello","hello"],["hello","hello"])
    #ins.place_ADD(None,["text1.txt","text2.txt"],"home")
    #ins.place_ADD(["--keep-git-dir","--checksum"],["text1.txt","text2.txt"],"home")
    #ins.place_ADD_whitespace_form(None,["text1.txt","text2.txt"],"home")
    #ins.place_ADD_whitespace_form(["--keep-git-dir","--checksum"],["text1.txt","text2.txt"],"home")
    #ins.place_CMD_exec_form("ls",["-a","b"])
    #ins.place_CMD_exec_form(None,["-a","b"])
    #ins.place_CMD_shell_form("ls",["-a","b"])
    #ins.place_SHELL("cmd",["-a","-d","-U"])
    #ins.place_SHELL("cmd",["args1","args2"])
    #ins.place_RUN_exec_form(["--mount=[type=TYPE]"],["ls -a","pwd"])
    #ins.place_RUN_exec_form(None,["ls -a","pwd"])
    #ins.place_RUN_shell_form(["--mount=[type=TYPE]"],["ls -a","pwd"])
    #ins.place_RUN_shell_form(None,["ls -a","pwd"])


    ins.place_FROM("ubuntu",None,None,None)
    ins.place_FROM("ubuntu",None,None,None)
    print(df.Dockerfile)
    fm.create_file()
    fm.write_file() 






if __name__ == "__main__":
    main()