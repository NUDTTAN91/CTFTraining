#!/bin/sh

sed -i "s/flag{aa4059c8-8d0b-442d-bc89-7f8d8846be26}/$FLAG/" /app/sshop/views/Shop.py

export FLAG=not_flag
FLAG=not_flag

cd /app

python main.py

tail -F /dev/null
