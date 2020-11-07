<template>
	
</template>
<script>

	import axios from 'axios';

	export default{
		name: 'userLogout',
		methods: {
			logout(){
				//const path = 'http://127.0.0.1:1337/logout';
			    //axios.get(path)
			    //  .then((res) => {
					localStorage.setItem('token', '');
					this.$store.state.user = {authenticated: false, phone: ''}
					this.$router.push('/');
		        //})
		        //.catch((error) => {
		        //  console.error(error);
		        //});
			}
		},
		created(){
			this.logout();
		}
	}
</script>