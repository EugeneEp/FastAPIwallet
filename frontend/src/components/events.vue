<template>
	<main>
		<infoHeader></infoHeader>
		<div class="container-custom">
			<div class="row">
				<indexLeft></indexLeft>
				<div class="col-10">
					<h5 class="inner-title">
	
						Частные мероприятия, ивенты

					</h5>
					<div class="inner-content">
						<p class="t2">
							Организуй концерты и вечеринки с любыми<br>
							объемами: просто и удобно!
						</p>

						<p class="t3">
							+запуск продаж без сайта<br>
							+поддержка социальных сетей и мессенджеров<br>
							+встроенные редактируемые окна оплаты (виджеты)<br>
							+операции в качестве физического лица
						</p>

						<p class="t4">
							Зачем Вам Wallet?
						</p>

						<p class="t3">
							На одной волне с аудиторией:<br>
							Для достижения максимального успеха оратор или продавец должен быть похож на свою аудиторию. Специально для<br>
							этого мы разработали уникальное решение - виджет оплаты. Принимайте платежи без сайта: любые <br>социальные сети и мессенджеры - будьте в тренде и оптимизируйте свои расходы уже сейчас!<br>
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
  name: 'Events',
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