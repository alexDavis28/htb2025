<script setup lang="ts">
//Ignore the fact that this is named Cnormal container
//I am halfway insane and i do not want to look for names rn
import normalContainer from '../components/normalImage.vue'
import imageUploadfrom from '../components/ImageUpload.vue'
import ParticleEffect from '../components/ParticleEffect.vue';
</script>

<template>
  <ParticleEffect />
  <div class="title">
    <h1>Skissue.com</h1>
    <h3>Upload images, then select optical then satellite images to recieve an enhanced image.</h3>
  </div>
  <div class="image-row-upper">
    <normalContainer/>
    <imageUploadfrom/>
  </div>
  <div class="top-right-text">
    <p>Top Right Text</p>
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

.top-right-text {
  position: absolute;
  top: 45px;
  right: 245px;
  color: white;
  font-size: 1.2rem;
  text-align: right;
}
</style>