/* eslint-disable no-underscore-dangle */
export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') throw new Error('Class extending Building must override evacuationWarningMessage');
    this._sqft = sqft;
  }

  // getters
  get sqft() {
    return this._sqft;
  }

  // setters

  // set sqft(sqft) {
  //   this._sqft = sqft;
  // }
}
