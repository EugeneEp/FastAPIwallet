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
								Кабинет партнера

								<span>Ваши личные данные</span>
							</h5>
						</div>
						<div class="col-lg-10 col-md-9">
							
						</div>
					</div>
					
				</div>
			</div>
		</div>
	</main>
</template>

<script>

	import walletHeader from './walletHeader'
	import walletLeft from './walletLeft'

export default {
  name: 'Partner',
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
    walletHeader: walletHeader,
    walletLeft: walletLeft
  },
  methods: {

  },
  created() {

  },
};
</script>