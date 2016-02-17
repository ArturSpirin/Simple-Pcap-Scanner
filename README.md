##This is a simple script that allows to search if a .pcap file contains certain values

#How to use:

0. You have to have tshark installed and TSHARK_HOME must be set
1. Call the script via python and tell the script where the .pcap file is located: python Scanner.py "path/to/my.pcap"
2. You have an option to specify which key values you want to search for: python Scanner.py "path/to/my.pcap" .us anchorfree hotspotshield vpn
  1. If you do not specify the key values, it will use default ones: keyWords = [".us","anchorfree","hotspotshield","vpn","proxy","rss2search", "hsselite"]
3. Script will produce stdout if it finds any of the key values
4. Once scan is started, a text file from .pcap file will become available in the project directory