<template>
		<nav class="navbar navbar-expand-lg navbar-light bg-white row header">
			<div class="col-2 header-brand">
		  		<router-link class="navbar-brand" to='/'>Wallet</router-link>
		  		<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
		    		<span class="navbar-toggler-icon"></span>
		  		</button>
		  	</div>
		  	<div class="collapse navbar-collapse col-10" id="navbarSupportedContent">
			    <ul class="navbar-nav mr-auto">
					
			    </ul>
			    <ul class="navbar-nav navbar-nav-wallet">
			    	<li class="nav-item dropdown">
				        <a class="nav-link wallet-link">
				          <div class="nav-icons">
				          	<i class="fa fa-chevron-down"></i>
				          	<i class="fa fa-wallet"></i>
				          </div>
				        </a>
				        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
				          <a class="dropdown-item" href="#">Пока ничего</a>
				          <a class="dropdown-item" href="#">Пока ничего нет</a>
				          <div class="dropdown-divider"></div>
				          <a class="dropdown-item" href="#">Тут пока ничего нет</a>
				        </div>
				    </li>
			    </ul>
		  	</div>
		</nav>
</template>