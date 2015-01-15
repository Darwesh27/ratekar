#!/bin/bash   
mysql --host=$DB_HOST --user=root --password=$DB_PASS << EOF
create database rateker charset utf8;
EOF
