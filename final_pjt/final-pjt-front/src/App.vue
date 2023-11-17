<template>
  <div>
    <nav>
      <RouterLink :to="{ name: 'main' }">Home</RouterLink> /
      <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink> /
      <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink>
    </nav>

  </div>
  <RouterView />
</template>

<script setup>

</script>

<style scoped>

</style>