## Comandos

## listar redes

```
docker network ls
```

## Crear network

```
docker network create nombre_de_la_red --driver nombre_del_driver 
por ejemplo:
docker network create web --driver bridge
```

## Crear un contenedor dentro de una red

```
docker create --name web01 --network web helloworld
```

##  filtrar ip en la salida de docker inspect
```
docker inspect web01 |grep IPAddress
```

## eliminar las redes que no esten en uso

```
docker network prune
```

## conectar y desconectar un contenedor de una red

```
docker connect web web01
docker disconnect web web01
```
