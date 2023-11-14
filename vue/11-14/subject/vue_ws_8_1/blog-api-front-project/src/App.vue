<template>
  <div>
    <nav class="bg-dark p-3 text-center">
      <RouterLink :to="{name:'home'}" class="text-white text-decoration-none fw-bold"> Home &nbsp; </RouterLink>
      <RouterLink :to="{name:'postList'}" class="text-white text-decoration-none fw-bold"> PostList &nbsp; </RouterLink>
      <RouterLink :to="{name:'category'}" class="text-white text-decoration-none fw-bold"> CategoryCreate </RouterLink>
    </nav>
  </div>

  <RouterView />
</template>

<script setup>

</script>

<style scoped>

</style>