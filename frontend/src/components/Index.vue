<template>
	<main>
		<indexHeader></indexHeader>
		<div class="container-custom">
			<div class="row">
				<indexLeft></indexLeft>
				<div class="col-10">
					<div class="index-page">
						
						<h1>Wallet</h1>

						<h4>Электронный кошелек нового<br>поколения</h4>

						<p>
							Сервис, который выгоден каждому!<br>
							- Продажи в социальных сетях<br>
							- Продажи в мессенджерах<br>
							- Оплата услуг<br>
							- Гейминг<br>
							- Массовые выплаты<br>
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

	import indexHeader from './indexHeader'
	import indexLeft from './indexLeft'
	import indexFooter from './indexFooter'

export default {
  name: 'Index',
  data() {
    return {
    	showModal: false,
    	ajaxConfig: {
	        headers: {
	          'Content-Type': 'application/x-www-form-urlencoded'
	        }
		},
    };
  },
  components: {
    indexHeader: indexHeader,
    indexLeft: indexLeft,
    indexFooter: indexFooter
  },
  methods: {

  },
  created() {

  },
};
</script>