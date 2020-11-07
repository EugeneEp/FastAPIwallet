<template>
  <div>
    <div v-if='success' class="alert alert-success" role="alert">{{ message }}</div>
    <div v-if='!success' class="alert alert-danger" role="alert">{{ message }}</div>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message','success'],
};
</script>