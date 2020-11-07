<template>
	<main>
		<infoHeader></infoHeader>
		<div class="container-custom">
			<div class="row">
				<indexLeft></indexLeft>
				<div class="col-10">
					<h5 class="inner-title">
	
						Инфобизнес

					</h5>
					<div class="inner-content">
						<p class="t1">Зарабатывай на своих навыках без лишних хлопот</p>

						<p class="t2">
							+запуск продаж без сайта<br>
							+поддержка социальных сетей и мессенджеров<br>
							+встроенные редактируемые окна оплаты (виджеты)<br>
							+операции в качестве физического лица
						</p>

						<p class="t3">
							-Международный стандарт безопасности PCI DSS<br>
							-низкие комиссии<br>
							-новейшие IT Разрабоитки
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
  name: 'Business',
  data() {
    return {
      ajaxConfig: {
      	showModal: false,
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