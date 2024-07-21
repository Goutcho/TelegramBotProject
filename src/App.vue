<template>
  <div id="app">
    <main-page />
    <nav-bar />
  </div>
</template>

<script>
import MainPage from './components/MainPage/MainPage.vue';
import NavBar from './components/NavBar/NavBar.vue';

export default {
  name: 'App',
  components: {
    MainPage,
    NavBar
  }
};
</script>

<style>
/* Styles globaux */
</style>
