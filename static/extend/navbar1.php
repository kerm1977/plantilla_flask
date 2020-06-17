
<!-- Estiliza el navbar en color ligero -->
<nav class="navbar navbar-expand-md navbar-light bg-light">

	<!-- Contenido para achicar el menú y no quede tan expandido y no esté pegada a los margenes -->
	<div class="container">

	<!-- navbar-brand coloca el título de la app -->
	
	<a href="#" class="navbar-brand">
		App
	</a>

	<!-- Boton tipo boton con la clase navbar-toggler y data-toggle busca el div collapse para realizar el colapso de los ul pero se necesita data-target que por medio del id para señalar que se va a colapsar-->

	<button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navbar1">
		<span class="navbar-toggler-icon"></span>
	</button>

	<!-- Colapsa el menú en dispositivos pequeños y envía en tamaños inferiores todos los uls a la izquierda  y la clase collapse es para no permitir que al minimizar la barra el menú aparezca extendido-->

	<div class="collapse navbar-collapse" id="navbar1">

	<!-- Clase para indicar que es la navegación -->
	<!-- ml es margin left y es automático enviando todo para la derecha-->

	<ul class="navbar-nav ml-auto">
			
		<!-- Estilos van en li y la clase nav-items para ocultar viñetas y colocarlos horizontalmente. Mientras a las etiquetas a se le agrega la clase nav-link -->

			<li class="nav-item"><a class="nav-link" href="https://hackerthemes.com/bootstrap-cheatsheet/ ">bootstrap</a></li>
			<li class="nav-item"><a class="nav-link" href="#">Enlace</a></li>
			<li class="nav-item"><a class="nav-link" href="#">Enlace</a></li>
			<li class="nav-item"><a class="nav-link" href="#">Enlace</a></li>
			<li class="nav-item"><a class="nav-link" href="#">Enlace</a></li>
		
	</ul>
		</div>
	</div>
</nav>