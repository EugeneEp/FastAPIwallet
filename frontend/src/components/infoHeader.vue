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
		    	<li class="">
          			<router-link to='/' class="nav-link"><i class="fa fa-arrow-left"></i> Назад</router-link>
        		</li>
		    </ul>
	  	</div>
	</nav>
</template>