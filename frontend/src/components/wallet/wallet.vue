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
								Мой кошелек
								<span>История операций</span>
							</h5>
						</div>
						<div class="col-lg-10 col-md-9">
							<div class="form-block">
								<form class="search-form form-inline">
									<a href="" class="trans-range" data-range='today'>За сегодня</a>
									<a href="" class="trans-range" data-range='yesterday'>За вчера</a>
									<a href="" class="trans-range" data-range='week'>За неделю</a>

									<div class="input-group">
								    	<div class="input-group-prepend">
								      		<div class="input-group-text">с</div>
								    	</div>
								    	<input type="date" class="form-control" v-model="sendData.date_from" value="">
								  	</div>

								  	<div class="input-group">
								    	<div class="input-group-prepend">
								      		<div class="input-group-text">по</div>
								    	</div>
								    	<input type="date" class="form-control" v-model="sendData.date_end" value="">
								  	</div>
								  	<input type="submit" class="btn btn-sm btn-light" value="Поиск">
								  	<a @click='sendData.date_from="";sendData.date_end="";openPage(1);'>Сбросить фильтры</a>
								</form>
							</div>
						</div>
					</div>
					<div class="text-left">
						<input @click='getCsv' type="button" data-action="csv" data-method="" class="btn btn-info action-btn" value="Выгрузить в CSV">
					</div>

					<table class="table">
						<thead>
							<tr>
								<th>Дата</th>
								<th>Тип транзакции</th>
								<th>Отправитель</th>
								<th>Получатель</th>
								<th>Статус</th>
								<th>Сумма</th>
							</tr>
						</thead>
						<tbody v-if='!preload'>
								<tr v-for='(v, k) in trans'>
									<td>{{v.time}}</td>
									<td>{{v.movement_type}}</td>
									<td></td>
									<td></td>
									<td>{{v.status}}</td>
									<td>{{v.amount}}</td>
								</tr>
						</tbody>
					</table>
					<nav>
						<ul class="pagination">
							<li class="page-item" :class='{"disabled":!paginator.has_prev}'><a class="page-link" @click='openPage(paginator.prev_num)'>Назад</a></li>

							
							<template v-if='paginator.pages && paginator.pages == paginator.page && paginator.pages !== paginator.next_num && ![1,2].includes(paginator.pages)'>
								<li class="page-item"><a class="page-link" @click='openPage(1)'>1</a>
								<li class="page-item disabled"><a class="page-link">...</a></li></li>
							</template>

							<template v-if='paginator.has_prev'>
								<li class="page-item"><a class="page-link" @click='openPage(paginator.prev_num)'>{{paginator.prev_num}}</a></li>
							</template>

							<li class="page-item active"><a class="page-link" @click='openPage(paginator.page)'>{{paginator.page}}</a></li>

					    	<template v-if='paginator.has_next'>
								<li class="page-item"><a class="page-link" @click='openPage(paginator.next_num)'>{{paginator.next_num}}</a></li>
							</template>

					    	<template v-if='paginator.pages && paginator.pages !== paginator.page && paginator.pages !== paginator.next_num'>
					    		<li class="page-item disabled"><a class="page-link">...</a></li>
								<li class="page-item"><a class="page-link" @click='openPage(paginator.pages)'>{{paginator.pages}}</a></li>
					    	</template>

							<li class="page-item" :class='{"disabled":!paginator.has_next}'><a class="page-link" @click='openPage(paginator.next_num)'>Вперед</a></li>
						</ul>
		</nav>
				</div>
			</div>
		</div>
	</main>
</template>

<script>

	import axios from 'axios'
	import walletHeader from './walletHeader'
	import walletLeft from './walletLeft'

export default {
  name: 'Wallet',
  data() {
    return {
    	showModal: false,
    	message: '',
    	success: '',
    	preload: true,
    	showMessage: false,
    	sendData: {
    		date_from:'',
    		date_end:'',
    		page:1
    	},
    	trans:{

    	},
    	paginator:{

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
    walletLeft: walletLeft
  },
  methods: {
  	getTrans(){
  		const path = 'http://127.0.0.1:8000/wallet/transactions';
	    axios.post(path, this.sendData, this.ajaxConfig)
			.then((res) => {
				this.trans = res.data.trans;
				this.paginator = res.data.paginator;
				this.preload = false;
        })
        .catch((error) => {
          this.message = error.response.data.message;
          this.success = false;
          console.log(this.message)
        });
  	},
  	getCsv(){
  		const path = 'http://127.0.0.1:8000/wallet/csv';
	    axios.post(path, this.sendData, this.ajaxConfig)
	      .then((res) => {
          
          this.message = res.data.msg;
          this.success = res.data.success;
          if(this.success)
          	location.href = res.data.link;
          else{

          }
        })
        .catch((error) => {
          this.message = error.response.data.message;
          this.success = false;
          console.log(this.message);
        });
  	},
  	openPage(page){
  		this.sendData.page = page;
  		this.getTrans();
  	}
  },
  created() {

  },
  mounted(){
  	this.getTrans()
  }
};
</script>