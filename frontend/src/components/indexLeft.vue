<template>
	<div class="col-2 left-menu">
				<ul class="navbar-nav navbar-header">
			        <li v-if='user.authenticated' class="nav-item dropdown">
			        	<router-link to='/wallet' v-if='!preload' class="profile_pic">
			        		<div v-if='user.photo' class="profile-outer" :style='{"background-image":"url("+user.photoUrl+"?t=" + Date.now()+")"}'></div>
			        		<i v-else class="fa fa-user"></i>
			        	</router-link>
			        	<router-link to='/userLogout'>
			        		Выйти
			        	</router-link>
			        </li>
			        <li v-else class="nav-item dropdown">
			        	<a @click='$parent.showModal = true'>
			        		<div class="profile_pic">
			        			<i class="fa fa-user"></i>
			        		</div>
			        		Войти
			        	</a>
			        </li>
                </ul>
                <ul class="navbar-nav navbar-menu">
                	<li class="nav-item dropdown">
			        	<router-link to='/capabilities/info' class="nav-link" >Возможности</router-link>
			        </li>
			        <li class="nav-item dropdown">
			        	<router-link to='/about/info' class="nav-link" >О нас</router-link>
			        </li>
			        <li class="nav-item dropdown">
			        	<router-link to='/contacts/info' class="nav-link" >Контакты</router-link>
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
				preload: true
			}
		},
		methods:{
			checkPhoto(){
				if(this.user.authenticated){
					const path = 'http://127.0.0.1:1337/static/upload/profile/' + this.user.id + '.png';
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
				}else{
					this.user.photo = false;
				}
			}
		},
		created(){
			this.checkPhoto();
		}
	}
</script>