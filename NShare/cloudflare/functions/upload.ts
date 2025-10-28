import type { Env } from "./_lib/types";
import {
  allowUpload,
  badRequest,
  forbidden,
  isBasicAuthValid,
  isTokenValid,
  maxUploadSize,
  normalizePath,
  sanitizeFilename,
  unauthorizedResponse,
  requiresAdminAuth,
} from "./_lib/utils";
import { renderUploadForm } from "./_lib/html";

export const onRequestGet: PagesFunction<Env> = async ({ request, env }) => {
  if (!isTokenValid(request, env)) {
    return unauthorizedResponse("Unauthorized", { bearer: true });
  }

  if (!allowUpload(env)) {
    return forbidden("Uploads disabled");
  }

  const basicValid = isBasicAuthValid(request, env);
  if (!basicValid && requiresAdminAuth(env)) {
    return unauthorizedResponse("Authentication required", { basic: true });
  }

  const url = new URL(request.url);
  const currentPath = normalizePath(url.searchParams.get("path") ?? "");
  const html = renderUploadForm(currentPath);
  return new Response(html, {
    headers: { "Content-Type": "text/html; charset=utf-8" },
  });
};

export const onRequestPost: PagesFunction<Env> = async ({ request, env }) => {
  if (!isTokenValid(request, env)) {
    return unauthorizedResponse("Unauthorized", { bearer: true });
  }

  if (!allowUpload(env)) {
    return forbidden("Uploads disabled");
  }

  if (!isBasicAuthValid(request, env) && requiresAdminAuth(env)) {
    return unauthorizedResponse("Authentication required", { basic: true });
  }

  const formData = await request.formData();
  const target = normalizePath(String(formData.get("target") ?? ""));
  const files = formData.getAll("files");

  if (files.length === 0) {
    return badRequest("No files provided");
  }

  const maxSize = maxUploadSize(env);
  let totalSize = 0;
  const uploads: Array<{ key: string; file: File }> = [];

  for (const entry of files) {
    if (!(entry instanceof File)) {
      continue;
    }
    const sanitized = sanitizeFilename(entry.name);
    if (!sanitized) {
      continue;
    }

    const key = target ? `${target}/${sanitized}` : sanitized;
    if (key.startsWith("__meta/")) {
      return forbidden("Reserved path");
    }

    totalSize += entry.size;
    if (totalSize > maxSize) {
      return badRequest("Upload exceeds maximum allowed size");
    }

    uploads.push({ key, file: entry });
  }

  if (uploads.length === 0) {
    return badRequest("No valid files to upload");
  }

  for (const { key, file } of uploads) {
    await env.FILES.put(key, file.stream(), {
      httpMetadata: {
        contentType: file.type || "application/octet-stream",
        contentDisposition: `attachment; filename="${file.name}"`,
      },
    });
  }

  const redirectPath = target ? `/?path=${encodeURIComponent(target)}` : "/";
  return new Response(null, {
    status: 303,
    headers: { Location: redirectPath },
  });
};
