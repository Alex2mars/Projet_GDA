FROM postgres:latest
COPY pg_* /run/secrets/
COPY init_sql_scripts/* /docker-entrypoint-initdb.d/
