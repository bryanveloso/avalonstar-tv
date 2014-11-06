require 'autoprefixer-rails'

http_path = "/"
css_dir = "avalonstar/static/stylesheets"
sass_dir = "avalonstar/assets/stylesheets"
images_dir = "avalonstar/static/images"
javascripts_dir = "avalonstar/static/javascripts"

# Output options.
line_comments = false
output_style = (environment == :production) ? :compressed : :compact

on_stylesheet_saved do |file|
  css = File.read(file)
  File.open(file, 'w') do |io|
    io << AutoprefixerRails.process(css)
  end
end
