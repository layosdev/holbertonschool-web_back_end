function cleanSet(mySet, startString) {
  if ((typeof mySet !== 'object')
  || (typeof startString !== 'string')
  || (startString.length === 0)
  ) {
    return '';
  }

  const stringSet = [];
  for (const i of mySet) {
    if (i && i.startsWith(startString)) {
      stringSet.push(i.slice(startString.length));
    }
  }
  return stringSet.join('-');
}

export default cleanSet;
