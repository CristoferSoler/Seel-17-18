<template>
  <body>
    <section class="hero is-primary is-bold is-fullheight">
      <div class="hero-body">
        <div class="container is-fluid has-text-centered">
          <div class="column is-4 is-offset-4">
            <h3 class="title has-text-light">Please login</h3>
            <div class="box">
         <form>
           <div class="field">
                  <div class="control">
                    <input class="input is-large" type="text" placeholder="Your Email" autofocus="">
                  </div>
                </div>
                <div class="field">
                  <div class="control">
                    <input class="input is-large" type="password" placeholder="Your Password">
                  </div>
                </div>
                 <div class="field">
                  <label class="checkbox">
                        <input type="checkbox">
                        Remember me
                  </label>
                </div>
                  <div class="field">
                  <a class="button is-block is-info is-medium">Login</a>
                </div>
                 <div class="field">
                  <a class="button is-text" href="/signup"> have not register yet? </a>
                </div>
         </form>
            </div>

          </div>
        </div>
      </div>
    </section>
  </body>
</template>



<style scoped>
  
</style>