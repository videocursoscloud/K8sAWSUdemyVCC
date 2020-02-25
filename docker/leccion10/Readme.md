## Comandos

## construir contenedor

```
docker build -t helloworld:4.0 
```

#tagear la imagen
```
docker tag helloworld:4.0 helloworld:latest
docker tag helloworld:4.0 videocursoscloud/helloworld:4.0
docker tag helloworld:4.0 videocursoscloud/helloworld:latest
```

# subir la imagen al repositorio

```
docker push videocursoscloud/helloworld:4.0 
docker push videocursoscloud/helloworld:latest
```

 
