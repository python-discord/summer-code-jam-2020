const express = require('express')
const app = express()
const port = 3000
var path = require('path')

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/src/index.html'));
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)

})