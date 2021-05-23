import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2])
      .then((data) => {
        const res = [];
        res.push('This is the list of our students');
        for (const i in data) {
          if (i) {
            res.push(
              `Number of students in ${i}: ${data[i].number}. ${data[i].list}`,
            );
          }
        }
        response.send(res.join('\n'));
      })
      .catch((error) => {
        response.send(error.message);
      });
  }

  static getAllStudentsByMajor(request, response) {
    if (!['SWE', 'CS'].includes(request.params.major)) {
      response.status(500).send('Major parameter must be CS or SWE');
    } else {
      readDatabase(process.argv[2])
        .then((data) => {
          response.send(data[request.params.major].list);
        })
        .catch((err) => {
          response.send(err.message);
        });
    }
  }
}

export default StudentsController;
