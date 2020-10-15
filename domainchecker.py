import whois
import sys

try:
    domain = whois.whois("usahidsolo.ac.id")
    if domain.domain_name == None:
        sys.exit(1)
except:
    print("Ooops,this domain unavailable")
else:
    print("This domain available !")
