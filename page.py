import os
os.system("git pull")
logo="""
╔═╗╔═╗╔═╗╔═╗╔═╗
╠═╝╠═╣║ ╦║╣ ╚═╗
╩  ╩ ╩╚═╝╚═╝╚═╝     Author : ALi Koja"""
def logox():
    os.system('clear')
    print(logo)
    print(50*'=')
def main():
    logox()
    print("\tMAIN MENU")
    print("[1] Create Pages")
    print("[2] Follow Pages")
    des=input("Choice :")
    if '1' in des:
        os.system("chmod 777 regpage && ./regpage")
    elif '2' in des:
        os.system("chmod 777 follow && ./follow")
    else:
        exit("Choose 1 or 2")
main()