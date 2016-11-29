// controller 
import Ember from 'ember';
import defaultTheme from '../themes/default-theme';

 
export default Ember.Controller.extend({
  //main data of the chart
  //define the type, the title and the sting numbers of the q (Q1,Q2,Q3 and Q4)
  
  chartOptions: {
    chart: {
      type: 'bar'
    },
    title: {
      text: 'Class Average'
    },
    xAxis: {
      title: {
        text: ''
      },
    labels: {
    //Generate the labels of each quarter
    formatter: function() {
      return 'Q'+(this.value+1);
    }
    }
    },
    yAxis: {
      title: {
        text: ''
      }
    }
  },
  //Retrive the data dynamically from the model which is directly connected to the API(Server)
  chartData: function(){
      return this.get('model')}.property('model.@each'),

      theme: defaultTheme

  
});