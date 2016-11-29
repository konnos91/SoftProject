import Ember from 'ember';

export default Ember.Controller.extend({
  actions:{
    deleteStudent: function(id){
      this.store.findRecord('student', id).then(function(student){
        student.deleteRecord();

        student.save();
      });
    }
  }
});