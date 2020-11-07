<template>
	<main>
		<walletHeader></walletHeader>
		<div class="container-custom">
			<div class="row">
				<walletLeft></walletLeft>
				<div class="col-10">
					<div class="row">
						<div class="col-lg-3 col-md-4">
							<h5 class="inner-title-profile">
								Пожертвования

								<span>Ваши личные данные</span>

								<p>Принимай донаты с любых сервисов и на любые суммы!</p>
							</h5>
						</div>
						<div class="col-lg-9 col-md-8">
							
						</div>
					</div>
					<div class="charge-block">
							<form class="data-form" @submit='sendData'>
								<p class="t5">1. Настройте интеграцию со стриминговыми сервисами</p>
								<div class="charge-images">
									<img src="/static/images/twitch.png">
									<img src="/static/images/wasd.png">
									<img src="/static/images/youtube.png">
								</div>

								<p class="t5">2. Настройте прием пожертвований</p>

								<a href="#">Открыть настройки пожертвований</a>


								<a href="#">Создать ссылку для оплаты <i class="fa fa-info-circle"></i></a>
								<input type="text" name="" class="form-control">

								<a href="#">Создать ссылку для оплаты <i class="fa fa-info-circle"></i></a>

								<a href="#" class="t2">Создать виджет оплаты</a>
								<p class="t5">Виджет - кастоммизированная ссылка на оплату, которая позволяет принимать платежи любым способом без создания собственного сайта.<br>Идеальный вариант для торговли в социальных сетях и мессенджерах.</p>
								<a href="#" class="t2">Получить виджет</a>

								<input type="submit" class="btn-square btn-blue-gradient" value="Создать">
							</form>
							<alert :message="message" :success="success" v-if='showMessage'></alert>
						</div>
				</div>
			</div>
		</div>
	</main>
</template>

<script>

	import axios from 'axios'
	import walletHeader from './walletHeader'
	import walletLeft from './walletLeft'
	import Alert from '../Alert'

export default {
  name: 'Donate',
  data() {
    return {
    	showModal: false,
    	showModal: false,
    	message: '',
    	success: '',
    	showMessage: false,
    	data: {

    	},
    	ajaxConfig: {
	        headers: {
	          'Content-Type': 'application/json',
	          Authorization: 'Bearer ' + this.$store.state.user.token
	        }
		},
    };
  },
  components: {
    walletHeader: walletHeader,
    walletLeft: walletLeft,
    alert: Alert,
  },
  methods: {
  	sendData(e){
		e.preventDefault();
  		const path = 'http://127.0.0.1:8000/wallet/donate';
  		console.log(this.ajaxConfig);
	    axios.post(path, this.sendData, this.ajaxConfig)
	      .then((res) => {
          
          this.message = res.data.msg;
          this.success = res.data.success;
          console.log(res.data);
          this.openMessage()
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
  created() {

  },
};
</script>