#!/bin/bash

chown pi:www-data ../Djangoticia/
chown pi:www-data ./app1/
chown pi:www-data ./db.sqlite3
chown pi:www-data ./log/
chown pi:www-data /var/www/
chown pi:www-data ./my_python/
chown root:www-data /
chown root:www-data /etc/wpa_supplicant/wpa_supplicant.conf

chmod 775 ../Djangoticia/
chmod 775 ./log/
chmod 775 ./app1/
chmod 775 /var/www/
chmod 664 ./db.sqlite3
chmod 775 ./my_python/
chmod 775 /
chmod 660 /etc/wpa_supplicant/wpa_supplicant.conf
