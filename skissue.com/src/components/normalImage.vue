<template>
  <div class="container">
    <div class="header-container">
      <h2 class="header">Header Text</h2>
      <button class="center-button" @click="triggerFileInput">Upload</button>
    </div>
    <input type="file" ref="fileInput" @change="handleFileChange" class="file-input" />
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

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
  setup() {
    const imageSrc = ref<string | null>(null);
    const fileInput = ref<HTMLInputElement | null>(null);

    const handleFileChange = (event: Event) => {
      const target = event.target as HTMLInputElement;
      const file = target.files?.[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          imageSrc.value = (e.target as FileReader).result as string;
          console.log("Image URL:", imageSrc.value); // Log the image URL
        };
        reader.readAsDataURL(file);
      }
    };

    const triggerFileInput = () => {
      fileInput.value?.click();
    };

    return {
      imageSrc,
      fileInput,
      handleFileChange,
      triggerFileInput
    };
  }
});
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header-container {
  display: flex;
  align-items: center;
  width: 100%;
  padding-left: 20px; /* Add some padding to the left */
  margin-bottom: 10px; /* Add some margin below the header container */
}

.header {
  color: white; /* Set the header text color */
  font-size: 1.5rem; /* Set the header font size */
  margin-right: 20px; /* Add some margin to the right of the header */
}

.center-button {
  padding: 10px 20px; /* Button padding */
  background-color: #4CAF50; /* Button background color */
  color: white; /* Button text color */
  border: none; /* Remove default border */
  border-radius: 5px; /* Rounded corners */
  cursor: pointer; /* Pointer cursor on hover */
  margin-left: 265px;
}

.center-button:hover {
  background-color: #45a049; /* Darker green on hover */
}

.file-input {
  display: none; /* Hide the file input */
}

.curved-square {
  width: 520px; /* Width of the square */
  height: 550px; /* Height of the square */
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
  margin-bottom: 10px; /* Add some margin between tiles */
  padding: 10px;
  background-color: #fff; /* Background color for tiles */
  border-radius: 5px; /* Rounded corners for tiles */
}
</style>