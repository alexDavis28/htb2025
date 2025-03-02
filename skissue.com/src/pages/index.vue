<template>
  <div id="app">
    <canvas id="particles-canvas"></canvas>
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
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const username = ref('');

const handleLogin = async () => {
  if (username.value.trim() !== '') {
    console.log('Logging in:', username.value);
    window.location.href = 'userFiles.html';

    const message_response = await fetch('/api/login/' + username.value, {
      method: 'GET'
    });
    console.log('Response:', message_response);
  }
};

onMounted(() => {
  const canvas = document.getElementById('particles-canvas') as HTMLCanvasElement;
  const ctx = canvas.getContext('2d')!;
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const particlesArray: Particle[] = [];
  const numberOfParticles = 100;

  class Particle {
    x: number;
    y: number;
    size: number;
    speedX: number;
    speedY: number;
    color: string;
    alpha: number;

    constructor() {
      this.x = Math.random() * canvas.width;
      this.y = canvas.height;
      this.size = Math.random() * 70 + 1;
      this.speedX = Math.random() * 3 - 1.5;
      this.speedY = Math.random() * 1.5 * -1;
      this.color = 'rgba(0, 0, 0, 0.8)';
      this.alpha = 0.8;
    }

    update() {
      this.x += this.speedX;
      this.y += this.speedY;

      if (this.size > 0.2){
        this.size -= 0.1;
        this.alpha -= 0.05;
      }
    }

    draw() {
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.closePath();
      ctx.fill();
    }
  }

  function init() {
    for (let i = 0; i < numberOfParticles; i++) {
      particlesArray.push(new Particle());
    }
    console.log('Particles initialized:', particlesArray);
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particlesArray.forEach((particle, index) => {
      particle.update();
      particle.draw();

      if (particle.size <= 0.2) {
        particlesArray.splice(index, 1);
        particlesArray.push(new Particle());
      }
    });
    requestAnimationFrame(animate);
  }

  init();
  animate();

  window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  });
});
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