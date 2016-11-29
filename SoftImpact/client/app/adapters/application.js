import DS from 'ember-data';

export default DS.RESTAdapter.extend({
  host: 'http://localhost:8080', //connect to the server and each time get the approprite parameter 
  corsWithCredentials:true,
});
