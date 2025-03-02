<script setup lang="ts">
import UpperContainer from '../components/UpperContainer.vue'
import LowerContainer from '../components/LowerContainer.vue';
import ParticleEffect from '../components/ParticleEffect.vue';

const goToUserFiles = () => {
  window.location.href = 'userFiles.html';
};
</script>

<template>
  <ParticleEffect />
  <div class="title">
    <h1>Sattelite image analysis</h1>
    <h3>Enhanced image with data analysis.</h3>
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
  <div class="top-right-button">
    <button @click="goToUserFiles">User Files</button>
  </div>
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

.top-right-button button {
  position: absolute;
  padding: 10px 20px; /* Button padding */
  color: white; /* Button text color */
  border: none; /* Remove default border */
  border-radius: 5px; /* Rounded corners */
  cursor: pointer; /* Pointer cursor on hover */
  top: 40px;
  right: 245px;
  font-size: 1.2rem;
  background-color: #ffffff00; 
}

.top-right-button button:hover {
  background-color: #ffffff4f; /* Darker green on hover */
}
</style>