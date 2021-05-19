function updateUniqueItems(myMap) {
  if (!(myMap instanceof Map)) {
    throw Error('Cannot process');
  }

  myMap.forEach((key, value) => {
    if (key === 1) {
      myMap.set(value, 100);
    }
  });

  return myMap;
}

export default updateUniqueItems;
