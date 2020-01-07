#!/bin/bash
# stops execution when error occurs
set -o errexit

mysql -uroot -ppassword -e "create database polling charset=utf8"
