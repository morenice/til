var fs = require('fs');

console.log('async read package.json');
fs.readFile('package.json', {encoding: 'utf8'}, (err, data) => {
  if (err) throw err;

  console.log('callback function.');
  //console.log(data);
});

console.log('sync read package.json');
fs.readFileSync('package-lock.json', {encoding: 'utf8'});

console.log('bye :)');
