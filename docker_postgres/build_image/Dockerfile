FROM postgres:latest
COPY pg_* /run/secrets/
COPY init_scripts/* /docker-entrypoint-initdb.d/
