const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('Sum Two Integers', function () {
    it('should return 4', function () {
      assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    });
  });

  describe('Substract Two Integers', function () {
    it('should return 2', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1, 3), 2);
    });
  });

  describe('Divide Two Integers', function () {
    it('should return 1.5', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 3, 2), 1.5);
    });
  });

  describe('Divide by 0', function () {
    it('should return Error', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 2, 0), 'Error');
    });
  });
});
