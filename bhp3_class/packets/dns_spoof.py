'''
    Code pilfered from thepacketgeek.com 
    https://thepacketgeek.com/scapy-p-09-scapy-and-dns/
    opcode=0 -> query, ancount=0 -> no answer count
    DNSQR -> query, DNSRR -> resource record
'''
from scapy.all import sniff, sr1, send, IP, UDP, DNS, DNSQR, DNSRR

DNS_SERVER_IP = '192.168.1.104'
BPF = f'udp dst port 53 and ip dst {DNS_SERVER_IP}'
SPOOF_NAME = 'trailers.apple.com'

def dns_responder():
 
    def forward_dns(orig_pkt):
        print(f'Forwarding: {orig_pkt[DNSQR].qname}')
        resp_pkt = IP(dst=orig_pkt[IP].src)/UDP(dport=orig_pkt[UDP].sport)/DNS()
        response = sr1(IP(dst='8.8.8.8')/UDP(sport=orig_pkt[UDP].sport)/
                    DNS(rd=1,id=orig_pkt[DNS].id,qd=DNSQR(qname=orig_pkt[DNSQR].qname)), 
                    verbose=0)
        
        resp_pkt[DNS] = response[DNS]
        send(resp_pkt, verbose=0)
        return f'Responding: {resp_pkt.summary()}'
 
    def get_response(pkt):
        if (DNS in pkt  and pkt[IP].src != DNS_SERVER_IP 
            and pkt[DNS].opcode == 0 and pkt[DNS].ancount == 0):
            if SPOOF_NAME in str(pkt['DNS Question Record'].qname):
                spoofed = IP(dst=pkt[IP].src)/UDP(dport=pkt[UDP].sport, sport=53)\
                            /DNS(id=pkt[DNS].id, ancount=1, an=DNSRR(rrname=pkt[DNSQR].qname, rdata=DNS_SERVER_IP))
                # print(spoofed.show())
                send(spoofed, verbose=0)
                return f'Spoofed DNS Response Sent: {spoofed.summary()}'
 
            else:
                return forward_dns(pkt)
 
    return get_response
 
if __name__ == '__main__':
    sniff(filter=BPF, prn=dns_responder())