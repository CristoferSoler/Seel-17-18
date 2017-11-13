
<template>
  <body>
    <section class="section">
      <div class="columns">
        <div class="column">
          <app-news-imp></app-news-imp>
        </div>
        <div class="column">
          <app-news></app-news>
        </div>
      </div>
    </section>
  
    <section class="hero is-small is-primary is-bold ">
      <div class="hero-body">
        <div class="container">
          <div class="columns">
            <div class="column is-one-third is-left">
              <p class="title">
                Try the Advanced Search!
              </p>
            </div>
            <div class="column">
              <app-search-adv></app-search-adv>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="hero is-small">
      <div class="hero-body">
        <div class="container">
          <div class="columns">
            <div class="column is-half is-left">
              <app-tutor-list></app-tutor-list>
            </div>
            <div class="column">
              <div class="hero-body">
                <div class="container2 is-fluid has-text-centered">
                  <div class="tile">
                    <article class="tile is-child notification is-primary">
                      <p class="title">Wizard tool</p>
                      <br>
                      <div class="container1">
                      <figure class="image is-128x128">
                        <img src="/src/assets/Magic.ico" alt="Image">
                      </figure>
                      </div>
                    </article>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
     
    </section>
  
  </body>
</template>

<style scoped>
  body {
    padding-top: 40px;
    z-index: -2;
  }
  
  @media screen and (max-width: 1023px) {
    body {
      padding-top: 80px;
      z-index: -2;
    }
  }
  .container1{
  height: 10em;
  display: flex;
  align-items: center;
  justify-content: center 
  }


figure{
   margin: 0;
}
</style>

