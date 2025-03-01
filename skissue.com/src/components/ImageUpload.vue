<template>
    <div class="container">
      <h2 class="header">Optical</h2>
      <div class = "placeholder"></div>
      <h2 class="header">Satellite</h2>
      <div class = "placeholder"></div>
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
  
  .header {
    margin: 10px 0; /* Add some margin above and below the header */
    color: white; /* Set the header text color */
    font-size: 2.0rem; /* Set the header font size */
    text-align: left; /* Align the header text to the left */
    width: 100%; /* Ensure the header takes the full width of the container */
    padding-left: 10px; /* Add some padding to the left */
  }

  .placeholder {
  width: 200px; /* Width of the placeholder */
  height: 200px; /* Height of the placeholder */
  background-color: #000000; /* Black background color */
  border-radius: 20px; /* Curved corners */
  display: flex;
  position: relative;
  left: 150px;
  align-items: center; /* Center content vertically */
  margin-bottom: 10px; /* Add some margin below the placeholder */
}

.uploaded-image {
  max-width: 100%;
  max-height: 100%;
  border-radius: 20px; /* Match the border radius of the placeholder */
}
  </style>