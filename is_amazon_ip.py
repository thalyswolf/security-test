
ips = [
    'x.x.x.x'
]



from ipwhois import IPWhois

for ip in ips:
    print "processing {}".format(ip)
    obj = IPWhois(ip)

    if 'Amazon' in str(obj.lookup()):
        print ip