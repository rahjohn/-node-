/*************************************************************************
You will need to fill out this file with Sequelize database connection 
information.  You will also need to rename this file db.js.  Make sure 
that you "export" (make externally available) the resources that you will
import (i.e., "require") and create in this file.  You should need no more \
than about 2 lines of code in this file.  You should read the 
documentation referenced on the lab specs before attempting to create this 
connection file.  If you took IT210A this will be similar to the database 
connection file you made for PHP in Lab 3.
**************************************************************************/

var sequelize = new Sequelize('it210b', 'guest', 'guest', {
    host: 'localhost',
    dialect: 'mysql'|'mariadb'|'sqlite'|'postgres'|'mssql',

    pool: {
        max: 5,
        min: 0,
        idle: 10000
    },

    // SQLite only
    storage: 'path/to/database.sqlite'
});

// Or you can simply use a connection uri
var sequelize = new Sequelize('postgres://guest:guest@guest.com:1337/it210b');
