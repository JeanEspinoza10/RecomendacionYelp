# Arquitectura
El presente servicio Apirest tendra el siguiente flujo:
![[Flujograma del pryecto]](img\arquitectura.png)

# Algoritmo de Recomendación
Estos sistemas personalizan las recomendaciones segun las calificaciones que recibe cada item. Para el presente trabajo de los diferentes sistemas de recomendacion se elijio el de Collaborative Filtering, adaptandolo para nuestras necesidades.

## Funcionamiento de Collaborative Filtering
Adaptando este sistema a nuestros objetivos, es tener las valoraciones de cada categoria según el espacio(estado) que se encuentre. Para posteriormente, obtener las categorias similares segun las puntuaciones obtenidas de nuestra base de datos.
Y recomendar los estados con mejor puntuación.

