export default function createReportObject(employeesList) {
  const newObjt = {
    allEmployees: employeesList,
    getNumberOfDepartments: (x) => Object.keys(x).length,
  };
  return newObjt;
}
