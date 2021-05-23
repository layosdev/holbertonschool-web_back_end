const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, fileData) => {
      if (error) {
        reject(Error('Cannot load the database'));
        return;
      }
      const res = [];

      if (fileData) {
        const fields = {};
        let data = fileData.toString().split('\n');
        data = data.filter((element) => element.length > 0);
        data.shift();
        res.push(`Number of students: ${data.length}`);
        console.log(res[0]);

        data.forEach((item) => {
          const student = item.split(',');
          if (!fields[student[3]]) {
            fields[student[3]] = [];
          }
          fields[student[3]].push(student[0]);
        });

        for (const i in fields) {
          if (i) {
            res.push(
              `Number of students in ${i}: ${
                fields[i].length
              }. List: ${fields[i].join(', ')}`,
            );
            console.log(
              `Number of students in ${i}: ${
                fields[i].length
              }. List: ${fields[i].join(', ')}`,
            );
          }
        }
      }
      resolve(res);
    });
  });
}

module.exports = countStudents;
