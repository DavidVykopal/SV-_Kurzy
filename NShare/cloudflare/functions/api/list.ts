import type { Env } from "../_lib/types";
import { isTokenValid, normalizePath, unauthorizedResponse } from "../_lib/utils";
import { listDirectory } from "../_lib/storage";

export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  if (!isTokenValid(request, env)) {
    return unauthorizedResponse("Unauthorized", { bearer: true });
  }

  const url = new URL(request.url);
  const path = normalizePath(url.searchParams.get("path") ?? "");
  const items = await listDirectory(env, path);

  const body = JSON.stringify({ path, items });
  return new Response(body, {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};
