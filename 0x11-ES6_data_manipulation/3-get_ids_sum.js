function getStudentIdsSum(students) {
  const studentsIdSum = students.reduce(
    (total, student) => total + student.id,
    0,
  );
  return studentsIdSum;
}

export default getStudentIdsSum;
