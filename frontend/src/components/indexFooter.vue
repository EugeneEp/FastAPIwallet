<template>


		<div class="modal-mask" id="modalSignUp" style="display: none;" v-show="$parent.showModal">
              <div class="modal-wrapper">
		  <div class="modal-dialog modal-lg">
		    <div class="modal-content row">
		    	<div class="col-5">
		    		<div class="reg-btns">
		    			<input type="button" @click='reg=true' :class="{'btn-blue': reg, 'btn-grey': !reg}" class="btn-tog" value="Регистрация">
		    			<input type="button" @click='reg=false' :class="{'btn-blue': !reg, 'btn-grey': reg}" class="btn-tog" value="Авторизация">
		    		</div>
		    		<div class="modal-block info-block">
			    		<div class="reg-modal-header">Wallet</div>
			    		<div class="reg-modal-desc">Открой <br>для себя безграничные возможности <span>Wallet</span></div>
			    		<p class="reg-modal-info">Пройдите первичную регистрацию, чтобы открыть функционал кошелька <span>Basic</span></p>
			    		<div class="reg-modal-lock">
			    			<i class="fa fa-lock"></i>
			    		</div>
			    	</div>
		    	</div>
		    	<div class="modal-block col-7">
					<button type="button" class="close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true" @click="$parent.showModal = false">&times;</span>
					</button>
		    		<div v-if='reg' class="modal-block-form">
		    			<div class="w3-light-grey w3-round">
	    					<div class="w3-container w3-just-blue w3-round" :style="{width:percentProgress}">
	    					{{percentProgress}}</div>
	  					</div>
			    		<div class="row" id="getSms">
			    			<form id="enter-phone" v-if='regStatus==0' @submit='getSms'>
			    				<h3>Укажите свой номер телефона</h3>
			    				<div class="enter-block enter-phone">
		                			<input type="text" name="phone" id="phone" v-model='smsForm.phone' class="form-control" v-mask="'+7(999)999-99-99'" placeholder="Номер телефона" maxlength="16">
		                			<span>У вас уже есть личный кабинет? </span>
		                			<a onclick="" value="Авторизация">Войти</a>
		                		</div>
		                		<div class="col-12">
			                		<input type="submit" class="btn-square btn-blue-gradient" value="Далее">
			                	</div>
			    			</form>
			    			<form id="enter-code" v-else-if='regStatus==1' @submit="smsCheck">
			    				<h3>На ваш номер было отправлено смс с кодом (1111)</h3>
			    				<div class="enter-block">
									<div class="divOuter">
									  <div class="divInner">
									    <input class="partitioned" required="" v-model='smsForm.code' type="text" name="code" maxlength="4" onKeyPress="if(this.value.length==4) return false;">
									  </div>
									</div>
								</div>
								<div class="col-12">
			                		<input type="submit" class="btn-square btn-blue-gradient" value="Далее">
			                	</div>
			    			</form>
			            </div>
			            <form class="row data-form" v-if='regStatus==2' @submit='regUser' id='reg'>
			            	<h3>Отлично! Теперь придумайте пароль, для вашей учетной записи</h3>

			            	<div class="enter-block">
			            		<input type="password" required="" v-model='userForm.password' name="password" class="form-control" placeholder="Придумайте пароль">
			            		<input type="password" v-model='userForm.confirm' required="" name="confirm" class="form-control" placeholder="Повторите парль">
			            	</div>

							<span style="color: red; display: none;" class="error"></span>
			                <div class="col-12">
			                	<input type="submit" class="btn-square btn-blue-gradient" value="Далее">
			                </div>
			            </form>
			            <div v-if='regStatus==3' class="row" id='finish'>
				            <div class="enter-block">
				            	<h3 class="enter-phone">Спасбо! Вы прошли первичную регистрацию</h3>
				            </div>
			            	<div class="col-12">
			                	<router-link to='/wallet' class="btn-square btn-blue-gradient" >Перейти в личный кабинет</router-link>
			                </div>
			            </div>
			        </div>
			        <div v-else class="modal-block-form">
			        	<form class="row data-form" @submit='logUser' id='log'>
			        		<h3>Авторизуйтесь с помощью номера мобильного телефона</h3>

			        		<div class="enter-block">
								<input type="text" v-model='logUserForm.phone' name="phone" v-mask="'+7(999)999-99-99'" value="" class="form-control" placeholder="Номер телефона" maxlength="16">
				            	<input type="password" v-model='logUserForm.password' required="" name="password" class="form-control" placeholder="Пароль">
				            </div>
			                <div class="col-12">
			                	<input type="submit" class="btn-square btn-blue-gradient" value="Войти">
			                </div>
			            </form>
			        </div>
			        <alert :message="message" :success="success" v-if='showMessage'></alert>
			    </div>
		    </div>
		  </div>
		</div>
	</div>
