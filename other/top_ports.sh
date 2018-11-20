cat /usr/share/nmap/nmap-services | grep -v "^#" | tr '\t' ' ' | awk '{print $3, $2, $1}' | sort -r | head -$1 | cut -d' ' -f2 | cut -d'/' -f1
