<template>
    <div class="w3-row">


        <div class="w3-col s4  w3-center w3-white">
            <div class="head-folder">ПАПКА 1</div>
            <hr style="margin: 0">
            <p><v-jstree :data="data" show-checkbox multiple allow-batch whole-row @item-click="itemClick"></v-jstree></p>
        </div>
        <div class="w3-col s4 w3-center">
            <div class="w3-card w3-white central-folder">
                РЕЗУЛЬТАТ ОБЪЕДИНЕНИЯ
            </div>
        </div>
        <div class="w3-col s4  w3-center w3-white">
            <div class="head-folder">ПАПКА 2</div>
            <hr style="margin: 0">
        </div>
    </div>
</template>

<script>
    import VJstree from 'vue-jstree'
    import axios from 'axios'

    export default {
        name: "Folders",
        components: {
            VJstree
        },
        created() {
            axios.get("http://localhost:5050/gets-disk").then((data)=>{
                console.log(data.data)
                this.data = data.data
            })
        },
        data() {
            return {
                data: [{"text": "Unknown"}]
            }
        },
        methods: {
            itemClick (node) {
              console.log(node.model.text + ' clicked !')
            }
      }
    }

</script>

<style scoped>
    .central-folder{
        min-height: calc(100vh - 38px);
        margin-left: 3px;
        margin-right: 3px;
    }
    .head-folder{
        margin-top: 4px;
        margin-bottom: 4px;
    }
</style>