<template>
    <div class="login-container">
      <h1>Login</h1>
      <form @submit.prevent="handleLogin">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required />
  
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
  
        <button type="submit">Login</button>
      </form>
      <a href="index.html">Back to Home</a>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref } from "vue";
  
  const username = ref("");
  const password = ref("");
  
  const handleLogin = () => {
    console.log("Logging in:", username.value, password.value);
  };
  </script>
  
  <style scoped>
  .login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #0F132E;
    color: white;
  }
  
  input {
    display: block;
    margin-bottom: 10px;
  }
  </style>
  