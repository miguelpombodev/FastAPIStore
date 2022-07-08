#!/bin/bash

#run the setup script to create the DB and the schema in the DB
/opt/mssql-tools/bin/sqlcmd -S 127.0.0.1 -U sa -P Passw0rd -i /usr/src/app/init.sql