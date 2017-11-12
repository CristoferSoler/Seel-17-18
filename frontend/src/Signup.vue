<template>
  <body>
    <section class="hero is-primary is-bold is-fullheight">
      <div class="hero-body">
        <div class="container is-fluid">
          <div class="column is-6 is-offset-3">
            <div class="box">
              <h3 class="title has-text-dark">Registration</h3>
              <form>
                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <label class="label">Name</label>
                  </div>
                  <div class="field-body">
                    <div class="field">
                      <div class="control">
                        <input class="input" type="text" placeholder="text input">
                      </div>
                    
                    </div>
                  </div>
                </div>
  
                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <label class="label">Username</label>
                  </div>
                  <div class="field-body">
                    <div class="field">
                      <div class="control">
                        <input class="input is-success" type="text" placeholder="username">
                      </div>
                      <p class="help is-success">
                        This field is required
                      </p>
                    </div>
                  </div>
                </div>
  
                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <label class="label">Email</label>
                  </div>
                  <div class="field-body">
                    <div class="field">
                      <div class="control">
                        <input class="input is-danger" type="email" placeholder="hello@">
                      </div>
                      <p class="help is-danger">
                        This field is required
                      </p>
                    </div>
                  </div>
                </div>
  
                <div class="field is-horizontal">
                  <div class="field-label is-normal">
                    <label class="label">Password</label>
                  </div>
                  <div class="field-body">
                    <div class="field">
                      <div class="control">
                        <input class="input is-danger" type="password" placeholder="****">
                      </div>
                      <p class="help is-danger">
                        This field is required
                      </p>
                    </div>
                  </div>
                </div>
  
  
                <div class="field is-horizontal">
                  <div class="field-label">
                    <!-- Left empty for spacing -->
  
                  </div>
                  <div class="field-body">
                    <div class="field">
                      <div class="control">
                        <label class="checkbox">
          <input type="checkbox">
          I agree to the <a href="#">terms and conditions</a>
        </label>
                      </div>
                    </div>
                  </div>
                </div>
  
                <div class="field is-horizontal">
                  <div class="field-label">
                    <!-- Left empty for spacing -->
  
                  </div>
                  <div class="field-body">
                    <div class="field is-grouped">
                      <div class="control">
                        <button class="button is-primary">
                       Submit
                      </button>
                      </div>
                      <div class="control">
                        <a class="button is-text" href="/login">Cancel</a>
                      </div>
                    </div>
                  </div>
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

@media screen and (max-width: 1023px){
  body{
    padding-top: 80px;
    z-index: -2;
  }
}
</style>