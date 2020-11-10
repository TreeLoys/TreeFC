<template>
    <div class="w3-row">


        <div class="w3-col s4  w3-center w3-white">
            <div class="head-folder">ПАПКА 1</div>
            <hr style="margin: 0">
            <p><v-jstree :data="data" :async="loadData" show-checkbox multiple allow-batch whole-row  ref="tree2"></v-jstree></p>
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
            axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
        },
        mounted() {
        },
        data() {
            return {
                data: [],
                loadData: function (oriNode, resolve) {
                    if (oriNode.data.id === undefined){
                        axios.get("http://localhost:5050/gets-disk").then((data)=>{
                            resolve(data.data)
                        })
                    }else{
                        console.log(oriNode, "oriNodeClicked")
                        axios.post("http://localhost:5050/click-browse", {fullpath: oriNode.data.fullpath}).then((data)=>{
                            resolve(data.data)
                        })
                    }
                }
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