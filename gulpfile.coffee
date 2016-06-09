gulp = require('gulp')
exec = require('child_process').exec

gulp.task 'default', ->
  # Start the development server
  exec './manage.py runserver --settings=settings_development.py'

  # Start Browser-Sync
  exec '$HOME/.nvm/nvm.sh use 5 && browser-sync start --config=bs-config.js'

  # Watch and compile Sass
  exec 'rvm use 2.2.4 && compass watch Sites/assets/'
  exec 'rvm use 2.2.4 && compass watch Blog/assets/'

  # Watch and compile CoffeeScript
  exec 'coffee -cw Sites/assets/'
  exec 'coffee -cw Blog/assets/'
  return
