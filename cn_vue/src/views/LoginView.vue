<template>
    <div class="card login_card bg-dark">
        <div class="login_text">WELCOME TO THE SYSTEM</div>
        <div class="input-group mb-3 bg-dark">
            <span class="input-group-text bg-dark" id="username">@</span>
            <input type="text" class="form-control bg-dark" placeholder="Username" aria-label="Username" aria-describedby="username">
        </div>

        <div class="input-group mb-3 bg-dark">
            <span class="input-group-text bg-dark" id="password">PS</span>
            <input type="text" class="form-control bg-dark" placeholder="Password" aria-label="Password" aria-describedby="password">
        </div>

        <button type="button" class="btn btn-success btn-login">Log In</button>
    </div>
</template>

<script>
export default {
  name: 'LoginView',
  components: {
  }
}
</script>

<style lang='sass'>
.login_card
    margin: 0 auto
    width: 35%
    padding: 50px 25px
    margin-top: 100px

.input-group-text
    box-shadow: 3px 3px 10px #00c361
    color: #00c361
    border-color: #00c361

.form-control
    box-shadow: 3px 3px 10px #00c361
    border-color: #00c361

.btn-login
    background-color: #00c361
    box-shadow: 1px 1px 8px #00c361

.login_text
    color: #00c361
    margin: 0 auto
    margin-bottom: 15px
    font-size: 24px
</style>