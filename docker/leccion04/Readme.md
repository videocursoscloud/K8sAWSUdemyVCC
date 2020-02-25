## Comandos

## Obtener la ip de un contenedor desde inspect
```
docker inspect NAME|grep IPAddress
```

## crear un contenedor publicando un puerto especifico

```
docker create -p 8080:80 --name web01 helloworld:latest
```

## crear un contenedor publicando un puerto especifico en un interfaz concreto

```
docker create -p ip:8080:80 --name web01 helloworld:latest
```

## crear la nueva imagen 

```
docker build -t helloworld:2.0
```

## taguear como latest

```
docker tag helloworld:2.0 helloworld:latest
```

## crear un contenedor publicando a un puerto local expuesto en la imagen

```
docker create -P --name web01 helloworld:latest
```

## Crear contenedor y arrancarlo a la vez en segundo plano con un solo comando

```
docker run -d ...
```

## Comprobar rango de puertos locales

```
cat /proc/sys/net/ipv4/ip_local_port_range
```


