<template>
    <div>
        <div class="field has-addons">
            <div class="control">
                <input class="input" type="text" v-model="search" placeholder="search">
            </div>
            <div class="control">
                <a class="button is-light">
              Search
            </a>
            </div>
    
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                search: ''
            }
        }
    }
</script>

