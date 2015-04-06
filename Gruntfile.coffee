module.exports = (grunt) ->
  # Configuration.
  grunt.initConfig
    pkg: grunt.file.readJSON 'package.json'

    coffee:
      dist:
        expand: true,
        cwd: './avalonstar/assets/javascripts',
        src: ['*.coffee'],
        dest: './avalonstar/static/javascripts/application',
        ext: '.js'

    sass:
      dist:
        options:
          style: 'compact'
        files:
          './avalonstar/static/stylesheets/live.css': './avalonstar/assets/stylesheets/live.scss',
          './avalonstar/static/stylesheets/site.css': './avalonstar/assets/stylesheets/site.scss'

    autoprefixer:
      dist:
        files:
          './avalonstar/static/stylesheets/live.css': './avalonstar/static/stylesheets/live.css',
          './avalonstar/static/stylesheets/site.css': './avalonstar/static/stylesheets/site.css'

    watch:
      coffee:
        files: './avalonstar/assets/javascripts/*.coffee'
        tasks: ['coffee']
      sass:
        files: './avalonstar/assets/stylesheets/*.scss'
        tasks: ['sass', 'autoprefixer']
      options: {livereload: true}

  # Imports.
  grunt.loadNpmTasks 'grunt-autoprefixer'
  grunt.loadNpmTasks 'grunt-contrib-coffee'
  grunt.loadNpmTasks 'grunt-contrib-sass'
  grunt.loadNpmTasks 'grunt-contrib-watch'

  # Task registration.
  grunt.registerTask 'default', [
    'coffee', 'sass', 'autoprefixer', 'watch'
  ]
