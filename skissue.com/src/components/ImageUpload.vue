<template>
    <div class="container">
      <h2 class="header">Optical</h2>
      <div class = "placeholder"></div>
      <button class="confirm-button" @click="confirmUpload">Confirm</button>
      <h2 class="header">LIDAR</h2>
      <div class = "placeholder"></div>
      <button class="confirm-button" @click="confirmUpload2">Confirm</button>
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

  const confirmUpload = () => {
  if (imageSrc.value) {
    console.log("Image confirmed:", imageSrc.value);
    // Add your confirmation logic here
  } else {
    console.log("No image to confirm");
  }
};
const confirmUpload2 = () => {
  window.location.href = "info.html";
  if (imageSrc.value) {
    console.log("Image confirmed:", imageSrc.value);
    // Add your confirmation logic here
  } else {
    console.log("No image to confirm");
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
  width: 175px; /* Width of the placeholder */
  height: 175px; /* Height of the placeholder */
  background-color: #44255e; /* Black background color */
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

.confirm-button {
  position: relative;
  left: 150px;
  padding: 10px 20px; /* Button padding */
  background-color: #AB81CD; /* Button background color */
  color: white; /* Button text color */
  border: none; /* Remove default border */
  border-radius: 5px; /* Rounded corners */
  cursor: pointer; /* Pointer cursor on hover */
  margin-top: 10px; /* Add some margin above the button */
}

.confirm-button:hover {
  background-color: #E2ADF2; /* Darker green on hover */
}

.file-input {
  display: none; /* Hide the file input */
}
  </style>