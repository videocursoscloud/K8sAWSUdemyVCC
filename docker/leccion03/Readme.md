## Comandos

## crear un contenedor
```
docker create helloworld
```
o 
```
docker create helloworld:etiqueta
```

## listar contenedores en ejecucion
```
docker ps 
```

## listar contenedores (incluso parados)
```
docker ps -a
```

## eliminar contenedores
```
docker rm ID_parcial
```
o
```
docker rm ID
```
o
```
docker rm name
```

## Iniciar o arrancar un contenedor ya creado

```
docker start name
```

## parar un contenedor ya creado y arrancado

```
docker stop name
```

## eliminar un contenedor que esta corriendo

```
docker rm name -f
```

## crear un container con nombre

```
docker create --name web01 helloworld:latest
```


## Inspeccionar contenedor

``` 
docker inspect web01
```


