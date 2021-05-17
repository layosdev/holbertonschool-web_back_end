export default function createEmployeesObject(departmentName, employees) {
  const newObjt = {
    [departmentName]: employees,
  };
  return newObjt;
}
