### Laboratorio

### Parte 2

## Crear la imagen de nuestra aplicacion

``` 
cd app
docker build -t python . 
```

## Ejecutar nuestra imagen

```
docker run --network lab -e db_host=db01 -e db_user=root -e MYSQL_ROOT_PASSWORD=passw0rd -e db_name=users --name python --rm -p 5000:5000 python:latest
```

## Conectamos a la base de datos e insertamos nuevos datos

```
docker exec -i db01 bash
mysql -uroot -ppassw0rd
use users;
select * from user;
insert into user values(2,"Warren")
select * from user;
```

