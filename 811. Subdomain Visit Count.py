cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
subdomain_count = {}

for cp in cpdomains:
    count, domains = cp.split()
    subdomains = domains.split('.')
    for i in range(len(subdomains)):
            subdomain = ".".join(subdomains[i:])
            if subdomain in subdomain_count:
                subdomain_count[subdomain] += int(count)
            else:
                subdomain_count[subdomain] = int(count)
    
result = []
for subdomain, count in subdomain_count.items():
    result.append(str(count) + " " + subdomain)


print(result)