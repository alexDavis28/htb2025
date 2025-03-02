<script setup lang="ts">
import GraphBox from './GraphBox2.vue'
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
  width: 520px; 
  height: 350px; 
  background-color: #222A68; 
  border-radius: 20px;
  display: flex;
  justify-content: center; 
  align-items: center;
  margin: 10px;
}
</style>