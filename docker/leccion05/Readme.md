## Comandos

## Instalar terminator

```
sudo apt install terminator -y
```

## Crear nueva division horizontal en terminator
```
Ctrl + Shift + o
```

## crear contenedor
```
docker run --name web01 -d -P helloworld
```

## Algunos ejemplos de ejecutar comandos dentro del contenedor con exec
```
docker exec web01 ls /
docker exec web01 ps
```

## Ejecutar la shell bash dentro de un contenedor que esta corriendo
```
docker exec -it web01 bash
```

## Ver logs de nginx dentro del contenedor
```
tail -f /var/log/nginx/access.log
```


