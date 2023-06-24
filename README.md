# serviciosRest
Tarea Academica Servicios Rest PUCP 
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

 
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Sobre el Proyecto

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Este proyecto tiene la finalidad de mostrar la funcionalidad de microservicios usando python y Django Rest Framework

Notas Importantes:
* Django Rest Framework tiene de manera nativa el consumo de endpoints con metodos GET, POST, PUT, DELETE
* El consumo es con pocas lineas


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Creado con

En esta seccion se lista los  frameworks/libraries usadas en el proyecto. .

* [Django]
* [DjangoRestFramework]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Para utilizar seguir los siguientes pasos
### Prerequisitos

Instalar Django (Se asume que python y pip ya se encuentran instalados en su maquina, se recomienda usar [Entornos virtuales ])
* Instalando Django
  ```sh
  pip install django
  ```
Instalar Django Rest Framework 
* Instalando DRF
  ```sh
  pip install djangorestframefork
  ```

### Instalacion

1. Clone the repo
   ```sh
   git clone https://github.com/rebaza98/serviciosRest.git
   ```
2. Instalar los requerimientos
   ```sh
   pip install -r requierements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Uso

Se puede usar cualquier cliente para el consumo de endpoints, como postman o insomnia
Para consultas GET utilizar:

```sh
   .../apis/cliente
```
Con este endpoint se puede consumir el servicio de consultas que retorna  la lista de clientes , utilizar el methodo GET en la peticion o request

Para consultas GET utilizar:

```sh
   .../apis/cliente/{id}
```
Con este endpoint se puede consumir el servicio de consultas que retorna  un clientes con el {id} , utilizar el methodo GET en la peticion o request

Para consultas POST utilizar:

```sh
   .../apis/cliente/
```
Con este endpoint se puede consumir el servicio de crear un cliente , utilizar el methodo POST en la peticion o request

Para consultas PUT utilizar:

```sh
   .../apis/cliente/{id}
```
Con este endpoint se puede consumir el servicio para actualizar un cliente con el {id} , utilizar el methodo PUT en la peticion o request

Para consultas DELETE utilizar:

```sh
   .../apis/cliente/{id}
```
Con este endpoint se puede consumir el servicio para eliminar un cliente con el {id} , utilizar el methodo DELETE en la peticion o request


##EJEMPLO

endpoint POST creacion de un cliente:
```sh
   http://localhost:8000/apis/cliente
```
body en formato JSON:
```sh
   {
		"id": 3,
		"nombre": "Jon",
		"apellido_paterno": "Snow",
		"apellido_materno": "eSnoe2",
		"dni": "313123123123"
	}
```



_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>








<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Django]: https://www.djangoproject.com/
[DjangoRestFramework]: https://www.django-rest-framework.org/
[Entornos virtuales]: https://www.programaenpython.com/miscelanea/crear-entornos-virtuales-en-python/
