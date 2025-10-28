import type { Env } from "../_lib/types";
import {
  allowUpload,
  badRequest,
  forbidden,
  isBasicAuthValid,
  isTokenValid,
  readNotice,
  unauthorizedResponse,
  writeNotice,
  requiresAdminAuth,
} from "../_lib/utils";

export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  if (!isTokenValid(request, env)) {
    return unauthorizedResponse("Unauthorized", { bearer: true });
  }

  const text = await readNotice(env);
  return new Response(JSON.stringify({ text }), {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};

export const onRequestPost: PagesFunction<Env> = async ({ request, env }) => {
  if (!isTokenValid(request, env)) {
    return unauthorizedResponse("Unauthorized", { bearer: true });
  }

  if (!allowUpload(env)) {
    return forbidden("Read-only mode");
  }

  if (!isBasicAuthValid(request, env) && requiresAdminAuth(env)) {
    return unauthorizedResponse("Authentication required", { basic: true });
  }

  let payload: unknown;
  try {
    payload = await request.json();
  } catch {
    return badRequest("Invalid JSON payload");
  }

  if (typeof payload !== "object" || payload === null || typeof (payload as any).text !== "string") {
    return badRequest("Missing text field");
  }

  const text = (payload as any).text;
  await writeNotice(env, text);

  return new Response(JSON.stringify({ success: true, text }), {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};
