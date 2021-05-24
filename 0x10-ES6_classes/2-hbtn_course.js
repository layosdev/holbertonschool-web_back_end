/* eslint-disable no-underscore-dangle */
export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  // Getters
  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  // Setters
  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    } else throw new TypeError('Name must be a string');
  }

  set length(length) {
    if (typeof length === 'number') {
      this._length = length;
    } else throw new TypeError('Length must be a number');
  }

  set students(students) {
    if (Array.isArray(students)) {
      this._students = students;
    }
  }
}
