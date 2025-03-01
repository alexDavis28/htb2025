<script setup lang="ts">
import ContentBox from './ImageBox.vue'
import GraphBox from './GraphBox.vue'
defineProps<{
  imageDesc: string,
  boxType: string
}>()
</script>

<template>
  <div class="curved-square">
    <ContentBox v-if="boxType == 'Image'" :text="imageDesc" />
    <GraphBox v-else-if="boxType == 'Graph'" :text="imageDesc" />
  </div>
</template>

<style scoped>
.curved-square {
  width: 250px; /* Width of the square */
  height: 300px; /* Height of the square */
  background-color: #222A68; /* Background color of the square */
  border-radius: 20px; /* Curved corners */
  display: flex;
  justify-content: center; /* Center content horizontally */
  align-items: center; /* Center content vertically */
  margin: 10px; /* Add some margin for spacing */
}
</style>