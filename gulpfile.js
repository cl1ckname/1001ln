var gulp = require("gulp");
var rename = require("gulp-rename");
var sass = require("gulp-sass");
var autoprefixer = require("gulp-autoprefixer");
var sourcemaps = require("gulp-sourcemaps");
var browserSync = require("browser-sync").create();



function Sync(done) {
    browserSync.init({
        server: {
            baseDir: "./static",
            index: "./html/index.html"
        },
        host: 'localhost',
        port: 9000,
        // serveStatic: ["./static"],
        open: false,
    });
    gulp.watch('./static/html/*.html').on("change",browserSync.reload);
    gulp.watch('./static/scss/*.scss').on('change',css_style);
    done();
}
function css_style() {
    gulp.src("./static/scss/style.scss")
    .pipe(sourcemaps.init())
    .pipe(sass({
        errorLogToConsole: true,
    }))
    .on('error', console.error.bind(console))
    .pipe(autoprefixer({
        cascade: false
    }))
    .pipe(rename({suffix: ".min"}))
    .pipe(sourcemaps.write('/'))
    .pipe(gulp.dest("./static/css/"))
    .pipe(browserSync.stream());

    
}

function watchSass(){
    gulp.watch("./scss/**/*",css_style)
}

function print(done){
    console.log("Heil");
    done();
}

gulp.task(Sync);
gulp.task(css_style);
gulp.task("default",Sync);


//gulp.task(print);
//gulp.task(css_style);