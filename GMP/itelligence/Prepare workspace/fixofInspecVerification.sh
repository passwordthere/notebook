#!/bin/bash

chgrp -v sapsys /usr/sap/sapservices && chmod -v 0755 /usr/sap/sapservices
cp /etc/fstab /etc/fstab_GMPSM-8238
sed -i '/vol[1-3]_/s/,rsize=32768//g' /etc/fstab
sed -i '/vol[1-3]_/s/,rsize=65536//g' /etc/fstab
sed -i '/vol[1-3]_/s/,wsize=32768//g' /etc/fstab
sed -i '/vol[1-3]_/s/,wsize=65536//g' /etc/fstab
sed -i '/vol[1-3]_/s/,actimeo=1//g' /etc/fstab
sed -i '/vol[1-3]_/s/,actimeo=600//g' /etc/fstab
umount -a -t nfs;mount -a
mount | grep vol[1-3]
mount -o remount,exec /tmp
rpm -e MFErt MFEcma ISecTP ISecESPAac ISecESP ISecESPFileAccess McAfeeRt
rm -rf /opt/McAfee/ /opt/isec/ /var/McAfee /etc/ma.d/ 
wget -O /tmp/mcafee-install.sh http://repo:50000/repo/tools/McAfee/mcafee-install.sh ; sh /tmp/mcafee-install.sh ; rm /tmp/mcafee-install.sh 
systemctl enable ma ; /usr/lib/systemd/systemd-sysv-install enable ma
umount -a -t nfs && mount -a
