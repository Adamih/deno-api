import { Context } from "https://deno.land/x/oak/mod.ts";

const errorHandler = async (ctx: Context, next: Function) => {
  try {
    await next();
  } catch (err) {
    ctx.response.status = err.status || 500;
    ctx.response.body = { message: err.message };
  }
};

export { errorHandler };
