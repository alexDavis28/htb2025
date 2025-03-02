<template>
    <div class="circle"></div>
  </template>
  
  <script setup lang="ts">
  </script>
  
  <style scoped>
  .circle {
    width: 50px;
    height: 50px;
    background-color: #AB81CD;
    border-radius: 50%;
    position: absolute;
    animation: moveAround 5s infinite alternate;
  }
  
  @keyframes moveAround {
    0% {
      top: 0;
      left: 0;
    }
    25% {
      top: 0;
      left: calc(100% - 50px);
    }
    50% {
      top: calc(100% - 50px);
      left: calc(100% - 50px);
    }
    75% {
      top: calc(100% - 50px);
      left: 0;
    }
    100% {
      top: 0;
      left: 0;
    }
  }
  </style>