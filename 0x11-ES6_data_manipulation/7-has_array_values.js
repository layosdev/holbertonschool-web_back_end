function hasValuesFromArray(set, array) {
  const status = array.every((i) => set.has(i));
  return status;
}

export default hasValuesFromArray;
