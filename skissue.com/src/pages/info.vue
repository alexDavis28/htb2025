<script setup lang="ts">
import UpperContainer from '../components/UpperContainer.vue'
import LowerContainer from '../components/LowerContainer.vue';
</script>

<template>
  <div class="title">
    <h1>Skissue.com</h1>
    <h3>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</h3>
  </div>
  <div class="image-row-upper">
    <UpperContainer imageDesc="Image 1" boxType="Image" />
    <UpperContainer imageDesc="Image 2" boxType="Image" />
    <UpperContainer imageDesc="Graph 1" boxType="Graph" />
    <UpperContainer imageDesc="Graph 2" boxType="Graph" />
  </div>
  <br> <!-- Line break -->
  <div class="image-row-lower">
    <LowerContainer imageDesc="Image 1" boxType="Image"/>
    <LowerContainer imageDesc="Graph 3" boxType="Graph"/>
  </div>
  <a href="login.html" class="login-link">Go to Login</a>
</template>

<style scoped>
:global(body) {
  background-color: #0F132E;
}

.title {
  position: absolute; /* Fix the container relative to the viewport */
  top: 10px;
  left: 200px;
  width: 1200px; /* Adjust width as needed */
  height: 100px; /* Adjust height as needed */
  padding: 10px;
}

.image-row-upper {
  display: flex;
  justify-content: flex-start; /* Align items to the left */
  align-items: flex-start; /* Align items to the top */
  padding-left: 50px; /* Start from 200px left padding */
  margin-top: 125px; /* Adjust top margin as needed */
}

.image-row-lower {
  display: flex;
  justify-content: flex-start; /* Align items to the left */
  align-items: flex-start; /* Align items to the top */
  padding-left: 50px; /* Start from 200px left padding */
  margin-top: 10px; /* Adjust top margin as needed */
}

h1 {
  font-weight: 500;
  font-size: 2.6rem;
  margin: 0; /* Remove default margin */
  color: white;
}

h3 {
  font-weight: 300;
  font-size: 1.0rem;
  margin: 0; /* Remove default margin */
  color: #E2ADF2;
}
</style>