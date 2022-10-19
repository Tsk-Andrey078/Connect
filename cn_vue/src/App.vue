<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-dark">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand cn_logo">CONNECT</router-link>
      <router-link to="/profile" class="navbar-brand cn_logo cn_acc">Account</router-link>
    </div>
  </nav>

  <section class="section">
    <router-view />
  </section>
</template>

<style lang="sass">
@import ~bootstrap/dist/css/bootstrap.css
body
  background-color: #373737
.cn_logo
  text-shadow: 1px 1px 19px #00c361
  font-size: 24px
  font-weight: bold
  font-family: Arial, Helvetica, sans-serif
  color: #00c361
  &:hover
    color: #00c361  
.cn_acc
  font-size: 16px
  border: 1px solid #00c361
  padding: 6px 12px
  border-radius: 3px
  box-shadow: 3px 3px 15px #00c361 
</style>
