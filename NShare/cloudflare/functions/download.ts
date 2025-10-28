import type { Env } from "./_lib/types";
import {
  badRequest,
  isTokenValid,
  normalizePath,
  notFound,
  unauthorizedResponse,
} from "./_lib/utils";

export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  if (!isTokenValid(request, env)) {
    return unauthorizedResponse("Unauthorized", { bearer: true });
  }

  const url = new URL(request.url);
  const rawPath = url.searchParams.get("path");
  if (!rawPath) {
    return badRequest("Missing path parameter");
  }
  const key = normalizePath(rawPath);
  if (!key) {
    return badRequest("Invalid path");
  }

  const object = await env.FILES.get(key);
  if (!object) {
    return notFound("File not found");
  }

  const headers: HeadersInit = {
    "Content-Length": object.size.toString(),
    "Content-Type": object.httpMetadata?.contentType || "application/octet-stream",
    "Content-Disposition": object.httpMetadata?.contentDisposition || `attachment; filename="${key.split("/").pop()}"`,
  };

  return new Response(object.body, {
    headers,
  });
};
