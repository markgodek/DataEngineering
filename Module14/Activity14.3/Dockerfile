
FROM mysql:8.0

ENV MYSQL_DATABASE=customerdb \
    MYSQL_ROOT_PASSWORD=MyNewPass

ADD customer.sql /docker-entrypoint-initdb.d

EXPOSE 3306