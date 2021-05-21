import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const profile = await signUpUser(firstName, lastName);
  let picName;
  try {
    picName = await uploadPhoto(fileName);
  } catch (err) {
    picName = err.toString();
  }
  return [
    { value: profile, status: 'fulfilled' },
    { value: picName, status: 'rejected' },
  ];
}

export default handleProfileSignup;
