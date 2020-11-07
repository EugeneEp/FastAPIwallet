// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import Vuex from 'vuex';
import App from './App';
import router from './router';

const VueInputMask = require('vue-inputmask').default
Vue.use(VueInputMask)

Vue.use(Vuex);

export const store = new Vuex.Store({
	state: {
  		user: {
  			authenticated: false,
  			token: '',
  			phone: ''
  		}
  	}
});

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});
