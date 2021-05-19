function updateStudentGradeByCity(students, city, newGrades) {
  const studentsList = students
    .filter((student) => student.location.localeCompare(city) === 0)
    .map((i) => {
      const grade = newGrades.filter((j) => j.studentId === i.id);
      const student = i;

      if (grade.length === 1) {
        student.grade = grade[0].grade;
      } else {
        student.grade = 'N/A';
      }

      return student;
    });

  return studentsList;
}

export default updateStudentGradeByCity;
