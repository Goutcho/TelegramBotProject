<template>
    <div class="main-page">
      <div class="logo-container">
        <img src="../../assets/tamia-logo.png" alt="logo-tamia" width="80" height="80" />
      </div>
      <div class="moulin-img">
        <img src="../../img/image-test_moulinet.png" alt="moulin-icon" width="300" height="300" />
      </div>
      <div class="crypto-info">
        <div>
          <p>{{ minedCrypto }} Crypto Monnaies Minées</p>
          <button @click="boostMining">Boost</button>
          <button @click="withdraw">Retirer</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        minedCrypto: 0
      };
    },
    methods: {
      boostMining() {
        // Logique pour augmenter la puissance de minage
      },
      withdraw() {
        // Logique pour retirer les cryptomonnaies
      }
    }
  };
  </script>
  
  <style scoped>
  /* Styles pour la page principale */
  .main-page {
    text-align: center;
  }
  
  .logo-container {
    background-color: #F5D504;
    width: 100%;
    padding: 20px 0; /* Ajustez le padding selon vos besoins */
  }
  
  .crypto-info {
    display: flex;
    justify-content: center;
    gap: 20px;
  }
  
  button {
    padding: 10px;
    margin: 25px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  