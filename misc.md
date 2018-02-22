# Misc

## A collection of useful network programs
#### Ping
Send ICMP ECHO_REQUEST to network hosts.
```
$ ping -c 3 umass.edu      
  PING umass.edu (128.119.8.148) 56(84) bytes of data.
  64 bytes from netreg.oit.umass.edu (128.119.8.148): icmp_seq=1 ttl=128 time=21.8 ms
  64 bytes from netreg.oit.umass.edu (128.119.8.148): icmp_seq=2 ttl=128 time=21.5 ms
  64 bytes from netreg.oit.umass.edu (128.119.8.148): icmp_seq=3 ttl=128 time=19.7 ms
  --- umass.edu ping statistics ---
  3 packets transmitted, 3 received, 0% packet loss, time 2005ms
  rtt min/avg/max/mdev = 19.710/21.040/21.842/0.954 ms
```
#### Traceroute
Print the route packets trace to network host.
```
 $ traceroute mit.edu
   traceroute to mit.edu (23.4.118.176), 30 hops max, 60 byte packets
   1  * * *
   2  n5-rt-1-1-xe-12-0-1.gw.umass.edu (128.119.3.35)  0.727 ms  0.711 ms  0.699 ms
   3  core1-rt-et-5-2-0.gw.umass.edu (128.119.0.9)  0.688 ms  0.688 ms  0.675 ms
   4  border1-rt-xe-0-1-0.gw.umass.edu (192.80.83.102)  0.644 ms  0.634 ms  0.622 ms
   5  nox300gw1-umass-cps.nox.org (207.210.142.241)  3.581 ms  3.564 ms  3.540 ms
   6  et-7-3-0.120.rtsw.newy32aoa.net.internet2.edu (198.71.47.57)  7.770 ms  7.882 ms  7.859 ms
   7  ae-3.4079.rtsw.wash.net.internet2.edu (162.252.70.138)  13.127 ms  13.109 ms  13.086 ms
   8  ae-1.4079.sdn-sw.ashb.net.internet2.edu (162.252.70.137)  13.658 ms  13.869 ms  13.416 ms
   9  et-2-1-0.4079.rtsw.clev.net.internet2.edu (162.252.70.55)  18.688 ms  18.638 ms  18.628 ms
   10  ae-1.4079.sdn-sw.eqch.net.internet2.edu (162.252.70.131)  27.503 ms  27.579 ms  27.621 ms
   11  lo-0.8.rtr.eqch.net.internet2.edu (64.57.29.130)  27.595 ms  28.557 ms  28.545 ms
   12  162.252.69.179 (162.252.69.179)  32.320 ms  32.091 ms  31.883 ms
   13  a23-4-118-176.deploy.static.akamaitechnologies.com (23.4.118.176)  28.287 ms  28.257 ms  28.104 ms
```
#### Iperf
Perform network throughput tests.
##### Server Side
```
$ iperf -s
 ------------------------------------------------------------
 Server listening on TCP port 5001
 TCP window size: 85.3 KByte (default)
 ------------------------------------------------------------
```
##### Client Side
```
$ iperf -c 10.10.1.1
 ------------------------------------------------------------
 Client connecting to 10.10.1.1, TCP port 5001
 TCP window size: 85.0 KByte (default)
 ------------------------------------------------------------
 [  3] local 10.10.1.3 port 45368 connected with 10.10.1.1 port 5001
 [ ID] Interval       Transfer     Bandwidth
 [  3]  0.0-10.1 sec   118 MBytes  97.7 Mbits/sec
```
###### Result on the Server Side
```
------------------------------------------------------------
Server listening on TCP port 5001
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  4] local 10.10.1.1 port 5001 connected with 10.10.1.3 port 45368
[ ID] Interval       Transfer     Bandwidth
[  4]  0.0-10.3 sec   118 MBytes  95.6 Mbits/sec
```
#### Netstat
Print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.
```
$ netstat
 Active Internet connections (w/o servers)
 Proto Recv-Q Send-Q Local Address           Foreign Address         State
```
#### Tcpdump
Dump traffic from a network.
```
 $ sudo tcpdump -vvi eth1 -w dump.pcap
  tcpdump: listening on eth1, link-type EN10MB (Ethernet), capture size 262144 bytes
  Got 24
```

#### Tshark
Dump and analyze network traffic.
```
$ sudo tshark -i eth1
  Capturing on 'enp4s0'
  1 0.000000000 73.114.134.205 → 128.119.88.168 TCP 60 58360 → 22 [ACK] Seq=1 Ack=1 Win=2161 Len=0
  2 0.026339010 128.119.89.161 → 128.119.89.255 NBNS 92 Name query NB UMAOITEPO<00>
  3 0.041025838 JuniperN_a3:11:00 → Broadcast    ARP 60 Who has 128.119.91.161? Tell 128.119.91.254
  4 0.041034648 JuniperN_a3:11:00 → Broadcast    ARP 60 Who has 128.119.89.120? Tell 128.119.89.254
  ...
```

