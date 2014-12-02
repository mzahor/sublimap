var gulp = require('gulp');
var watch = require('gulp-watch');

var path_to_sublime = '/Users/marianzagoruiko/Library/Application Support/Sublime Text 2/Packages/User/';

gulp.task('default', function() {
    gulp.src('*.py')
        .pipe(watch('*.py', function(files) {
            return files.pipe(gulp.dest(path_to_sublime));
        }))
});