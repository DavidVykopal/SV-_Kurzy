import type { Env } from "./_lib/types";
import { renderIndex } from "./_lib/html";
import { listDirectory } from "./_lib/storage";
import {
  allowUpload,
  badRequest,
  isBasicAuthValid,
  isTokenValid,
  normalizePath,
  readNotice,
  unauthorizedResponse,
  notFound,
  requiresAdminAuth,
} from "./_lib/utils";

export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  if (!isTokenValid(request, env)) {
    return unauthorizedResponse("Unauthorized", { bearer: true });
  }

  const url = new URL(request.url);
  const rawPath = url.searchParams.get("path") ?? "";
  const currentPath = normalizePath(rawPath);

  try {
    const items = await listDirectory(env, currentPath);
    if (currentPath && items.length === 0) {
      const object = await env.FILES.head(currentPath);
      if (object) {
        return badRequest("Path points to a file, not a directory");
      }
      return notFound("Path not found");
    }

    const noticeText = await readNotice(env);
    const basicValid = isBasicAuthValid(request, env);
    const adminRequired = requiresAdminAuth(env);

    const html = renderIndex({
      currentPath,
      items,
      allowUpload: allowUpload(env) && basicValid,
      tokenRequired: Boolean(env.AUTH_TOKEN),
      noticeText,
      canEdit: basicValid,
      adminRequired,
    });

    return new Response(html, {
      headers: { "Content-Type": "text/html; charset=utf-8" },
    });
  } catch (error) {
    console.error("Error rendering index", error);
    return badRequest("Unable to load directory");
  }
};
