const chai = require("chai");
const calculateNumber = require('./1-calcul');

const expect = chai.expect;


describe('calculateNumber', function () {
  describe("Sum Two Integers", function() {
    it("should return 4", function() {
      expect(calculateNumber('SUM', 2, 2)).to.be.equal(4);
    });
  });

  describe("SUBTRACT Two Integers", function() {
    it("should return 0", function() {
      expect(calculateNumber('SUBTRACT', 2, 2)).to.be.equal(0);
    });
  });

  describe("Divide Two Integers", function() {
    it("should return 5", function() {
      expect(calculateNumber('DIVIDE', 10, 2)).to.be.equal(5);
    });
  });

  describe("Divide Two Integers", function() {
    it("should return Error", function() {
      expect(calculateNumber('DIVIDE', 10, 0)).to.be.equal('Error');
    });
  });
});
