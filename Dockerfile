FROM mysql:latest

# Use .cnf format file for MySQL configuration
COPY ./config.cnf /etc/mysql/conf.d/

# Set the password for the default postgres user DO NOT USE IN PRODUCTION
ENV MYSQL_ROOT_PASSWORD=postgres
# Set the default database name DO NOT USE IN PRODUCTION
ENV MYSQL_DATABASE=postgres
# Set the default user for the database DO NOT USE IN PRODUCTION
ENV MYSQL_USER=postgres
# Set the password for the default postgres user DO NOT USE IN PRODUCTION
ENV MYSQL_PASSWORD=postgres

EXPOSE 45