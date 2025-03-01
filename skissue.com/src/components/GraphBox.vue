<script setup lang="ts">
defineProps<{
  text: string
}>()
</script>

<template>
  <div class="graph-box">
    <p class="text">{{ text }}</p>
    <!-- Placeholder for the graph -->
    <div class="graph-placeholder">Graph goes here</div>
  </div>
</template>

<style scoped>
.graph-box {
  display: flex;
  flex-direction: column; /* Arrange items in a column */
  justify-content: flex-start; /* Align content to the top */
  align-items: center; /* Center content horizontally */
  width: 300%;
  height: 300px;
  position: relative;
}

.text {
  position: absolute;
  top: 15px;
  left: 15px;
  font-size: 1.2rem;
  color: white; /* Text color */
}


.graph-placeholder {
  background-color: #fff; /* Background color for the placeholder */
  border-radius: 10px; /* Rounded corners */
  margin-top: 60px;
  width: 90%;
  height: 225px;
  display: flex;
  justify-content: center;
}

</style>