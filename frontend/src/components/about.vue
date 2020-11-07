<template>
	<main>
		<infoHeader></infoHeader>
		<div class="container-custom">
			<div class="row">
				<indexLeft></indexLeft>
				<div class="col-10">
					<h5 class="inner-title">
	
						О нас

					</h5>
					<div class="inner-content">
						
						<p class="t3">
						«Сервис, который выгоден каждому!»

						<br><br>

						Именно этими словами руководствовалась наша команда при разработке электронного кошелька Wallet. Успешно внедрив решения в области технологий<br>
						и безопасности, применявшиеся нами при создании нашей платежной системой, перед командой встала куда более сложная задача: создать такой кошелек,<br>
						который будет удовлетворять запросам КАЖДОГО потенциального пользователя в эпоху цифровых технологий.<br>
						Задача была решена, не нарушая наших основных принципов:<br><br>

						Удобство<br>
						Абсолютные возможности для торговли:<br>
						-массовые выплаты физическим лицам<br>
						-Автоплатежи платежи<br>
						-ссылкм м виджеты для оплаты: продавайте в социальных сетях, мессенджерах<br>
						и чатах - никаких сайтов, запуск продаж с первого дня и без вложений<br>
						-совместный сбор средств<br>
						-прием донатов и пожертвований для стримеров<br>
						-простая и понятная программа лоялности, море бонусов<br><br>

						Безопасность<br>
						Полное соответствие закону:<br>
						Сервис Wallet работает в полном соответствии с 115 и 161 ФЗ.<br>
						Fraud мониторинг<br>
						Мы используем мощную систему Fraud мониторинга и незамедлительно<br>
						пресекаем неправовое использование сервиса.
						Ежедневная отчетность<br>
						Онлайн-статистика в личном кабинете
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
  name: 'About',
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