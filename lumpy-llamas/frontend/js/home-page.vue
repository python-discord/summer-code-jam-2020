<template>
  <div class="home-grid">
    <div class="home-calendar item">
      <h2>Calendar</h2>
      Some events probably
    </div>
    <div class="home-newsfeed item">
      <h2> Newsfeed</h2>
      <ul>
        <li>Fake news</li>
        <li>Llamas rule. Alpacas drool</li>
      </ul>
    </div>
    <div class="home-menu item">
      <h2>Menu</h2>
      <ol class="home-menu-options">
        <router-link :to="{ name: 'forum'}"><li>Forums</li></router-link>
        <li>Email</li>
        <li>Games</li>
        <li>Chat</li>
      </ol>
    </div>
  </div>
</template>

<style>
.home-grid .item {
  border-style: solid;
  border-width: 1px;
  padding: 0.5em;
}

.home-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

.home-menu {
  grid-column: span 2;
}

.home-menu-options li:before {
  content: "[" counters(item, ".") "] ";
  counter-increment: item;
}

</style>
