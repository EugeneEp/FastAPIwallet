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
								Профиль

								<span>Ваши личные данные</span>
							</h5>
						</div>
						<div class="col-lg-10 col-md-9">
							
						</div>
					</div>
					<div class="charge-block">
						<form class="data-form" id="profile_picture" @submit='changePhoto'>
							<a href="#" class="t2">Добавить изображение профиля</a>
							<div class="profile_pic" data-file=''>
								<a v-if='!preload' class="profile_pic" data-file=''>
									<div class="profile-outer" :style="{'background-image':'url(' + preview + ')'}"></div>
								</a>
							</div>
							<div class="file-field">
							    <input type="file" id="file" class="input-file" name="img" accept="image/gif, image/jpeg, image/png" @input='readURL'>
							    <label for="file" class="btn btn-tertiary js-labelFile">
							    	<span class="js-fileName">Выберете файл</span>
							    </label>
							</div>
							<input type="submit" class="btn-square btn-blue-gradient" value="Загрузить">
							<alert :message="message" :success="success" v-if='showMessage'></alert>
						</form>
						<form class="data-form" @submit='userIdentity'>
							<a href="#" class="t2">Идентификация кошелька</a>
							<p class="t5">Введите ваши данные для получения идентифицированного кошелька.</p>
							<a href="#">Фамилия Имя Отчество</a>
							<input type="text" v-model='identity.fullname' required="" name="fullname" value="" placeholder="Иванов Иван Иванович"  class="form-control">
							<a href="#">Серия номер паспорта</a>
							<input type="text" v-model='identity.passport' required="" name="passport" value="" placeholder="1111 111111" class="form-control">
							<a href="#">Дата выдачи</a>
							<input type="date" v-model='identity.passportIssuedAt' required="" name="passportIssuedAt" value="" class="form-control">

							<input type="submit" class="btn-square btn-blue-gradient" value="Отправить">

							<alert :message="message" :success="success" v-if='showMessage1'></alert>

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
	name: 'Profile',
	data() {
	    return {
	    	showModal: false,
	    	user: this.$store.state.user,
	    	preload: true,
	    	preview: null,
	    	message: '',
	    	success: false,
	    	showMessage: false,
	    	showMessage1: false,
	    	identity: {
	    		fullname:'',
	    		passport:'',
	    		passportIssuedAt:''
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
  		checkPhoto(){
				const path = 'http://127.0.0.1:8000/static/upload/profile/' + this.user.id + '.png';
				axios.get(path)
					.then((res) => {
						this.user.photo = true;
						this.user.photoUrl = path;
						this.preview = path;
						this.preload = false;

		    	})
				.catch((error) => {
		        	this.user.photo = false;
				});			
				console.log(this.user);
			},
		readURL(event) {
	        let file = event.target.files
	        console.log(file);
	        if (file && file[0]) {
	          let reader = new FileReader
	          reader.onload = e => {
	          	this.user.photo = true;
	            this.user.photoUrl = e.target.result;
	            this.preview = e.target.result;
	            this.preload = false;
	          }
	          reader.readAsDataURL(file[0]);
	          this.$emit('input', file[0]);
			}
		},
		changePhoto(e){
			e.preventDefault();
			let formData = new FormData();
			let imagefile = document.querySelector('#file');
			formData.append("image", imagefile.files[0]);
			const path = 'http://127.0.0.1:8000/wallet/profile_picture';
			console.log(path);
			axios.post(path, formData, this.ajaxConfig).then((res) => {
				this.message = res.data.message;
          		this.success = res.data.success;
				this.showMessage = true;
				setTimeout(() => {
					this.showMessage = false;
				}, 3000);

		    }).catch((error) => {
		        	this.message = error.response.data.message;
		        	this.success = false;
		        	setTimeout(() => {
						this.showMessage = false;
					}, 3000);
		        });
		},
		userIdentity(e){
			e.preventDefault();
			const path = 'http://127.0.0.1:8000/wallet/profile';
			axios.put(path, this.identity, this.ajaxConfig)
				.then((res) => {
				this.message = res.data.message;
				this.success = res.data.success;
				this.showMessage1 = true;
				setTimeout(() => {
					this.showMessage1 = false;
				}, 3000);
	    	})
			.catch((error) => {
		        	this.message = error.response.data.message;
		        	this.success = false;
		        	setTimeout(() => {
						this.showMessage1 = false;
					}, 3000);
		        });
		},
		getUserIdentity(){
			const path = 'http://127.0.0.1:8000/wallet/profile';
			axios.get(path, this.ajaxConfig)
				.then((res) => {
					this.identity = res.data.identity;
	    	})
			.catch((error) => {
				console.log(error.response.data.message);
			});
		}
	},
	created() {
		this.checkPhoto();
		this.getUserIdentity();
	}
};
</script>