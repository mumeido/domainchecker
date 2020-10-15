import whois
import sys

try:
    domain_input = input("Input Your Domain : ")
    domain = whois.whois(domain_input)

    if domain.domain_name == None:
        sys.exit(1)
except:
    print("Ooops,this domain unavailable")
else:
    print("This domain available !")
