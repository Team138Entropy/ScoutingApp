const cool = require('cool-ascii-faces')
const express = require('express')
const fetch = require('node-fetch')
const json2csv = require('json2csv')
const path = require('path')
const PORT = process.env.PORT || 5000
const apiKey = process.env.APIKEY || process.argv[2]

if(!apiKey) throw new Error("No API key!")

express()
  .use(express.static(path.join(__dirname, 'public')))
  //.set('views', path.join(__dirname, 'views'))
  //.set('view engine', 'ejs')
  .get('/', (req, res) => res.render('pages/index'))
  .get('/cool', (req, res) => res.send(cool()))
  .get('/times', (req, res) => res.send(showTimes()))
	.get('/data.csv', (req, res) => {
		console.log("hi")
		// get our data
		fetch("https://strategy-e354.restdb.io/rest/strategy", {
			headers: {
		    "Content-Type": "application/json",
		    "X-Apikey": apiKey
		  }
		}).
		// make it json
		then(x=>{
			if(!x.ok) throw x
			return x.json()
		}).
		// make it csv
		then(data => {
			res.setHeader('Content-Type', 'text/csv')
			if(data.length)	res.write(json2csv.parse(data))
			res.end()
		}).
		catch(resp => {
			console.error(resp);
			res.error();
		})
	})
  .listen(PORT, () => console.log(`Listening on ${ PORT }`))

showTimes = () => {
  let result = ''
  const times = process.env.TIMES || 5
  for (i = 0; i < times; i++) {
    result += i + ' '
  }
  return result
}
