import type { Env } from "../_lib/types";
import {
  allowUpload,
  badRequest,
  forbidden,
  isBasicAuthValid,
  isTokenValid,
  normalizePath,
  unauthorizedResponse,
  requiresAdminAuth,
} from "../_lib/utils";
import { deletePath } from "../_lib/storage";

export const onRequestDelete: PagesFunction<Env> = async ({ request, env }) => {
  if (!isTokenValid(request, env)) {
    return unauthorizedResponse("Unauthorized", { bearer: true });
  }

  if (!allowUpload(env)) {
    return forbidden("Read-only mode");
  }

  if (!isBasicAuthValid(request, env) && requiresAdminAuth(env)) {
    return unauthorizedResponse("Authentication required", { basic: true });
  }

  const url = new URL(request.url);
  const rawPath = url.searchParams.get("path");
  if (!rawPath) {
    return badRequest("Missing path parameter");
  }
  const path = normalizePath(rawPath);
  if (!path) {
    return badRequest("Invalid path");
  }

  try {
    await deletePath(env, path);
  } catch (error) {
    console.error("Delete error", error);
    return badRequest("Failed to delete target");
  }

  return new Response(JSON.stringify({ success: true, path }), {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};
