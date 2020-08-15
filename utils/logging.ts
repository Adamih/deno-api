import { Context } from "https://deno.land/x/oak/mod.ts";

const logging = async (ctx: Context, next: Function) => {
  await next();
  const rt = ctx.response.headers.get("X-Response-Time");
  console.log(`${ctx.request.method} ${ctx.request.url} - ${rt}`);
};

const timing = async (ctx: Context, next: Function) => {
  const start = Date.now();
  await next();
  const ms = Date.now() - start;
  ctx.response.headers.set("X-Response-Time", `${ms}ms`);
};

export { logging, timing };
