# Denosaur-fetching API built with deno 🦕 and Oak 🌳

## Start deno 🚀

`deno run --allow-read --allow-net main.ts`

## Endpoints 🚪

- `http://localhost:8000/dinosaur`
  - GET
  - POST
- `http://localhost:8000/dinosaur/:id`
  - PUT
  - DELETE

Do you really need anything more? I didn't think so.

## Anatomy of a denosaur ✨

No two dinosaurs look the same. The visual element combined with it's name is required to really capture it's personality.

example:

```json
{
  "name": "Denver",
  "img": "https://raw.githubusercontent.com/github/explore/master/topics/deno/deno.png",
  "id": "cc3ac624-a239-48b8-b5cd-d842560d950e"
}
```
