<template>
  <div id="app" class="">
    <Navigate></Navigate>
    <div class="">
      <Folders></Folders>
    </div>
  </div>
</template>

<script>
import Navigate from './components/Navigate.vue'
import Folders from "./components/Folders";

export default {
  name: 'App',
  components: {
    Navigate,
    Folders
  }
}
</script>

<style>

</style>