#### Dig
DNS lookup utility.
##### Query for "A" record type
```
$ dig umass.edu
                
  ; <<>> DiG 9.10.3-P4-Ubuntu <<>> umass.edu
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 45598
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

  ;; OPT PSEUDOSECTION:
  ; EDNS: version: 0, flags:; MBZ: 0005 , udp: 512
  ;; QUESTION SECTION:
  ;umass.edu.			IN	A

  ;; ANSWER SECTION:
  umass.edu.		5	IN	A	128.119.8.148

  ;; Query time: 24 msec
  ;; SERVER: 127.0.1.1#53(127.0.1.1)
  ;; WHEN: Fri Dec 29 11:12:08 EST 2017
  ;; MSG SIZE  rcvd: 54  
```

##### Query for "NS" record type
```
$ dig ns umass.edu
                
  ; <<>> DiG 9.10.3-P4-Ubuntu <<>> ns umass.edu
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 3540
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 4

  ;; OPT PSEUDOSECTION:
  ; EDNS: version: 0, flags:; MBZ: 0005 , udp: 512
  ;; QUESTION SECTION:
  ;umass.edu.			IN	NS

  ;; ANSWER SECTION:
  umass.edu.		5	IN	NS	ns3.umass.edu.
  umass.edu.		5	IN	NS	ns1.umass.edu.
  umass.edu.		5	IN	NS	ns2.umass.edu.

  ;; ADDITIONAL SECTION:
  ns1.umass.edu.		5	IN	A	128.119.10.27
  ns2.umass.edu.		5	IN	A	128.119.10.28
  ns3.umass.edu.		5	IN	A	128.103.38.68

  ;; Query time: 30 msec
  ;; SERVER: 127.0.1.1#53(127.0.1.1)
  ;; WHEN: Fri Dec 29 11:13:47 EST 2017
  ;; MSG SIZE  rcvd: 140
```

##### Query for "MX" (mail server) record type
```
$ dig mx umass.edu
                
  ; <<>> DiG 9.10.3-P4-Ubuntu <<>> mx umass.edu
  ;; global options: +cmd
  ;; Got answer:
  ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 14842
  ;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 3

  ;; OPT PSEUDOSECTION:
  ; EDNS: version: 0, flags:; MBZ: 0005 , udp: 512
  ;; QUESTION SECTION:
  ;umass.edu.			IN	MX

  ;; ANSWER SECTION:
  umass.edu.		5	IN	MX	10 race-2.oit.umass.edu.
  umass.edu.		5	IN	MX	10 race-1.oit.umass.edu.
  umass.edu.		5	IN	MX	10 race-4.oit.umass.edu.
  umass.edu.		5	IN	MX	10 race-3.oit.umass.edu.

  ;; ADDITIONAL SECTION:
  race-4.oit.umass.edu.	5	IN	A	128.119.8.37
  race-3.oit.umass.edu.	5	IN	A	128.119.8.36

  ;; Query time: 25 msec
  ;; SERVER: 127.0.1.1#53(127.0.1.1)
  ;; WHEN: Fri Dec 29 11:15:26 EST 2017
  ;; MSG SIZE  rcvd: 166   
```

##### Full DNS lookup hiearchy
```
$ dig +trace umass.edu
```

##### Full reverse DNS lookup -- Map an IP addr to a name
```
$ dig +trace -x 128.119.8.148
```

#### Whois
Client for the whois directory service. whois searches for an object in a RFC 3912 database.

```
$ whois -h whois.ra.net 128.119.8.148
```

#### Host
DNS lookup utility.
```
$ host umass.edu
  umass.edu has address 128.119.8.148
  umass.edu mail is handled by 10 race-4.oit.umass.edu.
  umass.edu mail is handled by 10 race-3.oit.umass.edu.
  umass.edu mail is handled by 10 race-2.oit.umass.edu.
  umass.edu mail is handled by 10 race-1.oit.umass.edu.
```

##### CNAME records
```
$ host -t CNAME google.com
```

#### Route
Show / manipulate the IP routing table.
```
$ route -n
  Kernel IP routing table
  Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
  0.0.0.0         172.16.0.1      0.0.0.0         UG    0      0        0 eth0
  10.10.1.0       0.0.0.0         255.255.255.0   U     0      0        0 eth1
  172.16.0.0      0.0.0.0         255.240.0.0     U     0      0        0 eth0
```

#### Ip Tables
Administration tool for IPv4/IPv6 packet filtering and NAT


#### TCP Version
Print the route packets trace to network host (default is cubic)
```
$ cat /proc/sys/net/ipv4/tcp_congestion_control
  cubic
```

## A collection of useful Linux commnands with examples
#### Cat
Concatenate files and print on the standard output.
```
$ echo "Hello, world!" > filename.txt
$ cat filename.txt 
  Hello, world!
```
#### Tail
Output the last part of files.
```
$ tail -f fileName.txt
```
#### Awk
Pattern scanning and processing language.
```
$ awk '{ sum += $6; n++ } END { if (n > 0) print sum / n; }'
```
#### Sed
Stream editor for filtering and transforming text.
```
$ for file in *; do mv $file `echo $file | sed -e "s/n1/n2/"`; done
```
##### Get IP address from `ifconfig`
```
$ ifconfig eth0 | awk '/inet addr:/ { print $2 }' | sed 's/addr://'
  10.10.1.1
```
#### Watch
Execute a program periodically, showing output fullscreen.
```
$ watch "ls -lrt | tail -10"
```
