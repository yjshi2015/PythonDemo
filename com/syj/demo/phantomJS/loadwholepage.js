var url = 'http://movie.mtime.com/260270/';
var page = require('webpage').create();

console.log('The default user agent is ' + page.settings.userAgent);
page.settings.userAgent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0';

page.open(url, function(status) {
    if(status != 'success') {
        console.log('Unable to access network');
    } else {
        var ua = page.evaluate(function() {
            return document.getElementById('ratingRegion').textContent;
        })
        console.log(ua);
    }
    phantom.exit();
});