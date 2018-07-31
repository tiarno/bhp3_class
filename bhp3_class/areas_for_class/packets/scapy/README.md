## Other stuff

res, unans = traceroute(['reachtim.com'], dport=[443], maxttl=20, retry=-2)

res.graph()

hosts = ['www.microsoft.com', 'www.cisco.com', 'www.yahoo.com', 'www.wanadoo.fr', 'www.pacsec.com']

res, unans = traceroute(hosts, dport=[80,443], maxttl=20, retry=-2)


a = Ether()/IP(dst="www.slashdot.org")/TCP()/"GET /index.html HTTP/1.0 \n\n"

hexdump(a)

a[0].pdfdump(layer_shift=1)