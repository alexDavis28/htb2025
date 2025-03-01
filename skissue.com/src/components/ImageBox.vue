<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
  props: {
    text: {
      type: String,
      required: true
    }
  },
  setup(props) {
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

    return {
      props,
      imageSrc,
      fileInput,
      handleFileChange,
      triggerFileInput
    };
  }
});
</script>

<template>
  <div class="content-box">
    <p class="text">{{ text }}</p>
    <div class="image-container" v-if="imageSrc">
      <img :src="imageSrc" alt="Uploaded Image" class="uploaded-image" />
    </div>
  </div>
</template>

<style scoped>
.content-box {
  display: flex;
  flex-direction: column; /* Arrange items in a column */
  justify-content: flex-start; /* Align content to the top */
  align-items: center; /* Center content horizontally */
  width: 100%;
  height: 100%;
  position: relative;
}

.text {
  position: absolute;
  top: 15px;
  left: 15px;
  font-size: 1.2rem;
  color: white; /* Text color */
}

.image-container {
  margin-top: 60px;
  width: 100%;
  display: flex;
  justify-content: center;
}

.uploaded-image {
  max-width: 100%;
  max-height: 225px; /* Adjust as needed */
  border-radius: 10px;
}

.center-button {
  position: absolute;
  top: 15px;
  left: 200px;
  transform: translateX(-50%); /* Center the button horizontally */
  padding: 8px 15px; /* Button padding */
  background-color: #AB81CD; /* Button background color */
  color: white; /* Button text color */
  border: none; /* Remove default border */
  border-radius: 5px; /* Rounded corners */
  cursor: pointer; /* Pointer cursor on hover */
}

.center-button:hover {
  background-color: #E2ADF2; /* Lighter color on hover */
}

.file-input {
  display: none; /* Hide the file input */
}
</style>