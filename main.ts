import { Application } from "https://deno.land/x/oak/mod.ts";
import { config } from "https://deno.land/x/dotenv/mod.ts";
import { oakCors } from "https://deno.land/x/cors/mod.ts";
import Router from "./routes.ts";
import { logging, timing } from "./utils/logging.ts";
import { errorHandler } from "./utils/errorHandler.ts";

const env = config();

const port = 8000;

const app = new Application();

app.use(logging);
app.use(timing);
app.use(errorHandler);
app.use(oakCors());
app.use(Router.routes());

console.log(`Listening on http://localhost:${port}`);
await app.listen({ port: port });
