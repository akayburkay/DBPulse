# DBPulse
PostgreSQL Database Performance and Health App

DBPulse is a comprehensive desktop application designed to monitor the performance and overall health of PostgreSQL databases. 
It allows you to easily track query statistics, inspect database structures, and observe system resource usage — all in real time.

🚀 Features
Query performance statistics using pg_stat_statements

Database contents: tables, views, indexes

Disk usage, table sizes, and growth trends

Server status monitoring: CPU, memory, disk, active connections

Real-time monitoring with a user-friendly desktop interface

⚙️ Requirements
For the application to function correctly, the pg_stat_statements extension must be enabled in the PostgreSQL configuration.

Make sure the following line exists in your postgresql.conf file:

shared_preload_libraries = 'pg_stat_statements'
After making this change, restart the PostgreSQL service.

Then, run the following SQL command in the connected database:

CREATE EXTENSION pg_stat_statements;
Without this extension, query performance statistics cannot be collected.
