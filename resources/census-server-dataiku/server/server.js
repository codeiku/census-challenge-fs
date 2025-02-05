'use strict';
const path = require('path');
const express = require('express');
const dbUtils = require('./dbUtils');

const app = express();
app.use(express.static(path.join(__dirname, '/')));

// Allows you to set port in the environment variables.
app.set('port', process.env.CENSUS_SERVER_PORT || 4000);

// Register API routes (starts with /api)
const router = express.Router();
router.get('/', (req, res) => {
  res.json({message: 'API'});
});
app.use('/api', router);

/*
 * GET /api/columns
 * Retrieve names of all columns
 */
router.get('/columns', (req, res) => {
  dbUtils.getColumns(res);
});

/*
 * GET /api/data/:id
 * Retrieve statistics over one column represented by 'id'
 */
router.get('/data/:id', (req, res) => {
  dbUtils.getStatistics(res, req.params.id);
});

// Run express
const server = app.listen(app.get('port'), () => {
  console.log('process.env.NODE_ENV = ' + process.env.NODE_ENV);
  dbUtils.connect(); // Init database
  console.log('');
  console.log('******************');
  console.log('* Server STARTED *');
  console.log('******************');
  console.log('Open the following url in your browser to test the server: http://localhost:'+ app.get('port')+'/api/columns');
});

module.exports = server;
