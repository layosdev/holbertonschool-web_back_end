export default function createIteratorObject(report) {
  const employees = [];

  const departmentsList = Object.values(report.allEmployees);
  for (const employee of departmentsList) {
    employees.push(...employee);
  }

  return employees;
}
