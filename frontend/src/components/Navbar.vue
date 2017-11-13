<template>
   <nav class="navbar is-dark">
  <div class="navbar-brand">
    <a class="navbar-item" href="/" >
      <img src="../assets/seel-logo.png"  width="112" height="28">
    </a>
    <div class="navbar-burger burger" data-target="navbarExampleTransparentExample">
      <span></span>
      <span></span>
      <span></span>
    </div>
  </div>

  <div id="navbarExampleTransparentExample" class="navbar-menu">
    <div class="navbar-start">
      <a class="navbar-item" href="/">
        Home
      </a>
    <a class="navbar-item" href="/">
        Browse BSI
      </a>
      <a class="navbar-item" href="/">
        Tutorials
      </a>
      <a class="navbar-item" href="/">
       Wizard
      </a>
  
      </div>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="field is-grouped">
          <p class="control">
            <app-search></app-search>
          </p>
          <p class="control">
            <a class="button is-primary" href="/login">
              
              <span>Login</span>
            </a>
          </p>
        </div>
      </div>
    </div>
  </div>
</nav>
</template>


<style scoped>
.navbar{
 
  position: fixed;
  width: 100%;
  padding-bottom:5px;
  padding-bottom:5px;
  z-index: 2;
  
}
</style>