</template>
<script>

	import axios from 'axios';
	import Alert from './Alert'

export default {
  props: ['showModal'],
  data() {
    return {
    	reg: true,
    	regStatus: 0,
    	message: '',
    	success: true,
    	showMessage: false,
    	percentProgress: '25%',
    	smsForm: {
    		code: '',
    		phone: '',
    		type: 'reg'
    	},
    	userForm: {
    		phone: '',
    		password: '',
    		confirm: ''
    	},
    	logUserForm: {
    		phone: '',
    		password: ''
    	},
    	ajaxConfig: {
	        headers: {
	          'Content-Type': 'application/json',
	        }
		}
    };
  },
  methods: {
  	getSms(e){
  		e.preventDefault();
  		const path = 'http://127.0.0.1:8000/sms';
	    axios.post(path, this.smsForm)
	      .then((res) => {
          
          this.message = res.data.message;
          this.success = res.data.success;
          console.log(res.data.success);
          if(this.success){
          	this.percentProgress = '50%';
          	this.regStatus=1;
          }
        })
        .catch((error) => {
          this.message = error.response.data.message;
          this.success = false;
          this.openMessage()
        });
  	},
  	smsCheck(e){
  		e.preventDefault();
  		console.log(this.smsForm);
  		const path = 'http://127.0.0.1:8000/sms_check';
	    axios.post(path, this.smsForm)
	      .then((res) => {
          
          this.message = res.data.message;
          this.success = res.data.success;
          this.userForm.phone = this.smsForm.phone
          if(this.success){
          	this.percentProgress = '75%';
          	this.regStatus=2;
          }
        })
        .catch((error) => {
          this.message = error.response.data.message;
          this.success = false;
          this.openMessage()
        });
  	},
  	regUser(e){
  		e.preventDefault();
  		const path = 'http://127.0.0.1:8000/registration';
	    axios.post(path, this.userForm)
	      .then((res) => {
          
          this.message = res.data.message;
          this.success = res.data.success;
          if(this.success){
			let token = res.data.token;
          	let phone = this.userForm.phone.replace(/\D/g, "");
          	let id = res.data.id;
			localStorage.setItem('token', token);
			localStorage.setItem('phone', phone);
			localStorage.setItem('id', id);
			this.$store.state.user = {authenticated: true, phone: phone, token: token, id: id}
			this.percentProgress = '100%';
          	this.regStatus=3;
          }
        })
        .catch((error) => {
          this.message = error.response.data.message;
          this.success = false;
          this.openMessage()
        });
  	},
  	logUser(e){
  		e.preventDefault();
  		const path = 'http://127.0.0.1:8000/login';
	    axios.post(path, this.logUserForm)
	      .then((res) => {
          console.log(res);
          this.message = res.data.message;
          this.success = res.data.success;
          if(this.success){
          	let token = res.data.token;
          	let phone = this.logUserForm.phone.replace(/\D/g, "");
          	let id = res.data.id;
			localStorage.setItem('token', token);
			localStorage.setItem('phone', phone);
			localStorage.setItem('id', id);
			this.$store.state.user = {authenticated: true, phone: phone, token: token, id: id}
			this.$router.push('/wallet')
          }
        })
        .catch((error) => {
          this.message = error.response.data.message;
          this.success = false;
          this.openMessage()
        });
  	},
  	openMessage(){
  		this.showMessage = true;
	          setTimeout(() => {
	            this.showMessage = false;
	          }, 3000);
  	}
  },
  components: {
  	alert: Alert
  }
};
</script>