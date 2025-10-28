import type { Env } from "./types";

const SIZE_UNITS = ["B", "KB", "MB", "GB", "TB"];

export function sanitizeFilename(name: string): string | null {
  const trimmed = name.trim();
  if (!trimmed) return null;
  const parts = trimmed.replace(/\\/g, "/").split("/");
  const candidate = parts[parts.length - 1];
  if (!candidate || candidate === "." || candidate === "..") {
    return null;
  }
  return candidate;
}

export function normalizePath(raw: string | null | undefined): string {
  if (!raw) return "";
  const clean = raw.replace(/\\/g, "/");
  const parts = clean
    .split("/")
    .map((segment) => segment.trim())
    .filter((segment) => segment && segment !== ".");

  const stack: string[] = [];
  for (const segment of parts) {
    if (segment === "..") {
      if (stack.length) stack.pop();
      continue;
    }
    stack.push(segment);
  }

  return stack.join("/");
}

export function formatSize(bytes: number): string {
  if (bytes === 0) return "0 B";
  let size = bytes;
  for (const unit of SIZE_UNITS) {
    if (size < 1024 || unit === SIZE_UNITS[SIZE_UNITS.length - 1]) {
      return unit === "B" ? `${Math.round(size)} ${unit}` : `${size.toFixed(1)} ${unit}`;
    }
    size /= 1024;
  }
  return `${size.toFixed(1)} TB`;
}

export function allowUpload(env: Env): boolean {
  const value = env.ALLOW_UPLOAD ?? "true";
  return value.toString().toLowerCase() !== "false";
}

export function maxUploadSize(env: Env): number {
  const value = Number(env.MAX_UPLOAD_SIZE ?? "104857600");
  return Number.isFinite(value) && value > 0 ? value : 104857600;
}

export function resolveAdminCredentials(env: Env): { username: string; password: string } | null {
  const username = (env.AUTH_USER ?? "admin").trim();
  const password = (env.AUTH_PASS ?? "admin").trim();
  if (!username && !password) {
    return null;
  }
  return { username, password };
}

export function requiresAdminAuth(env: Env): boolean {
  return resolveAdminCredentials(env) !== null;
}

export async function readNotice(env: Env): Promise<string> {
  const object = await env.FILES.get("__meta/notice_board.txt");
  if (!object) return "";
  return await object.text();
}

export async function writeNotice(env: Env, text: string): Promise<void> {
  await env.FILES.put("__meta/notice_board.txt", text, {
    httpMetadata: { contentType: "text/plain; charset=utf-8" },
  });
}

export function listPrefixFor(path: string): string {
  return path ? `${path.replace(/\/+$/, "")}/` : "";
}

export function tokenFromRequest(request: Request): string | null {
  const header = request.headers.get("Authorization");
  if (header?.startsWith("Bearer ")) {
    return header.slice("Bearer ".length).trim() || null;
  }
  const url = new URL(request.url);
  const token = url.searchParams.get("token");
  return token ? token : null;
}

export function isTokenValid(request: Request, env: Env): boolean {
  const expected = env.AUTH_TOKEN;
  if (!expected) return true;
  const provided = tokenFromRequest(request);
  return !!(provided && timingSafeEqual(provided, expected));
}

export function isBasicAuthValid(request: Request, env: Env): boolean {
  const credentials = resolveAdminCredentials(env);
  if (!credentials) return true;
  const { username, password } = credentials;

  const header = request.headers.get("Authorization");
  if (!header?.startsWith("Basic ")) return false;

  try {
    const decoded = atob(header.slice("Basic ".length));
    const [providedUser, providedPass] = decoded.split(":", 2);
    if (providedUser === undefined || providedPass === undefined) {
      return false;
    }
    return timingSafeEqual(providedUser, username) && timingSafeEqual(providedPass, password);
  } catch {
    return false;
  }
}

export function unauthorizedResponse(message: string, opts: { basic?: boolean; bearer?: boolean } = {}): Response {
  const headers: HeadersInit = {
    "Content-Type": "text/plain; charset=utf-8",
  };
  if (opts.basic) {
    headers["WWW-Authenticate"] = 'Basic realm="NShare Admin"';
  }
  if (opts.bearer) {
    headers["WWW-Authenticate"] = "Bearer";
  }
  return new Response(message, { status: 401, headers });
}

export function forbidden(message: string): Response {
  return new Response(message, {
    status: 403,
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}

export function notFound(message: string = "Not found"): Response {
  return new Response(message, {
    status: 404,
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}

export function badRequest(message: string): Response {
  return new Response(message, {
    status: 400,
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}

function timingSafeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let result = 0;
  for (let i = 0; i < a.length; i += 1) {
    result |= a.charCodeAt(i) ^ b.charCodeAt(i);
  }
  return result === 0;
}
