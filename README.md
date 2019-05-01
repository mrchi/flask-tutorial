# flask-tutorial

```
docker run -d \
    --name flaskr-db \
    -e POSTGRES_USER=flask \
    -e POSTGRES_PASSWORD=flask123 \
    -e POSTGRES_DB=flaskr \
    -p 127.0.0.1:5432:5432 \
    postgres
```

```
psql -U flask -d flaskr -p 5432 -h localhost
```

## TODO

- [] json schema 参数验证；
