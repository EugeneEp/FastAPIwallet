<template>
	<main>
		<infoHeader></infoHeader>
		<div class="container-custom">
			<div class="row">
				<indexLeft></indexLeft>
				<div class="col-10">
					<h5 class="inner-title">
	
						Стриминг

					</h5>
					<div class="inner-content">
						
						<p class="t2">
							Рынок стриминга показывает стабильный рост в РФ в течении пары лет.<br>
							Несмотря на это, сервис донатов до сих пор не представил гибокого и<br>
							демократичного предложения по сбору пожертвований.
						</p>

						<p class="t3">
							Проводи трансляции с максимальной выгодой и широкими возможностями<br>
							+низкая комиссия<br>
							+система лояльности и промокодов<br>
							+настраиваемые виджеты оплаты и удобный личный кабинет
						</p>

						<p class="t4">
							Наша команда решила эту проблему и предоставляет Вам:
						</p>

						<p class="t3">
						
						-простую и понятную систему промокодов<br>
						-интеграцию со всеми популярныеми стриминговыми платформами<br>
						-самую низкую комиссию на рынку: всего 5.5% совокупной комиссии<br>
						-редактируемые виджеты и ссылки оплаты<br>
						-удобный и практичный личный кабинет<br>
						-Международный стандарт безопасности PCI DSS

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
  name: 'Stream',
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