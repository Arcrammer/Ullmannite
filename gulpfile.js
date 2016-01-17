var gulp = require('gulp');
var exec = require('child_process').exec;

gulp.task('default', function () {
  // Start the development server
  exec('python manage.py runserver');

  // Start Browser-Sync
  exec('$HOME/.nvm/nvm.sh use 5 && browser-sync start --config=bs-config.js');

  // Watch and compile Sass
  exec('rvm use 2.2.4 && compass watch Sites/assets');

  // Watch and compile CoffeeScript
  exec('coffee -cw Sites/assets');
});
