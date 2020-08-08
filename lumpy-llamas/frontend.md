# Building frontend components

## Create the page

Create a file in frontend/js/filename.vue

Example file

Just copy the format for now. The parts you need to worry about are the <template> and <style>

and the method `getData()`

change the url of in axios.get to your api url
Axios will be expecting a json, which will be mappend to a javascript object (Which is basically a dictionary)

You can then access the data in the template with {{ }} tags

```
<template>
  <div v-if="ready"> # this tells the page to not render until the page is ready
      # access objects directly with {{ myStuff.heading }} is the JS equivalent of {{ myStuff['heading'] }}

    <h2 class="some-heading">Hello and welcome to {{ myStuff.heading }}</h2>
    Here is how to do a list
    # if myStuff is a list, you can do a list rendering like so
    <ul>
      <li v-for="item in myStuff">
        My item name is: {{item}}
      </li>
    </ul>
    # Links can be done like this
    <router-link :to="{ name: 'some_page_name' }">Click Here</router-link>
  </div>
</template>

<style>
.some-heading {
  font-size: xx-large;
  color: pink;
}
</style>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      myStuff: null,
      ready: false,
    };
  },
  beforeMount() {
    this.getData();
  },
  methods: {
    getData() {
      axios.get('/api/stuff').then((response) => {
        this.myStuff = response.data;
        this.ready = true;
      });
    },
  }
}
</script>
```


## adding to routes

Each route object is just a dictionary
open up `frontend/js/routes.js`, and add your page like so

```
import MySpecialPage from './filename.vue'

const routes = [
   ... # Other routes
   {
     path: /some/path, # This is not the same as the API path, but the url the user will see
     component: MySpecialPage,
     name: 'my_special_page' # unique name, this will be passed to <router-link>
      
   }

]

```


# Global prompt

The site uses a single prompt to aid navigation.
Note usage of this should be optional (exception of when the user needs to type. So still use links and buttons as normal, but there should be a callback for the button itself)

## Adding specific commands
Note all commands are strings (since they come from input)

```

...
methods: {
    initFunction() {
        this.$cmd.on('1', this.someFunction) # When user enters '1', do someFunction
        this.$cmd.on('/giphy', this.otherFunction) # When enters '/giphy', do otherFunction
    }
    someFunction() {
        //stuff
    }
    otherFunction() {
       //things
    }
}
...

```

## Asking for specific input

You can ask for specific function, and then after use a callback function like so


```
...
methods: {
    askForName() {
        this.$cmd.input('Enter name: ').then((userInput) => { // ask for user to enter something, Then do this function
            this.greet(userInput);
        });
    }
    greet(name) {
        console.log(`Hello ${name}`);
    }
}
...

```
