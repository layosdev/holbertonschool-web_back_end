function getStudentsByLocation(students, city) {
  const studentsList = students.filter(
    (student) => student.location.localeCompare(city) === 0,
  );
  return studentsList;
}

export default getStudentsByLocation;
