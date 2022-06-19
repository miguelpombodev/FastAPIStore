#!/bin/bash

# Typically SQL Server takes about 5-10 seconds to start up 
# Wait for the SQL Server to come up (90 sec) You can reduce to 20sec and see
sleep 90s

#run the setup script to create the DB and the schema in the DB
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P P@ssw0rd -d master -i init.sql