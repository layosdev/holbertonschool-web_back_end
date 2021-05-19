function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw Error('Position outside range');
  }

  const arrayBuffer = new ArrayBuffer(length);
  const dataView = new Int8Array(arrayBuffer);

  dataView.set([value], position);

  const newDataView = new DataView(arrayBuffer);

  return newDataView;
}

export default createInt8TypedArray;
