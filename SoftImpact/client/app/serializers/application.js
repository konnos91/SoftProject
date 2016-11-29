import DS from 'ember-data';

export default DS.RESTSerializer.extend({
  //the restserializer here will help us to normalize the records that we get from the server
  //to put them in the rigth JSON model that the ember can accept, which this reiqures a unique id which the records must have
  //otherwise the system will fail to start
  isNewSerializerAPI: true,

  normalizeArrayResponse: function(store, primaryModelClass, payload, id, requestType) {
    var normalizedRecords = [];

    payload.map(function(record){
      record.type = primaryModelClass.modelName;
      normalizedRecords.push(record);
    });

    var obj = {};
    obj[primaryModelClass.modelName] = normalizedRecords;


    return this._super(store, primaryModelClass, obj, id, requestType);
   }
});