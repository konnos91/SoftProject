import DS from 'ember-data';

export default DS.Model.extend({ 
//the man model of our system
  studentid: DS.attr('number'),
  name: DS.attr('string'),
  birth: DS.attr('string'),
  stclass: DS.attr('string'),
  Year: DS.attr('string'),
  Quarter: DS.attr('string'),
  math: DS.attr('number'),
  computer: DS.attr('number'),
  literature: DS.attr('number'),
});
