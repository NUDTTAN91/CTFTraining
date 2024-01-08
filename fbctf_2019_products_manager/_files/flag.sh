#!/bin/bash

# 修改数据库中的 FLAG
mysql -e "INSERT INTO products VALUES('facebook', sha2('wkjhduiefgheruifertyf7834tr349ft7dgweif', 256), '$FLAG');" -uroot -proot

export FLAG=not_flag
FLAG=not_flag

rm -f /flag.sh
