<template>
  <h1>{{ msg }}</h1>
  <button @click="method()">count is: {{ count }}</button>
  <p>Edit <code>components/HelloWorld.vue</code> to test hot module replacement.</p>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      count: 0
    }
  },
  methods: {
      method() {
          this.$router.push("/foo")
      }
  }
}
</script>

<style>
h1 {
    font-size: 7em
}

</style>
