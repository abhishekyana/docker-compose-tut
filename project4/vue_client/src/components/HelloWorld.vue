<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click='logconsole()'>BUTTON</button>
    <button @click='logconsole_web()'>BUTTON webserver_service</button>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data(){
    return{
      msg:"HHEHEHEHEHEHHEHEHEH",
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
    logconsole_web(){
      console.log("BUTTON PRESSED INSIDE the logconsole_web");
      const path = 'http://webserver_service:5000/ping';
        axios.get(path)
        .then((res) => {
          console.log("INSIDE method webserver_service");
          console.log("BUTTON PRESSED webserver_service");
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
  }
}
}
</script>
