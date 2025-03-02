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
  width: 250px; 
  height: 300px;
  background-color: #222A68;
  border-radius: 20px; 
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px; 
}
</style>