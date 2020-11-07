<template>
	<main>
		<infoHeader></infoHeader>
		<div class="container-custom">
			<div class="row">
				<indexLeft></indexLeft>
				<div class="col-10">
					<h5 class="inner-title">
	
						Возможности

					</h5>
					<div class="inner-content">
						
						<div class="row">
		
		<div class="col-lg-4 col-md-4 col-sm-6 block-parent">
			
			<div>
				<p class="t2">
					Маркетплейс для самозанятых
				</p>
				<p class="t3">
					Запусти продажи на базе маркетплейса от
					Wallet в качестве самозанятого!<br>
					Несомненные плюсы:<br>
					-Огромная аудитория<br>
					-Весь функционал сделан за Вас<br>
					-4% в качесиве самозанятого вместо 13% как физ. лица<br>
					-Не нужно регистрировать Юридическое лицо или ИП
					-Указан налог по договору купли-продажи между физическими лицами
				</p>
			</div>

		</div>

		<div class="col-lg-4 col-md-4 col-sm-6 block-parent">
			
			<div>
				<p class="t2">
					Игровые биржи
				</p>
				<p class="t3">
					Владеете биржей игровой валюты, аккаунтов, кейсов и скинов?<br>
					По достоинству оцените персональное предложение от Wallet:<br>
					-самые низкие комиссии на рынке: от 6%<br>
					СУММАРНО<br>
					-встраиваемые кошельки для пользователей<br>
					-индивидуальные подход<br>
					-современные технологии безопасности
				</p>
			</div>

		</div>

		<div class="col-lg-4 col-md-4 col-sm-6 block-parent">
			
			<div>
				<p class="t2">
					Краудфандинг
				</p>
				<p class="t3">
					Собираешь деньги на различные цели?<br>
					Планируешь обновление спальни или запуск собственного стартапа? Оцени простой и удобный сервис сбора средств от Wallet<br>
					Плюсы:<br>
					-без регистрации в качестве юр лица или самозанятого<br>
					-без сложных схем: просто и понятно для каждого!<br>
					-неограниченные лимиты сбора
				</p>


			</div>

		</div>

	</div>
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
  name: 'Capabilities',
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