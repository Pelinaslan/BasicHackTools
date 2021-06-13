import os
os.system("apt-get install figlet")
os.system("apt-get install nmap")
os.system("clear")
os.system("figlet PORT SCANNER")

print("""
Welcome to Port Scanner App
Please select an option:
1) Quick scan
2) Learn about service and version
3) Learn about the operating system
4) Deep search (requires proxy)
""")

transactionnum = input("Enter the transaction number: ")

if(transactionnum == "1"):
    targetIp = input("Enter the target Ip: ")
    os.system("nmap " + targetIp)

elif(transactionnum == "2"):
    targetIp = input("Enter the target Ip: ")
    os.system("nmap -sS -sV " + targetIp)

elif(transactionnum == "3"):
    targetIp = input("Enter the target Ip: ")
    os.system("nmap -O " + targetIp)

elif(transactionnum == "4"):
    targetIp = input("Enter the target Ip: ")
    proxy1 = input("Enter your proxy addresses: ")
    os.system("nmap -Pn " + targetIp + " -sV -sS -v -T4 -O --proxy " + proxy1)