<template>
    <div class="field has-addons has-addons-right">
  <p class="control">
    <span class="select">
      <select>
        <option>All</option>
        <option>News</option>
        <option>Modules</option>
         <option>Threats</option>
          <option>Measures</option>
      </select>
    </span>
  </p>
  <p class="control is-expanded">
    <input class="input" type="text" v-model="search" placeholder="Search">
  </p>
  <p class="control">
    <a class="button is-info">
      Advanced
    </a>
  </p>
</div>


    
</template>

<script>
    export default {
        data() {
        return {
            search:''
        }
        }
    }
</script>

