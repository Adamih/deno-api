import * as yup from "https://cdn.pika.dev/yup@^0.29.1";

interface IDinosaur {
  id: string;
  name: string;
  image: string;
}

const DB = new Map<string, IDinosaur>();

const dinosaurSchema = yup.object({
  name: yup.string().trim().min(2).required(),
  image: yup.string().trim().url().required(),
});

export { IDinosaur, DB, dinosaurSchema };
