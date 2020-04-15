<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click='logconsole()'>BUTTON</button>
    <button @click='logconsole_web("abhishek")'>BUTTONNNn webserver_service</button>
    <button @click='logconsole_web("user_dataset")'>Delete</button>
    <button type="button"
            class="btn btn-danger btn-sm"
            v-on:click="logconsole_web('user_dataset')">Delete</button>
    <button type="button"
            class="btn btn-danger btn-sm"
            v-on:click="logconsole_web('user_dataset')"><b-icon icon="x-circle" scale="2" variant="danger"></b-icon></button>
    <b-icon-arrow-up></b-icon-arrow-up>
    <b-icon icon="exclamation-circle-fill" variant="success"></b-icon>

  </div>
</template>

<script>
import axios from 'axios';
import { BIcon, BIconArrowUp } from 'bootstrap-vue';
export default {
  components: {
    BIcon,
    BIconArrowUp
  },
  data(){
    return{
      msg:"Hellloooooooooo",
    }
  },
  methods:{
    logconsole(){
      console.log("BUTTON PRESSED");
      const path = 'http://localhost:5000/ping';
        axios.get(path)
        .then((res) => {
          console.log("INSIDE method");
          console.log("BUTTON PRESSED");
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    logconsole_web(expt){
      console.log("BUTTON PRESSED INSIDE the logconsole_web");
      this.$confirm("Are you sure? You want to delete the dataset?").then(() => {
        console.log("COnfirm is pressedddd");
        console.log(expt)
      }).catch((error) =>{
        console.error(error);
        console.log("Pressed cancellllll")
      });
  }
}
}
</script>
