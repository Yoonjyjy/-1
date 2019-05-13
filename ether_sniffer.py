import os
import socket
import argparse
import struct

ETH_P_ALL = 0x0003
ETH_SIZE = 14

def dumpcode(buf):
    print('\n\nRaw Data')
    print("%7s"% "offset ", end='')

    for i in range(0, 16):
        print("%02x " % i, end='')
 
        if not (i%16-7):
            print("- ", end='')

    print("")
 
    for i in range(0, len(buf)):
        if not i%16:
            print("0x%04x" % i, end= ' ')

        print("%02x" % buf[i], end= ' ')

        if not (i % 16 - 7):
            print("- ", end='')

        if not (i % 16 - 15):
            print(" ")

    print("\n\n")

def ip_header_print(data):
    ip_version = struct.unpack('!B', data[ETH_SIZE:ETH_SIZE+1])
    ip_header_length = ""
    ip_header_length = str(hex(ip_version[0]))
    length_header = int(ip_header_length[3]) * 4
    ip_header = make_ip_header(data[ETH_SIZE:ETH_SIZE+length_header])
    for item in ip_header.items():
        print('{0} : {1}'.format(item[0], item[1]))

def sniffing(nic):
    if os.name == 'nt':
        address_familiy = socket.AF_INET
        protocol_type = socket.IPPROTO_IP

    else:
        address_familiy = socket.AF_PACKET
        protocol_type = socket.ntohs(ETH_P_ALL)

    with socket.socket(address_familiy, socket.SOCK_RAW, protocol_type) as sniffe_sock:
        sniffe_sock.bind((nic, 0))

        if os.name == 'nt':
            sniffe_sock.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
            sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

        while True :    
            global cnt 
            print('[%d] IP_PACKET----------------------------------------' % cnt)   
            data, _ = sniffe_sock.recvfrom(65535)
            ethernet_type_check = struct.unpack('!H', data[12:ETH_SIZE])
            if ethernet_type_check[0] == 2048 :
                ethernet_header = make_ethernet_header(data[:ETH_SIZE])

                for item in ethernet_header.items():
                    print('{0} : {1}'.format(item[0], item[1]))

                ip_header_print(data)
                dumpcode(data)

                if os.name == 'nt':
                    sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
                cnt = cnt + 1

            else:
                continue

def make_ethernet_header(raw_data):
    ether = struct.unpack('!6B6BH', raw_data)
    print('\n\nETHERNET HEADER')
    return {'[dst]':'%02x:%02x:%02x:%02x:%02x:%02x' % ether[:6],
            '[src]':'%02x:%02x:%02x:%02x:%02x:%02x' % ether[6:12],
            '[ether_type]':ether[12]}

def make_ip_header(raw_data):
    ip = struct.unpack('!BBHHBBBBH4B4B', raw_data)
    print('\n\nIP HEADER')
    version_ip= ""
    version_ip = str(hex(ip[0]))
    version = int(version_ip[2])
    header_length = int(version_ip[3])
    return{'[version]':'%x' % version,
            '[header_length]':'%x' % header_length,
            '[tos]':'%x' % ip[1],
            '[total_length]':'%d' % ip[2],
            '[id]':'%d' % ip[3],
            '[flag]':'%x' % ip[4],
            '[offset]':'%x' % ip[5],
            '[ttl]':ip[6],
            '[protocol]':ip[7],
            '[checksum]':ip[8],
            '[src]':'%d:%d:%d:%d' % ip[9:13],
            '[dst]':'%d:%d:%d:%d' % ip[13:17]}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is a simpe packet sniffer')
    parser.add_argument('-i', type=str, required=True, metavar='NIC name', help='NIC name')
    args = parser.parse_args()

    cnt = 1

    while True: 
        sniffing(args.i)
