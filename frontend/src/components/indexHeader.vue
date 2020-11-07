<template>
		<nav class="navbar navbar-expand-lg navbar-light bg-white row header">
			<div class="col-2 header-brand">
		  		<router-link class="navbar-brand" to='/'>Wallet</router-link>
		  		<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
		    <span class="navbar-toggler-icon"></span>
		  </button>
		  	</div>
		  	<div class="collapse navbar-collapse col-10" id="navbarSupportedContent">
			    <ul class="navbar-nav">
			    	<li class="nav-item">
	          			<router-link to='/start-business/info' class="nav-link" >Бизнес на старте</router-link>
	        		</li>
	        		<li class="nav-item">
	          			<router-link to='/stream/info' class="nav-link" >Стриминг</router-link>
	        		</li>
	        		<li class="nav-item">
	        			<router-link to='/business/info' class="nav-link" >Инфобизнес</router-link>
	        		</li>
	        		<li class="nav-item">
	        			<router-link to='/gaming/info' class="nav-link" >Игровые биржи</router-link>
	        		</li>
	        		<li class="nav-item">
	        			<router-link to='/events/info' class="nav-link" >Частные мероприятия, ивенты</router-link>
	        		</li>
			    </ul>
		  	</div>
		</nav>
</template>