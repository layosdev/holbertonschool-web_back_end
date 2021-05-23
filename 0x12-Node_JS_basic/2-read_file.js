const fs = require('fs');

function countStudents(path) {
  const fields = {};
  let fileData;

  try {
    fileData = fs.readFileSync(path, 'utf8').split('\n');
    fileData = fileData.filter((element) => element.length > 0);
    fileData.shift();
    console.log(`Number of students: ${fileData.length}`);
  } catch (error) {
    throw Error('Cannot load the database');
  }

  fileData.forEach((x) => {
    const student = x.split(',');
    if (!fields[student[3]]) {
      fields[student[3]] = [];
    }
    fields[student[3]].push(student[0]);
  });

  for (const i in fields) {
    if (i) {
      console.log(
        `Number of students in ${i}: ${fields[i].length}. List: ${fields[
          i
        ].join(', ')}`,
      );
    }
  }
}

module.exports = countStudents;
