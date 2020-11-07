<template>
	<div class="col-2 left-menu">
				<ul class="navbar-nav navbar-header">
			        <li class="nav-item dropdown navbar-header">
			        	<a v-if='!preload' class="profile_pic" data-file=''>
			        		<div v-if='user.photo' class="profile-outer" :style='{"background-image":"url("+user.photoUrl+"?t=" + Date.now()+")"}'></div>
			        		<i v-else class="fa fa-user"></i>
			        	</a>
			        	<h6>+ {{ user.phone }}</h6>
			        </li>
                </ul>
                <ul class="navbar-nav navbar-menu-profile">
                	<li class="nav-item dropdown">
			        	<router-link to='/wallet'>
			        		Мой кошелек
			        	</router-link>
			        </li>
			        <li class="nav-item dropdown">
			        	<router-link to='/wallet/profile'>
			        		Профиль
			        	</router-link>
			        </li>
			        <li class="nav-item dropdown">
			        	<router-link to='/wallet/charge'>
			        		Пополнить
			        	</router-link>
			        </li>
			        <li class="nav-item dropdown">
			        	<router-link to='/wallet/transfer'>
			        		Переводы
			        	</router-link>
			        </li>
			        <li class="nav-item dropdown">
			        	<router-link to='/wallet/moneybank'>
			        		Сбор средств
			        	</router-link>
			        </li>
			        <li class="nav-item dropdown">
			        	<router-link to='/wallet/donate'>
			        		Пожертвования
			        	</router-link>
			        </li>
			        <li class="nav-item dropdown">
			        	<router-link to='/wallet/partner'>
			        		Кабинет партнера
			        	</router-link>
			        </li>
					<li class="nav-item dropdown">
			        	<router-link to='/userLogout'>
			        		<strong>Выйти</strong>
			        	</router-link>
			        </li>
                </ul>
	</div>
</template>
<script>

	import axios from 'axios'

	export default {
		data(){
			return {
				user: this.$store.state.user,
				preload: true,
			}
		},
		methods: {
			checkPhoto(){
				const path = 'http://127.0.0.1:8000/static/upload/profile/' + this.user.id + '.png';
				axios.get(path)
					.then((res) => {
						this.user.photo = true;
						this.user.photoUrl = path;
						this.preload = false;

		    	})
				.catch((error) => {
		        	this.user.photo = false;
		        	this.preload = false;
				});
			}
		},
		created(){
			this.checkPhoto();
		}
	}
</script>