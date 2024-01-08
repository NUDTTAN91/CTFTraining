#!/bin/bash

#sed -i "s/flag_here/$FLAG/" /var/www/html/flagaa.php

mysql -e "USE ctftraining;CREATE TABLE \`flag\` (\`flag\` varchar(255) DEFAULT NULL) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;INSERT INTO \`flag\`(flag) VALUES ('$GZCTF_FLAG');" -uroot -proot

export FLAG=not_flag
FLAG=not_flag

rm -f /flag.sh
