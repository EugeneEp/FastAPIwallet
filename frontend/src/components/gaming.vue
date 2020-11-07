<template>
	<main>
		<infoHeader></infoHeader>
		<div class="container-custom">
			<div class="row">
				<indexLeft></indexLeft>
				<div class="col-10">
					<h5 class="inner-title">
	
						Игровые биржи

					</h5>
					<div class="inner-content">
						
						<p class="t1">
							Твоя сфера - продажа игровой валюты,<br>
							аккаунтов, кейсов и скинов?
						</p>

						<p class="t2">
							Специально для тебя Wallet подготовил уникальное пакетное<br>
							предложение:
						</p>

						<p class="t3">
							-самые низкие комиссии на рынке: от 6% СУММАРНО<br>
							-встраиваемые кошельки для пользователей<br>
							-удобные ссылки и виджеты для оплаты<br>
							-инливидуальный подход<br>
							-современные технологии безопасности
						</p>
						<input @click='showModal = !showModal' type="button" class="btn-circle btn-blue-gradient" value="Регистрация">
					</div>
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
  name: 'Gaming',
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