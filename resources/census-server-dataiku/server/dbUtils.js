'use strict';
const sqlite3 = require('sqlite3').verbose();
const config = require('../configuration.js');

module.exports = {
  db: false,
  connect() {
    console.log('Connection to DB');
    this.db = new sqlite3.Database(config.sql_file_path);
  },

  close() {
    if (this.db) {
      console.log('Close DB');
      this.db.close(function (err) {
        if (err) {
          console.error(err);
        }
        this.db = false;
      });
    }
  },

  getColumns(res) {
    const query = config.sql.schema;
    this.db.all(query, (err, rows) => {
      if (err) {
        console.error(err);
      }
      res.json({columns: rows.map(x => x.name)});
    });
  },

  getStatistics(res, column) {
    const query = config.sql.statistics.split('?').join(column);

    const queryCount = config.sql.count.split('?').join(column);

    this.db.all(query, (err, rows) => {
      if (err) {
        console.error(err);
        console.error('query = ' + query);
      }
      this.db.get(queryCount, (err, count) => {
        if (err) {
          console.error(err);
          console.error('queryCount = ' + queryCount);
        }
        if (count.count) {
          count = count.count;
        }

        res.json({values: rows, count});
      });
    });
  }
};
