<template>
  <div class="layout">
    <Navbar />
    <main class="content">
      <slot />
    </main>
    <Footer />
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue';
import Navbar from '@/components/Navbar.vue';





export default {
  name: "DefaultLayout",
  components: { Navbar, Footer },
};
</script>

<style scoped>
.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.content {
  flex: 1;
  padding: 2rem;
}
</style>