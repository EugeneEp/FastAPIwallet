<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'App',
  data (){
  	return {
  		user: {
  			authenticated: false,
  			token: '',
  			phone: '',
  			id: '',
  			photo: false,
  			photoUrl: ''
  		},
  	}
  },
  methods: {
	checkAuth() {
	    let getToken = localStorage.getItem('token')
	    if(getToken) {
	    	if(this.isValidJWT(getToken)){
	    		this.$store.state.user.authenticated = true;
	    		this.$store.state.user.phone = localStorage.getItem('phone');
	    		this.$store.state.user.id = localStorage.getItem('id');
	    		this.$store.state.user.token = getToken;
	    	}
	    }else
	    	this.$store.state.user.authenticated = false;
  	},
  	isValidJWT(jwt){
  		if (!jwt || jwt.split('.').length < 3) {
			return false
		}
		const data = JSON.parse(atob(jwt.split('.')[1]))
		const exp = new Date(data.exp * 1000)
		const now = new Date()
		return now < exp
  	}
  },
  created(){
  	this.checkAuth();
  },
};
</script>


