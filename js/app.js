/*//Force https protocol for Save to Drive functionality
window.onload = function(){
    if (window.location.protocol == "http:")
	window.location.href = "https:" + window.location.href.substring(window.location.protocol.length)
};
*/

var app = angular.module('jazzGalleryApp', [
    'ngRoute',
    'galleryControllers'
]);

app.service('sharedProperties', function () {
    var propertyValue = {
	data:{}
    };

    return {
	getProperty: function () {
	    return propertyValue.data;
	},
	setProperty: function (value) {
	    propertyValue.data = value;
	    alert(propertyValue.data);
	}
    };
});

//ROUTING ================================================
app.config(['$routeProvider',
	    function($routeProvider) {
    $routeProvider
	
	.when('/', {
	    templateUrl: 'gallery.html',
	    controller : 'galleryViewController'
	})
        .when('/views/:viewid', {
	    templateUrl: 'piece-detail.html',
	    controller : 'pieceViewController'
	});
	    }]);

