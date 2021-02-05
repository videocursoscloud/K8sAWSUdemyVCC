## Comandos

## etiquetar imagen

```
docker tag imagenlocal:etiqueta usuarioremoto/imagenremota:etiqueta
```

## subir imagen

```
docker push usuarioremoto/imagenremota:etiqueta
```

## descargar imagen

```
docker pull usuarioremoto/imagen:etiqueta
```

## borrar todas las imagenes de nuestra caché
```
docker rmi $(docker images -a -q)
```
