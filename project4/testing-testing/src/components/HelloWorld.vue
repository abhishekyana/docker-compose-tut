<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click='logconsole()'>BUTTON</button>
  </div>
</template>

<script>
import axios from 'axios';
export default {
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
    }
  }
}
</script>
