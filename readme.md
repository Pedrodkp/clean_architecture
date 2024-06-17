# Install

```
docker rm -f clean_architecture_mysql
docker run --name clean_architecture_mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:8.0.37-debian
```

# Run

```
pytest -s -v
```