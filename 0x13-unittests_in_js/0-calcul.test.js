const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  describe('Two Integers', function () {
    it('should return 4', function () {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
  });

  describe('Second decimal', function () {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(3.7, 1), 5);
    });
  });

  describe('First decimal', function () {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });

  describe('Both decimal', function () {
    it('should return 7', function () {
      assert.strictEqual(calculateNumber(1.5, 5.3), 7);
    });
  });

  describe('Other datatype', function () {
    it('should return NaN', function () {
      assert.strictEqual(calculateNumber("a", 6), NaN);
    });
  });
});

