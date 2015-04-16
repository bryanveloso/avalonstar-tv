module.exports = (grunt) ->
  # Configuration.
  grunt.initConfig
    pkg: grunt.file.readJSON 'package.json'

    coffee:
      dist:
        expand: true,
        cwd: './avalonstar/assets/javascripts',
        src: ['*.coffee'],
        dest: './static/javascripts/application',
        ext: '.js'

    sass:
      dist:
        options:
          sourcemap: 'none'
          style: 'compact'
        files:
          './static/stylesheets/live.css': './avalonstar/assets/stylesheets/live.scss',
          './static/stylesheets/site.css': './avalonstar/assets/stylesheets/site.scss'

    autoprefixer:
      dist:
        files:
          './static/stylesheets/live.css': './static/stylesheets/live.css',
          './static/stylesheets/site.css': './static/stylesheets/site.css'

    watch:
      coffee:
        files: './avalonstar/assets/javascripts/*.coffee'
        tasks: ['coffee']
      sass:
        files: './avalonstar/assets/stylesheets/*.scss'
        tasks: ['sass', 'autoprefixer']

  # Imports.
  grunt.loadNpmTasks 'grunt-autoprefixer'
  grunt.loadNpmTasks 'grunt-contrib-coffee'
  grunt.loadNpmTasks 'grunt-contrib-sass'
  grunt.loadNpmTasks 'grunt-contrib-watch'

  # Task registration.
  grunt.registerTask 'default', [
    'coffee', 'sass', 'autoprefixer', 'watch'
  ]
