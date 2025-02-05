const sql_file_path = 'server/us-census.db';
const table_name = 'census_learn_sql';

module.exports = {
  sql_file_path,
  sql: {
    schema: 'PRAGMA table_info(' + table_name + ')',
    statistics: 'SELECT `?` AS id, COUNT(*) AS count, ROUND(AVG(age), 0) AS average FROM ' + table_name + ' WHERE `?` IS NOT NULL group by `?` ORDER BY COUNT(*) DESC LIMIT 100;',
    count: 'SELECT COUNT(*) AS count FROM ( SELECT `?` FROM ' + table_name + ' WHERE `?` IS NOT NULL group by `?`);'
  }
};
