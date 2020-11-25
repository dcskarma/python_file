import whois

def is_reg(domain_name):

    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)


domains = [
    "google.com",
    "github.com",
    "facebook.com",
     "hhf.com"
    ]

for domain in domains:
     print(domain, "is registered" if is_reg(domain) else "is not registered")