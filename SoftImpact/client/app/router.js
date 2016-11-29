import Ember from 'ember';  
import config from './config/environment';

const Router = Ember.Router.extend({  
  location: config.locationType
});

//define all the suitable routes of the program
Router.map(function() {
  this.route('manage');
  this.route('new');
  this.route('record', { path: 'record/:student_id'});
  this.route('statistic',{ path: '/statistic/:student_id'});
  this.route('computer',   {path: '/computer/'});
  this.route('math',   {path: '/math/'});
  this.route('literature',   {path: '/literature/'});
  this.route('quarter',{path: '/quarter/'});
  this.route('quartertwo',{path: '/quartertwo/'});
  this.route('quarterthree',{path: '/quarterthree/'});
  this.route('home');



});

export default Router;
