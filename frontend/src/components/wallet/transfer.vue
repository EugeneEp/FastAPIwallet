<template>
	<main>
		<walletHeader></walletHeader>
		<div class="container-custom">
			<div class="row">
				<walletLeft></walletLeft>
				<div class="col-10">
					<div class="row">
						<div class="col-lg-2 col-md-3">
							<h5 class="inner-title-profile">
								Переводы

								<span>Выберете способ перевода</span>
							</h5>
						</div>
						<div class="col-lg-10 col-md-9">
							
						</div>
					</div>
					<div class="transfer-block">

								<form class="data-form" @submit='sendData'>
									<div>
										<div class="form-group">
											<span>На банковскую карту</span>
											<input type="text" placeholder="Введите номер карты" name="card" class="form-control">
											<input type="number" placeholder="Сумма" name="amount" class="form-control">
										</div>
										<div class="form-group">
											<span>На другой кошелек</span>
											<input type="text" placeholder="Номер кошелька" name="card" class="form-control">
											<input type="number" placeholder="Сумма" name="amount" class="form-control">
										</div>
										<div class="form-group">
											<span>На рассчетный счет</span>
											<input type="text" placeholder="Номер счета" name="card" class="form-control">
											<input type="number" placeholder="Сумма" name="amount" class="form-control">
										</div>
										<div class="form-group">
											<span>Массовые выплаты</span>

											<div class="custom-file">
											    <input type="file" class="custom-file-input" id="inputGroupFile01"
											      aria-describedby="inputGroupFileAddon01">
											    <label class="custom-file-label" for="inputGroupFile01">Выберете CSV файл</label>
											</div>
										</div>
									</div>
									<input type="submit" class="btn-square btn-blue-gradient" value="Перевести">
									<br><br>
									<alert :message="message" :success="success" v-if='showMessage'></alert>
								</form>
								
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
  name: 'Transfer',
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