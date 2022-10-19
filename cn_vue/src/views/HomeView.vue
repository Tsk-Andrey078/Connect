<template>
  <div class="card dialogs_card bg-dark">
    <div class="card dialogs_title bg-dark">DIALOGS</div>
    <ul v-for="chat in chats" v-bind:key="chat.id">
      <router-link v-bind:to="chat.slug" class="chat_link">
        <li>
          <div class="card chat mb-3 bg-dark">
            <div class="name">{{chat.person_name}}</div>
            <div class="last_msg">{{chat.last_message}}</div>
          </div>
        </li>
      </router-link>
      
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
export default {
  name: 'HomeView',
  data() {
    return {
      chats: []
    }
  },
  mounted() {
    this.getLatestMessages()
  },
  methods: {
    getLatestMessages() {
      axios
        .get('/api/v1/messages/')
        .then(response => {
          this.chats = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style lang="sass">
  .dialogs_card
    margin: 0 auto
    margin-top: 30px
    padding: 20px 40px
    width: 50%
  .chat
    box-shadow: 1px 1px 8px #00c361
    font-size: 15px
    margin: 0 auto
    width:80%
    border: 2px solid #00c361
  .name
    padding: 2px 15px
    background-color: #00c361
  .last_msg
    color: #00c361
    padding: 2px 15px
  .chat_link
    &:link
      color: black
      text-decoration: none
    &:hover
      color: black
      text-decoration: none
    &:visited
      color: black
      text-decoration: none
    &:active 
      color: black
      text-decoration: none 
  .dialogs_title
    margin-bottom: 30px
    font-size: 24px
    text-align: center
    font-weight: bold
    color: #00c361
    border: 1px solid #00c361
    border-radius: 3px
    box-shadow: 3px 3px 15px #00c361
</style>
