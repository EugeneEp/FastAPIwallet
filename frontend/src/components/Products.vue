<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Products</h1>
        <hr><br><br>
        <alert :message="message" :success="success" v-if='showMessage'></alert>
        <button type="button" class="btn btn-success btn-sm" @click='showModal = !showModal'>Add Product</button>
        <br><br>
        <div v-if='!preload'>
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Id</th>
                <th scope="col">Name</th>
                <th scope="col">Slug</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for='(v, k) in products'>
                <td>{{k}}</td>
                <td>{{v.name}}</td>
                <td><a href="">{{v.slug}}</a></td>
                <td>
                  <button type="button" class="btn btn-warning btn-sm" @click='updateModal(v)'>Update</button>
                  <button type="button" class="btn btn-danger btn-sm" @click='onDelete(v)'>Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>


            <div class="modal-mask" style="display: none;" v-show="showModal">
              <div class="modal-wrapper">

              <div class="modal-dialog" role="document">
                  <div class="modal-content">
                    <form @submit='onSubmit' @reset='onReset'>
                      <div class="modal-header">
                          <h5 class="modal-title">Add product</h5>
                          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true" @click="showModal = false">&times;</span>
                          </button>
                      </div>
                      <div class="modal-body">
                          <div class="form-group">
                            <input type="text" class="form-control" v-model="productsForm.name" required placeholder="Enter title">
                          </div>
                          <div class="form-group">
                            <textarea placeholder="Enter description" class="form-control" v-model="productsForm.description" required></textarea>
                          </div>
                      </div>
                      <div class="modal-footer">
                          <button type="reset" class="btn btn-secondary" >Reset</button>
                          <button type="submit" class="btn btn-primary">Add product</button>
                      </div>
                    </form>
                  </div>
              </div>

              </div>
            </div>

            <div class="modal-mask" style="display: none;" v-show="showUpdateModal">
              <div class="modal-wrapper">

              <div class="modal-dialog" role="document">
                  <div class="modal-content">
                    <form @submit='onSubmitUpdate' @reset='onReset'>
                      <input type="hidden" v-model="productsFormUpdate.id">
                      <div class="modal-header">
                          <h5 class="modal-title">Update product</h5>
                          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true" @click="showUpdateModal = false">&times;</span>
                          </button>
                      </div>
                      <div class="modal-body">
                          <div class="form-group">
                            <input type="text" class="form-control" v-model="productsFormUpdate.name" required placeholder="Enter title">
                          </div>
                          <div class="form-group">
                            <textarea placeholder="Enter description" class="form-control" v-model="productsFormUpdate.description" required></textarea>
                          </div>
                      </div>
                      <div class="modal-footer">
                          <button type="reset" class="btn btn-secondary">Cancel</button>
                          <button type="submit" class="btn btn-primary">Update product</button>
                      </div>
                    </form>
                  </div>
              </div>

              </div>
            </div>

  </div>
</template>
<script>

import axios from 'axios';
import Alert from './Alert'

export default {
  name: 'Products',
  data() {
    return {
      preload: true,
      products: {},
      productsForm: {
        name: '',
        description: ''
      },
      productsFormUpdate: {
        id: '',
        name: '',
        description: ''
      },
      showModal: false,
      showUpdateModal: false,
      showMessage: false,
      message: '',
      success: true,
      ajaxConfig: {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getProducts() {
      const path = 'http://127.0.0.1:1337/py_products';
      axios.get(path)
        .then((res) => {
          this.products = res.data.products;
          this.preload = false;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    updateModal(product) {
      this.showUpdateModal = !this.showUpdateModal;
      console.log(product);
      this.productsFormUpdate = product;
    },
    onSubmit(e) {
      e.preventDefault();
      this.showModal = false;
      const path = 'http://127.0.0.1:1337/py_products';
      axios.post(path, this.productsForm)
        .then((res) => {
          console.log(res.data)
          this.getProducts();
          this.initForm();
          this.message = res.data.msg;
          this.success = res.data.success;
          console.log(res.data.success);
          this.showMessage = true;
          setTimeout(() => {
            this.showMessage = false;
          }, 3000);
        })
        .catch((error) => {
          console.error(error);
        });
    },onSubmitUpdate(e) {
      e.preventDefault();
      this.showUpdateModal = false;
      const path = 'http://127.0.0.1:1337/py_products';
      axios.put(path, this.productsFormUpdate)
        .then((res) => {
          console.log(res.data)
          this.getProducts();
          this.initForm();
          this.message = res.data.msg;
          this.success = res.data.success;
          console.log(res.data.success);
          this.showMessage = true;
          setTimeout(() => {
            this.showMessage = false;
          }, 3000);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    onReset(e) {
      e.preventDefault();
      this.getProducts();
      this.initForm();
      this.showUpdateModal = false;
    },
    onDelete(product) {
      const path = 'http://127.0.0.1:1337/py_products?id='+product.id;
      axios.delete(path)
        .then((res) => {
          this.getProducts();
          this.initForm();
          this.message = res.data.msg;
          this.success = res.data.success;
          console.log(res.data);
          this.showMessage = true;
          setTimeout(() => {
            this.showMessage = false;
          }, 3000);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    initForm(){
      this.productsForm.name = '';
      this.productsForm.description = '';
      this.productsFormUpdate.id = '';
      this.productsFormUpdate.name = '';
      this.productsFormUpdate.description = '';
    }
  },
  created() {
    this.getProducts();
  },
};
</script>