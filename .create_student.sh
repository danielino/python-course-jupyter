#!/bin/bash

help(){ 
  echo "$0 student"
  exit -1
}

[[ $# -ne 1 ]] && help

student=$1
base=$(realpath $(pwd)/students)

[[ -d $base/$student ]] && rm -rf $base/$student

cp -R corso/ $base/$student

find $base/$student -type f -name "*solu*" -exec rm {} \;
