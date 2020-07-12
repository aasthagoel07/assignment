#!/usr/bin/env bash
SOURCE=$1
FILELOCATION=$2
JSONDATA=""
case $SOURCE in
    capterra)
        JSONDATA=$(python Read_Yaml.py $FILELOCATION)
        ;;
    softwareadvice)
        JSONDATA=$(python Read_Json.py $FILELOCATION)
        ;;
esac
python Import_To_Db.py "$JSONDATA"