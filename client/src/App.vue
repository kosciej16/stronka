<template>
  <Tile @click="this.var=1"/>
  <Tile @click="this.var=2"/>
  <Kontakt v-if="this.var==1" />
  <About v-if="this.var==2" />
  <router-view />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Kontakt from './components/Kontakt.vue'
import About from './components/About.vue'
import Tile from './components/Tile.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Kontakt,
    About,
    Tile
  },
  data() {
     return {
         var: 0
     }
  }
}
</script>
