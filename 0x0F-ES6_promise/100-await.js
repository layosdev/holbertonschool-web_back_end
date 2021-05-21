import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let photo;
  let user;

  try {
    user = await createUser();
    photo = await uploadPhoto();
  } catch (error) {
    return {
      photo: null,
      user: null,
    };
  }
  return {
    photo,
    user,
  };
}
