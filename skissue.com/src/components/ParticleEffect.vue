<template>
    <canvas id="particles-canvas"></canvas>
  </template>
  
  <script setup lang="ts">
  import { onMounted } from 'vue';
  
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
  
        if (this.size > 0.2) {
          this.size -= 0.1;
          this.alpha -= 0.001;
          this.alpha = Math.max(0, this.alpha);
          this.color = 'rgba(0, 0, 0,' + this.alpha + ')';
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
      init(); // Reinitialize particles to fit the new canvas size
    });
  });
  </script>
  
  <style scoped>
  #particles-canvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1; /* Ensure particles are behind other content */
  }
  </style>