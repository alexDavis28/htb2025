<template>
  <div id="app">
    <ParticleEffect />
    <div class="login-container">
      <div class="title">
        <h1>Skissue.com</h1>
      </div>
      <div class="login-box">
        <h2>Login</h2>
        <form @submit.prevent="handleLogin">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
          <button type="submit">Login</button>
          <br>
          <button type="submit" @click="registerUser()">Register</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import ParticleEffect from '../components/ParticleEffect.vue';

const username = ref('');
console.log(username);

const registerUser = async () => {
    if (username.value.trim() !== '') {
      console.log('Registering:', username.value);
      const message_response = await fetch("https://skissue.com/api/signup/"+username.value, {
        method: 'GET'
      });
      console.log("Response:", message_response);
      if (message_response.status === 200) {
        window.location.href = "userFiles.html";
      }

    }
}


const handleLogin = async () => {
   if (username.value.trim() !== '') {
    console.log('Logging in:', username.value);

      const message_response = await fetch('https://skissue.com/api/login/' + username.value, {
        method: 'GET'
      });
      console.log('Response:', message_response);
      if (message_response.status === 200) {
        window.location.href = "userFiles.html";
      }
  }
};
</script>

<style scoped>
:global(body) {
  background-color: #0F132E;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}


#particles-canvas {
  position: absolute;
  left: 0px;
  top: 100px;
  width: 100%;
  height: 100%;
  z-index: -1; /* Ensure particles are behind other content */
}


.login-container {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  left: 0px;
  top: 0px;
  width: 100%;
  height: 100%;
}

.title {
  margin-bottom: 20px;
}

.login-box {
  background-color: #ffffff;
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 300px;
}

.login-box h2 {
  margin-bottom: 20px;
}

.login-box form {
  display: flex;
  flex-direction: column;
}

.login-box label {
  margin-bottom: 5px;
  text-align: left;
}

.login-box input {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.login-box button {
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login-box button:hover {
  background-color: #45a049;
}

.login-box a {
  display: block;
  margin-top: 10px;
  color: #4CAF50;
  text-decoration: none;
}

.login-box a:hover {
  text-decoration: underline;
}

h1 {
  font-size: 2.6rem;
  margin-bottom: -10px;
  color: white;
}

h2 {
  font-size: 1.6rem;
  margin-bottom: 10px;
  color: #222A68;
}
</style>