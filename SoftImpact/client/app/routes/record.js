import Ember from 'ember';  

export default Ember.Route.extend({
  	model:function(params) {
       //get the JSON values from the specified url
  	   var url = 'http://localhost:8080/students/'+params.student_id;
	  //return this.store.findRecord('statistic',params.student_id).then(function(data) {
	  return Ember.$.getJSON(url).then(function(data) {

		//adds the data to/from an array. splice(0,2) is the number of items to be displayed: is 2

		//array to strorw the results which will produce the grap
		//get the records to identify the name and q1,q2,q3 and q4
		var temprecs = data.statistics; //error undefined 
		console.log(temprecs);

	   });
	}


});