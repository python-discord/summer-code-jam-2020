# Lumpy Llamas

## Installation
Python 3.8
Create a virtual environment
```
python -m venv venv
. venv/bin/activate
```

```
pip install -r requirements.txt
```

## Server commands

Run the server
```
python manage.py runserver
```


## Workflow

Pull this repo
```
git clone git@github.com:CanaryWharf/summer-code-jam-2020.git
# OR
```

Create a new branch
```
git checkout -b branch-name-preferably-something-relevant
```

Add changed/added files
```
git add file1 folder/file2
```

Commit changes
```
git commit -m "Message summarising changes"
```

Push branch

```
git push -u origin branch-name-preferably-something-relevant
```

Create a pull request
 - on github.com go to "Pull Request"
 - Select your branch as the source branch
 - Select 'master' as the target branch
 - Create request



# Making frontend changes

## Compiling frontend
Make sure you have either `npm` or `yarn` installed.
Deployment will be done via yarn, so that is the recommended route

Then run
```
yarn install
yarn build
```

# OR
```
npm install
npm build
```


## Create a .vue file in `frontend/js`

.vue files have the specific html, css and js files in one go
Basic structure is this
```
<template>
    <div> HTML goes here</div>
</template>

<style>
.css-goes-here {
  color: blue;
}
</style>

<script>
import someModule from 'some-module';
// Javascript goes here
export default {
   data() {
     return {
       stuff: 'things';
     };
   },
}
</script>
```

You can build the frontend with yarn
`yarn build`
