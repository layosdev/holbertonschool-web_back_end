const fs = require('fs');

const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, (error, fileData) => {
    if (error) {
      reject(Error('Cannot load the database'));
    }
    if (fileData) {
      const fields = {};
      const info = {};
      let data = fileData.toString().split('\n');
      data = data.filter((element) => element.length > 0);
      data.shift();
      data.forEach((item) => {
        const student = item.split(',');
        if (!fields[student[3]]) {
          fields[student[3]] = [];
        }
        fields[student[3]].push(student[0]);
      });
      for (const i in fields) {
        if (i) {
          const list = fields[i];
          info[i] = {
            list: `List: ${fields[i].join(', ')}`,
            number: list.length,
          };
        }
      }

      resolve(info);
    }
  });
});

module.exports = readDatabase;
