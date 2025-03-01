<template>
    <div class="container">
      <div class="placeholder">
        <img v-if="imageSrc" :src="imageSrc" alt="Uploaded Image" class="uploaded-image" />
      </div>
      <div class="curved-square">
        <!-- Scrollable content inside the curved square -->
        <div class="scrollable-content">
          <div class="individualTile">asd</div>
          <div class="individualTile">More content...</div>
          <div class="individualTile">Even more content...</div>
          <div class="individualTile">Content goes here</div>
          <div class="individualTile">More content...</div>
          <div class="individualTile">Even more content...</div>
          <div class="individualTile">Content goes here</div>
          <div class="individualTile">More content...</div>
          <div class="individualTile">Even more content...</div>
          <div class="individualTile">asd</div>
          <div class="individualTile">More content...</div>
          <div class="individualTile">Even more content...</div>
          <div class="individualTile">Content goes here</div>
          <div class="individualTile">More content...</div>
          <div class="individualTile">Even more content...</div>
          <div class="individualTile">Content goes here</div>
          <div class="individualTile">More content...</div>
          <div class="individualTile">Even more content...</div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  
  const imageSrc = ref('');
  const fileInput = ref<HTMLInputElement | null>(null);
  
  const handleFileChange = (event: Event) => {
    const target = event.target as HTMLInputElement;
    const file = target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        imageSrc.value = (e.target as FileReader).result as string;
      };
      reader.readAsDataURL(file);
    }
  };
  
  const triggerFileInput = () => {
    fileInput.value?.click();
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .placeholder {
    width: 250px; /* Width of the placeholder */
    height: 250px; /* Height of the placeholder */
    background-color: #000000; /* Black background color */
    border-radius: 20px; /* Curved corners */
    display: flex;
    justify-content: center; /* Center content horizontally */
    align-items: center; /* Center content vertically */
    margin-bottom: 10px; /* Add some margin below the placeholder */
  }
  
  .uploaded-image {
    max-width: 100%;
    max-height: 100%;
    border-radius: 20px; /* Match the border radius of the placeholder */
  }
  
  .curved-square {
    width: 520px; /* Width of the square */
    height: 350px; /* Height of the square */
    background-color: #222A68; /* Background color of the square */
    border-radius: 20px; /* Curved corners */
    display: flex;
    justify-content: center; /* Center content horizontally */
    align-items: center; /* Center content vertically */
    margin: 10px; /* Add some margin for spacing */
    overflow: hidden; /* Hide overflow */
  }
  
  .scrollable-content {
    width: 100%;
    height: 100%;
    overflow-y: auto; /* Enable vertical scrolling */
    padding: 10px; /* Add some padding */
    box-sizing: border-box; /* Include padding in the element's total width and height */
  }
  
  .individualTile {
    color: white;
    background-color: #2e377e;
    border-radius: 20px;
    padding-left: 10px; /* Add padding to the left */
    margin-bottom: 10px; /* Add some margin at the bottom for spacing */
  }
  </style>