import socket
import struct
import argparse

def make_ip_header(des_ip) :
    version = 4
    header_length = 5
    tos = 0
    total_length = 0
    id_ = 0
    flag_offset = 0
    ttl = 250
    protocol = socket.IPPROTO_TCP
    checksum = 0
    src = 0
    dst = socket.inet_aton (des_ip)

    ip_ver_hl = (version << 4) + header_length 

    ip_header = struct.pack('!BBHHHBBH4s4s', ip_ver_hl, tos, total_length, id_, flag_offset, ttl, protocol, checksum, bytes(src, 'utf-8', bytes(dst, 'utf-8'))

    return ip_header

def make_icmp_header() :
    type_ = 8
    code = 0
    checksum = 0
    id_ = 0
    sequence_number = 0
    data = 'haha'

    icmp_header = struct.pack('!BBHHH2s', type_ , code , checksum , id_ , sequence_number , data.encode())
   
    for x in struct.unpack('!5H', icmp_header) :
        checksum += x

        if checksum >  0xffff :
            checksum = (checksum & 0xffff) + (checksum >> 16)

    checksum = ~checksum & 0xFFFF

    checksum = struct.pack('!H', checksum)
    icmp_header = icmp_header[:2] + checksum + icmp_header[4:]

    return icmp_header

def echo_request(des_ip) :
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

    s.bind(('' , 0))
        
    try :
        des_ip = socket.gethostbyname(args.d)
    except socket.error :
        print ("Incorrect domain name")
    packet = make_ip_header(des_ip) + make_icmp_header()
    s.sendto(packet , (des_ip , 0))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='echo request packet')
    parser.add_argument('-d', type=str, required = True, help = 'IP or Domain')
    args = parser.parse_args()
    
    echo_request(args.d)