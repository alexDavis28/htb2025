<template>

  <div class="container">
    <div class="header-container">
      <h2 class="header">User files</h2>
      <button class="center-button" @click="triggerFileInput">Upload</button>
    </div>
    <input type="file" ref="fileInput" @change="handleFileChange" class="file-input" />
    <div class="curved-square">
      <div class="scrollable-content" id="file-list">
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

let urlParams = new URLSearchParams(window.location.search);
var userID = urlParams.get('user_id'); 
export const loadFiles = async () => {
  const message_response = await fetch("https://skissue.com/api/filelist/"+userID, {
    method: 'GET'
  });
  const message_json = await message_response.json();

  var files = message_json["files"];
  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    var d = document.createElement("div");
    d.setAttribute("id", file[1]);
    d.innerHTML = file[0];
    d.setAttribute("@click", "window.location.href = '/public/info.html?file_hash=" + file[1] + "'");    
    d.setAttribute("class", "individualTile");
    var list = document.getElementById("file-list");
    list?.appendChild(d);
  }
}

window.onload = loadFiles;

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
          console.log("Image URL:", imageSrc.value); 
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
  padding-left: 20px; 
  margin-bottom: 10px; 
}

.header {
    margin: 10px 0;
    color: white; 
    font-size: 2.0rem; 
    text-align: left; 
    width: 100%; 
    padding-left: 0px; 
  }


.center-button {
  position: relative;
  padding: 10px 20px; 
  background-color: #AB81CD; 
  color: white; 
  border: none;
  border-radius: 5px; 
  cursor: pointer; 
  left: -20px;
}

.center-button:hover {
  background-color: #E2ADF2; 
}

.file-input {
  display: none;
}

.curved-square {
  width: 520px; 
  height: 550px;
  background-color: #222A68; 
  border-radius: 20px; 
  display: flex;
  justify-content: center; 
  align-items: center; 
  margin: 10px;
  overflow: hidden;
}

.scrollable-content {
  width: 100%;
  height: 100%;
  overflow-y: auto; 
  padding: 10px; 
  box-sizing: border-box;
}

.individualTile {
  margin-bottom: 10px; 
  padding: 10px;
  background-color: #fff;
  border-radius: 5px; 
}
</style>