/*********************************************************
This model connects to the 'images' table in your database.
This will be a similar connection to the users.js model also
found in this folder.  You will need to examine the database 
that you imported and add functionality to this file to allow
it to function like the users.js model.  Make sure that you 
export this model so that the data in it can be used in the 
controller.
*********************************************************/


//DO WORK HERE PART 1!  Add code to this document similar to the users.js model for the images table in your database. Be sure to watch capitalization. Note that Timestamps are DATE objects, not STRING objects

var	db = require('../db.js'), //This imports the database connection and makes it usable by this page.
    sequelize = db.sequelize, //This imports the sequelize package to utilize in querying the database for information.
    Sequelize = db.Sequelize; //This imports the exact database connection information from db.js for information.

/*The following function creates the images table in the database if the table does not exist.  A data precautionary step.*/
var Images = sequelize.define('images', {
    imageId: {type: Sequelize.INTEGER, primaryKey: true, autoIncrement: true},
    imagePath: Sequelize.STRING,
    imageApproved: Sequelize.STRING,
    altText: Sequelize.STRING,
    userId: Sequelize.INTEGER,
    numLikes: Sequelize.INTEGER,
    createdAt: Sequelize.DATE,
    updatedAt: Sequelize.DATE
});


exports.Images = Images; //This exports the data from the the users table in the database for use in controllers.
