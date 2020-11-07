<template>
	<main>
		<infoHeader></infoHeader>
		<div class="container-custom">
			<div class="row">
				<indexLeft></indexLeft>
				<div class="col-10">
					<h5 class="inner-title">
	
						Контакты

					</h5>
					<div class="inner-content">
						Контакты<br>
						Онлайн<br>
						test@test.com<br>
						+7 (999) 999-99-99<br>
						Оффлайн<br>
						Россия, г.Москва, ул. Пушкина<br>
						+7 (888) 888-88-88<br>
						Часы работы: с 9:00 дл 18:00
						


					</div>
					<br><br>
					<input @click='showModal = !showModal' type="button" class="btn-circle btn-blue-gradient" value="Регистрация">
				</div>
			</div>
		</div>
		<indexFooter></indexFooter>
	</main>
</template>

<script>

	import infoHeader from './infoHeader'
	import indexLeft from './indexLeft'
	import indexFooter from './indexFooter'

export default {
  name: 'Contacts',
  data() {
    return {
    	showModal: false,
		ajaxConfig: {
	        headers: {
	          'Content-Type': 'application/json',
	        }
		},
    };
  },
  components: {
    infoHeader: infoHeader,
    indexLeft: indexLeft,
    indexFooter: indexFooter
  },
  methods: {

  },
  created() {

  },
};
</script>