## Comandos

## listar volumenes

```
docker volume ls
```

## Crear volumen
```
docker volume create my-volume
```

## Inspeccionar volumen
```
docker volume inspect my-volume
```

## crear contenedor con volumen persistente
```
docker create -P --mount source=my-volume,target=/var/www/html --name web01 helloworld:latest
```

## eliminar un volumen
```
docker volume rm my-volume
```

## limpiar o purgar el listado de volumenes no utilizados
``` 
docker volume prune
```


